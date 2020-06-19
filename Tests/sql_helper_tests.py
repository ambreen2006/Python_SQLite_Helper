import unittest
import os.path as path
import SQLiteHelper as DB


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.db_name = 'TestDatabase.db'
        self.db_helper = DB.SQLiteHelper(self.db_name)

    def test_connection(self):
        db_exists = path.exists(self.db_name)
        print(f'Database exists: {db_exists}')
        self.assertEqual(db_exists, True)

    def table_create(self):
        fields_info = {
            'model': 'TEXT',
            'type': 'INTEGER',
            'epoch': 'INTEGER',
            'iou': 'REAL',
            'val_iou': 'REAL',
            'loss': 'REAL',
            'val_loss': 'REAL'
        }
        result, _ = self.db_helper.create('Measurements', fields_info)
        return result

    def test_create_table(self):
        self.assertTrue(self.table_create())

    def table_insert(self):
        records = {
            'model': 'unet',
            'type': 1,
            'epoch': 1,
            'iou': 1,
            'val_iou': 1,
            'loss': 1,
            'val_loss': 1
        }
        result, _ = self.db_helper.insert('Measurements', records)
        return result

    def test_insert_table(self):
        self.assertTrue(self.table_insert())

    def test_fetch_table(self):
        selection = 'MODEL, DATE(date_time) as dt, val_loss'
        conditions = 'model = "unet" and dt = "2020-06-18"'
        self.table_create()
        self.table_insert()
        result, cursor = self.db_helper.fetch('Measurements', selection, conditions)
        self.assertTrue(result)
        results = cursor.fetchall()
        for row in results:
            print(row)


if __name__ == '__main__':
    unittest.main()
