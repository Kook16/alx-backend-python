import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseConnection()
        self.db.connect()

    def tearDown(self):
        self.db.disconnect()

    def test_query(self):
        result = self.db.query("SELECT * FROM users")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
