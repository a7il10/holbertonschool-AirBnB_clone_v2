import unittest
from models.__init__ import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down for the tests"""
        pass

    def test_do_create(self):
        """Test the do_create method"""
        result = self.console.do_create()
        self.assertIsNotNone(result)

    def test_do_show(self):
        """Test the do_show method"""
        result = self.console.do_show()
        self.assertIsNotNone(result)

    def test_do_destroy(self):
        """Test the do_destroy method"""
        result = self.console.do_destroy()
        self.assertIsNotNone(result)

    def test_do_all(self):
        """Test the do_all method"""
        result = self.console.do_all()
        self.assertIsNotNone(result)

    def test_do_count(self):
        """Test the do_count method"""
        result = self.console.do_count()
        self.assertIsNotNone(result)

    def test_do_update(self):
        """Test the do_update method"""
        result = self.console.do_update()
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
