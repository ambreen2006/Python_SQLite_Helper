import sqlite3
from datetime import datetime


class SQLiteHelper:

    def __init__(self, db_path):
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_path)
            print("Connected to SQLite DB")
        except sqlite3.Error as e:
            print(f"Error {e}")

    @staticmethod
    def get_datetime_key():
        return 'date_time'

    def execute(self, query, values=None):
        cursor = self.connection.cursor()
        try:
            if not values:
                cursor.execute(query)
            else:
                cursor.execute(query, values)
            self.connection.commit()
            return True, cursor
        except sqlite3.Error as e:
            print(f'Error executing query: {e}')
            return False, cursor

    def create(self, table_name, table_structure):
        create_table_query = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ('
        sep = ''
        for field in table_structure:
            create_table_query += sep + field + ' ' + table_structure[field]
            sep = ', '
        create_table_query += sep + self.get_datetime_key() + ' TEXT'
        create_table_query += ');'
        return self.execute(create_table_query)

    def update(self, table_name, data):
        pass

    def insert(self, table_name, data):
        field_list = data.keys()
        insert_table_query = f'INSERT INTO ' + table_name + ' (' + (','.join(field_list)) + ',' \
                             + self.get_datetime_key() + ') VALUES (' \
                             + ','.join(['?'] * len(data)) + ',?);'

        record = tuple(data[field] for field in field_list) + (datetime.now().isoformat(),)
        return self.execute(insert_table_query, record)

    def fetch(self, table_name, selections, condition):
        fetch_table_query = 'SELECT ' + selections + ' FROM ' + table_name + ' WHERE ' + condition + ';'
        return self.execute(fetch_table_query)

    def delete(self, table_name, delete):
        pass
