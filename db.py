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

    def add_user(self, user):
        self.cursor.execute(
            f'''
            INSERT INTO users (id, first_name, last_name, role, birth_date, reg_date)
            VALUES ({user.uid}, '{user.first_name}', '{user.last_name}', '{user.role}', '{user.birth_date}', '{self.get_datetime()}')
            '''
        )
        self.conn.commit()

    def update_user(self, user):
        self.cursor.execute(
            f'''
            UPDATE users
            SET first_name = '{user.first_name}',
                last_name = '{user.last_name}',
                role = '{user.role}',
                birth_date = '{user.birth_date}'
            WHERE id = {user.uid}
            '''
        )
        self.conn.commit()

    def add_group(self, group):
        self.cursor.execute(
            f'''
            INSERT INTO groups (id, name, kvantum, level, teacher_id, reg_date)
            VALUES ({group.uid}, '{group.name}', '{group.kvantum}', {group.level}, {group.teacher_id}, '{self.get_datetime()}')
            '''
        )
        self.conn.commit()

    def update_group(self, group):
        self.cursor.execute(
            f'''
            UPDATE users
            SET name = '{group.name}',
                kvantum = '{group.kvantum}',
                level = {group.level},
                teacher_id = {group.teacher_id}
            WHERE id = {group.uid}
            '''
        )
        self.conn.commit()

    def add_u2g(self, user_id, group_id):
        self.cursor.execute(
            f'''
            INSERT INTO relationships (user_id, group_id, join_date)
            VALUES ({user_id}, {group_id}, '{self.get_datetime()}')
            '''
        )
        self.conn.commit()


class User:
    def __init__(self, uid, first_name, last_name, role, birth_date):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.birth_date = birth_date


class Group:
    def __init__(self, name, kvantum, level, teacher_id):
        self.uid = -1
        self.name = name
        self.kvantum = kvantum
        self.level = level
        self.teacher_id = level