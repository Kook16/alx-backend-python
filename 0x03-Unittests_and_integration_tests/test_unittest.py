import unittest

# Define a class that inherits from unittest.TestCase
class TestStringMethods(unittest.TestCase):

    # Each method that starts with 'test' will be run as a test case
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello','world'])

        # Check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

# Run the tests
if __name__ == '__main__':
    unittest.main()
