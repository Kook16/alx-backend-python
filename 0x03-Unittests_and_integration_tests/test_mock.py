# Mocking is a technique used in unit testing where you replace parts of your system under
# test with mock objects to isolate and test specific functionality.
# This allows you to simulate the behavior of complex objects and control their outputs.

# Basic concepts of mocking
# Define return values for methods.
# Track how methods are called.
# Make assertions about those calls.

from unittest.mock import Mock

# Create a mock object
mock = Mock()

# Set a return value for a method
mock.some_method.return_value = 'mocked'

# Call the method
result = mock.some_method()

# Assert the return value
assert result == 'mocked!'
