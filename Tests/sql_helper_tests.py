import unittest
import os.path as path

from SQLiteHelper import SQLiteHelper as DB


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.db_name = 'TestDatabase.db'
        self.db_helper = DB.SQLiteHelper(self.db_name)

    def test_connection(self):
        db_exists = path.exists(self.db_name)
        print(f'Database exists: {db_exists}')
        self.assertEqual(db_exists, True)

    def test_create_table(self):
        fields_info = {
            'model': 'TEXT',
            'type': 'INTEGER',
            'epoch': 'INTEGER',
            'iou': 'REAL',
            'val_iou': 'REAL',
            'loss': 'REAL',
            'val_loss': 'REAL'
        }
        result = self.db_helper.create('Measurements', fields_info)
        self.assertTrue(result)

    def test_insert_table(self):
        records = {
            'model': 'unet',
            'type': 1,
            'epoch': 1,
            'iou': 1,
            'val_iou': 1,
            'loss': 1,
            'val_loss': 1
        }
        result = self.db_helper.insert('Measurements', records)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
