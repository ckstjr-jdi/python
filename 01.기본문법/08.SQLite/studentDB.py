import os
import sqlite3
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

class Student:
    def __init__(self):
        self.code = 0
        self.name = ''
        self.birthday = ''

    def print(self):
        print(f'학번:{self.code}, 이름:{self.name}, 가격:{self.birthday}')

def list(type): #type = 1:학번순, 2.이름순
    con = sqlite3.connect(db_name)
    cursor=con.cursor()
    sql = 'select * from student '
    if type == 1:
        sql += 'orede by code'
    elif