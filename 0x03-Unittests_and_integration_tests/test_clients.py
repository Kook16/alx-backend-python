#!/usr/bin/env python3
"""UNIT & INTEGRATION TESTS MODULE"""

# Import necessary modules and functions for testing
import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient, get_json
from fixtures import TEST_PAYLOAD
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ('google',),
        ('apple',),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """
        Test that the org method returns the correct data
        """
        ORG_URL = "https://api.github.com/orgs/"
        # Instantiate the GithubOrgClient with the organization name
        client = GithubOrgClient(org)
        result = client.org
        # Verify the return value and the call to get_json
        self.assertEqual(result, mock_get_json.return_value)
        mock_get_json.assert_called_once()
        mock_get_json.assert_called_with(f"{ORG_URL}{org}")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test the _public_repos_url property
        """
        mock_org.return_value = {"repos_url": "mock_url"}
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("dummy_org")
        result = client._public_repos_url
        # Verify the repos_url is correctly fetched from the org property
        self.assertEqual(result, "mock_url")
        mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test the public_repos method
        """
        mock_get_json.return_value = [{'name': 'nema'}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'mock_url'
            # Call public_repos and verify the output
            client = GithubOrgClient('org')
            result = client.public_repos()
            self.assertEqual(result, ['nema'])
            mock_get_json.assert_called_once_with('mock_url')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, key, expected):
        """
        Test the has_license method
        """
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient using fixtures
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class-level mocks for requests.get
        """
        config = {
            'return_value.json.side_effect': [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Stop the class-level patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos method with integration data
        """
        client = GithubOrgClient("lax")
        # Verify the org property and public_repos method
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """
        Test public_repos with a specific license filter
        """
        client = GithubOrgClient("lax")
        # Verify the output of public_repos with and without license filter
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.mock_get.assert_called()
