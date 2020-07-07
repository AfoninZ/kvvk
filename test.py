from db import Database
import random
import string

db = Database()
db.add_user(1, 'Барак', 'Обама', 'student', '04/08/1961')
db.add_group('Враги России', 'IT', 2)
db.add_u2g(1, 1)