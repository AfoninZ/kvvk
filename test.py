from db import Database, User, Group
import random
import string

db = Database()
u1 = User(123, 'Барак', 'Обама', 'student', '04/08/1961')
g1 = Group('И17.1', 'IT', 1, u1.uid)
db.add_user(u1)
db.add_group(g1)
u2 = db.get_user(db.get_group('И17.1').teacher_uid)
print(u2.first_name)