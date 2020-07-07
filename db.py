import sqlite3
import shutil
import os.path
from datetime import datetime


class Database:
    def __init__(self):
        if not os.path.isfile('main.db'):
            shutil.copy('template.db', 'main.db')

        self.conn = sqlite3.connect('main.db')
        self.cursor = self.conn.cursor()
        print('Connected to SQLite database')

    def get_datetime(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")

    def add_user(self, id, first_name, last_name, role, birth_date):
        self.cursor.execute(
            f'''
            INSERT INTO users (id, first_name, last_name, role, birth_date, reg_date)
            VALUES ({id}, '{first_name}', '{last_name}', '{role}', '{birth_date}', '{self.get_datetime()}')
            '''
        )
        self.conn.commit()

    def add_group(self, name, kvantum, level):
        self.cursor.execute(
            f'''
            INSERT INTO groups (name, kvantum, level, reg_date)
            VALUES ('{name}', '{kvantum}', '{level}', '{self.get_datetime()}')
            '''
        )
        self.conn.commit()

    