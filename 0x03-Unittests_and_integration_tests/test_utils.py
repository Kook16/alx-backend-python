#!/usr/bin/env python3
"""Unit and Integration Tests for Utility Functions"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """Unit tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_dict: Mapping, path: Sequence, expected_value: Any):
        """Test that access_nested_map returns the correct value"""
        self.assertEqual(access_nested_map(nested_dict, path), expected_value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_dict: Mapping, path: Sequence):
        """Test that access_nested_map raises a KeyError for invalid paths"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_dict, path)


class TestGetJson(TestCase):
    """Unit tests for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch("utils.requests.get")
    def test_get_json(self, url: str, expected_response: dict, mock_get: Any) -> None:
        """Test that get_json correctly fetches and returns JSON data"""
        mock_get.return_value.json.return_value = expected_response
        self.assertEqual(get_json(url), expected_response)
        mock_get.assert_called_once_with(url)


class TestMemoize(TestCase):
    """Unit tests for memoize decorator"""

    def test_memoize(self):
        """Test the memoize decorator to ensure it caches method results"""
        class DummyClass:
            """A simple class to test memoize decorator"""

            def compute_value(self) -> int:
                """A method that returns 42"""
                return 42

            @memoize
            def cached_value(self) -> Any:
                """A memoized method that calls compute_value"""
                return self.compute_value()

        with mock.patch.object(DummyClass, "compute_value") as mock_compute:
            instance = DummyClass()
            for _ in range(7):
                instance.cached_value
            # Verify that compute_value was called only once due to memoization
            mock_compute.assert_called_once()
