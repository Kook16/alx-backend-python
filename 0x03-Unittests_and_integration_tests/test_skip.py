'''
Skipping tests is a feature in the unittest framework that allows you to bypass certain tests based on specified conditions.
This can be particularly useful in scenarios where certain tests are not applicable or when you know that specific tests are expected to fail under certain conditions.
'''
import unittest

class TestMath(unittest.TestCase):

    # Unconditionally Skip a Test
    '''
    You can skip a test unconditionally using the @unittest.skip decorator. This is useful if you want to temporarily disable a test without deleting or commenting it out.
    '''

    @unittest.skip('demonstrating skipping')
    def test_nothing(self):
        self.fail('shouldnt happen')

    #  Conditionally Skip a Test
    '''
    You can skip a test based on a condition using the @unittest.skipIf
    and @unittest.skipUnless decorators.
    @unittest.skipIf(condition, reason): Skips the test if the condition is True.
    @unittest.skipUnless(condition): Skips the test unless the condition is True.
    '''

    @unittest.skipIf(1 == 1, "demonstrating skipping")
    def test_skip_if(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(1 == 2, "demonstrating skipping")
    def test_skip_unless(self):
        self.assertTrue(True)

    #  Skip a Test in a Method
    '''You can also skip tests programmatically within a test method using the self.skipTest(reason) method.'''
    def test_conditional_skip(self):
        if not False:
            self.skipTest('Condition not meet')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
