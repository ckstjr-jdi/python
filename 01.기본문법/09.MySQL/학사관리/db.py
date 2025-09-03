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
        sql = 'select convert(max(id)+1, char(4)) as new_id from student'
        cur.execute(sql)
        row = cur.fetchone()
        return row['new_id']
    except Exception as err:
        print('새로운학번:', err)

def listDept():
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        dept_list = []
        for row in rows:
            dept = Dept()
            dept.dept_code = row['dept_code']
            dept.dept_name = row['dept_name']
            dept_list.append(dept)
        return dept_list
        
    except Exception as err:
        print('학과목록오류:', err)

#학과코드입력함수
def inputCode(title, menu):
    list = listDept()
    codes = [dept.dept_code for dept in list]
    print('-' * 50)
    for dept in list:
        print(f'{dept.dept_code}.{dept.dept_name}', end="|")
    print()
    print('-'*50)
    while True:
        code = input(title)
        if code == '' and menu==1:
            print('학과코드 꼭 입력하세요!')
        elif code == '' and menu == 5:
            return code
        elif not code.isnumeric():
            print('학과코드는 숫자로 입력하세요!')
        elif codes.count(int(code))==0:
            print(f'{codes} 코드번호를 입력하세요!')
        else:
            return int(code)

def insert(stu):
    try:
        sql = 'insert into student(id, name, code) values(%s, %s, %s)'
        cur.execute(sql, (stu.id, stu.name, stu.code))
        con.commit()
        print('학생등록완료')        
    except Exception as err:
        print('학생등록오류:', err)

def read(id):
    try:
        sql = 'select * from vstudent where id=%s'
        cur.execute(sql, (id))
        row = cur.fetchone()
        if row != None:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.code = row['code']
            stu.dept_name = row['dept_name']
            return stu
    except Exception as err:
        print('학생읽기오류:', err)

def delete(id):
    try:
        sql = 'delete from student where id=%s'
        cur.execute(sql, (id))
        con.commit()
        print('학생삭제완료')
    except Exception as err:
        print('학생삭제오류', err)

def update(stu):
    try:
        sql = 'update student set name=%s, code=%s where id=%s'
        cur.execute(sql, (stu.name, stu.code, stu.id))
        con.commit()
        print('학생수정완료')
    except Exception as err:
        print('학생수정오류:', err)

#학과등록
def insertDept(dept_name):
    sql = 'insert into dept(dept_name) values(%s)'
    cur.execute(sql, (dept_name))
    con.commit()
    print('학과등록완료!')

#코드로 학과찾기
def readDept(dept_code):
    sql = 'select * from dept where dept_code=%s'
    cur.execute(sql, (dept_code))
    row = cur.fetchone()
    dept = Dept()
    dept.dept_code = row['dept_code']
    dept.dept_name = row['dept_name']
    return dept

#학과수정
def updateDept(dept):
    sql = 'update dept set dept_name=%s where dept_code=%s'
    cur.execute(sql, (dept.dept_name, dept.dept_code))
    con.commit()
    print('학과수정완료!')






# if __name__=='__main__':