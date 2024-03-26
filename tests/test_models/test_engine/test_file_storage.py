#!/usr/bin/python3
"""
Module for testing file storage
"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_get(self):
        """ Test get method """
        new = BaseModel()
        _id = new.to_dict()['id']
        self.assertEqual(new, storage.get('BaseModel', _id))

    def test_count(self):
        """ Test count method """
        num = storage.count()
        new = BaseModel()
        if num == 0:
            self.assertEqual(storage.count(), 1)
        else:
            self.assertEqual(storage.count(), num + 1)

    def test_count_cls(self):
        """ Test count method with class specified """
        num = storage.count()
        new = BaseModel()
        if num == 0:
            self.assertEqual(storage.count('BaseModel'), 1)
        else:
            self.assertEqual(storage.count('BaseModel'), num + 1)

    def test_count_fake_cls(self):
        """ Test count method with fake class """
        self.assertEqual(storage.count('MyModel'), 0)

    def test_get_none(self):
        """ Test get method with None """
        self.assertEqual(storage.get(None, None), None)

    def test_count_none(self):
        """ Test count method with None """
        self.assertEqual(storage.count(None), 0)

    def test_count_fake_id(self):
        """ Test count method with fake id """
        self.assertEqual(storage.count('BaseModel', 'fake_id'), 0)

    def test_get_fake_id(self):
        """ Test get method with fake id """
        self.assertEqual(storage.get('BaseModel', 'fake_id'), None)

    def test_get_fake_cls(self):
        """ Test get method with fake class """
        self.assertEqual(storage.get('MyModel', 'fake_id'), None)

    def test_count_new_cls(self):
        """ Test count method with new class """
        new = BaseModel()
        self.assertEqual(storage.count('MyModel'), 0)

    def test_get_new_cls(self):
        """ Test get method with new class """
        new = BaseModel()
        self.assertEqual(storage.get('MyModel', new.id), None)

    def test_count_new_id(self):
        """ Test count method with new id """
        new = BaseModel()
        self.assertEqual(storage.count('BaseModel', 'new_id'), 0)

    def test_get_new_id(self):
        """ Test get method with new id """
        new = BaseModel()
        self.assertEqual(storage.get('BaseModel', 'new_id'), None)

    def test_count_new_cls_id(self):
        """ Test count method with new class and id """
        new = BaseModel()
        self.assertEqual(storage.count('MyModel', 'new_id'), 0)

    def test_get_new_cls_id(self):
        """ Test get method with new class and id """
        new = BaseModel()
        self.assertEqual(storage.get('MyModel', 'new_id'), None)

    def test_count_new_cls_fake_id(self):
        """ Test count method with new class and fake id """
        new = BaseModel()
        self.assertEqual(storage.count('MyModel', 'fake_id'), 0)

    def test_get_new_cls_fake_id(self):
        """ Test get method with new class and fake id """
        new = BaseModel()
        self.assertEqual(storage.get('MyModel', 'fake_id'), None)

    def test_count_fake_cls_new_id(self):
        """ Test count method with fake class and new id """
        new = BaseModel()
        self.assertEqual(storage.count('MyModel', new.id), 0)

    def test_get_fake_cls_new_id(self):
        """ Test get method with fake class and new id """
        new = BaseModel()
        self.assertEqual(storage.get('MyModel', new.id), None)

    def test_count_fake_cls_fake_id(self):
        """ Test count method with fake class and fake id """
        new = BaseModel()
        self.assertEqual(storage.count('MyModel', 'fake_id'), 0)
