import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        self.storage.new(obj)
        with patch('builtins.open', new=StringIO()) as mock_output:
            self.storage.save()
            self.assertIn(obj.to_dict(), mock_output.getvalue())

    def test_reload(self):
        """Test the reload method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = obj.__class__.__name__ + '.' + obj.id
        self.assertIn(key, self.storage.all())
