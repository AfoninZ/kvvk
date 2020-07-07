from db import Database, User
import random
import string

db = Database()
u1 = User(123, 'Барак', 'Обама', 'student', '04/08/1961')
g1 = Group()
db.add_user(u1)
u1.first_name = 'Ёбаный'
db.update_user(u1)