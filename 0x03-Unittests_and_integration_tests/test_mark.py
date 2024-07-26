# Marking Tests as Expected Failures
'''In addition to skipping tests, unittest allows you to mark tests as expected failures using the @unittest.expectedFailure decorator.
This is useful when you have tests that are known to fail, and you want to acknowledge the failure without affecting the overall test results.'''

import unittest

class TestFailure(unittest.TestCase):

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 1, "broken")

if __name__ == '__main__':
    unittest.main()
