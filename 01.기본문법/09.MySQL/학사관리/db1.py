import pymysql
from function import *


con = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='haksa',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

cur = con.cursor()

class Dept:
    def __init__(self):
        self.dept.code = 0
        self.dept.name = ''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.code = 0
    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dept.name}({self.code})')
        print('-' * 50)

def list(key):
    try:
        keys=['id','name','dept_name']
        sql = f'select * from vstudent order by {keys[key-1]}'
        cur.execute(sql)
        rows = cur.fetchall()
        student_list = []
        for row in rows:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.dept_name = row['dept_name']
            stu.code = row['code']
            student_list.append(stu)
        return student_list
    except Exception as err:
        print('학생목록오류', err)

def newID():
    try:
        sql = 'select convert(max(id)+1, char(4)) as new_id from student'
        cur.execute(sql)
        row = cur.fetchone()
        return row['new_id']
    except Exception as err:
        print('새로운학번:', err)

def insert(stu):
    try:
        sql = 'insert into student(id, name, dept_code) values(%s, %s, %s)'
        cur.execute(sql, (stu.id, stu.name, stu.code))
        con.commit
        print('학생등록완료!')
    except Exception as err:
        print('학생등록오류:', err)

if __name__=='__main__':
    stu = Student()
    stu.id = newID()
    stu.name = input('학생이름>')
    stu.code = int(input('학과코드>'))
    insert(stu)
                
