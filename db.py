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
            INSERT INTO users (uid, first_name, last_name, role, birth_date, reg_date)
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
            WHERE uid = {user.uid}
            '''
        )
        self.conn.commit()

    def get_user(self, uid):
        user_info = self.cursor.execute(
            f'''
            SELECT uid, first_name, last_name, role, birth_date FROM users WHERE uid="{uid}"
            '''
        ).fetchall()
        return User(user_info[0][0], user_info[0][1], user_info[0][2], user_info[0][3], user_info[0][4])

    def add_group(self, group):
        self.cursor.execute(
            f'''
            INSERT INTO groups (uid, name, kvantum, level, teacher_uid, reg_date)
            VALUES ({group.uid}, '{group.name}', '{group.kvantum}', {group.level}, {group.teacher_uid}, '{self.get_datetime()}')
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
                teacher_uid = {group.teacher_uid}
            WHERE uid = {group.uid}
            '''
        )
        self.conn.commit()

    def get_group(self, name):
        group_info = self.cursor.execute(
            f'''
            SELECT uid, name, kvantum, level, teacher_uid FROM groups WHERE name="{name}"
            '''
        ).fetchall()
        return Group(group_info[0][1], group_info[0][2], group_info[0][3], group_info[0][4])

    def add_u2g(self, user_uid, group_uid):
        self.cursor.execute(
            f'''
            INSERT INTO relationships (user_uid, group_uid, join_date)
            VALUES ({user_uid}, {group_uid}, '{self.get_datetime()}')
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
    def __init__(self, name, kvantum, level, teacher_uid):
        self.uid = -1
        self.name = name
        self.kvantum = kvantum
        self.level = level
        self.teacher_uid = teacher_uid
