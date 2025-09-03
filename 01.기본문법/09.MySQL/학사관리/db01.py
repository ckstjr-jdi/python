import pymysql

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
        self.dept_code = 0
        self.dept_name = ''

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.code = 0
    def print(self):
        print(f'학번:{self.id}, 이름:{self.name}, 학과:{self.dept_name}({self.code})')
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

def search(value):
    try:
        sql = 'select * from vstudent where id like %s or name like %s or dept_name like %s'
        value = f'%{value}%'
        cur.execute(sql, (value, value, value))
        rows = cur.fetchall()
        if not rows == None:
            search_list = []
            for row in rows:
                stu = Student()
                stu.id = row['id']
                stu.name = row['name']
                stu.code = row['code']
                stu.dept_name = row['dept_name']
                search_list.append(stu)
            return search_list
    except Exception as err:
        print('학생검색오류', err)    

def newID():
    try:
        sql = 'select convert(max(id)+1, char(4)) as new_id from studnet'
    except Exception as err: