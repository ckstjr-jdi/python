import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/joojoo.db'

class Person:
    def __init__(self):
        self.seq = 0
        self.name = '홍길동'
        self.address = '경기도 광명시'

    def print(self):
        print(f'번호:{self.seq}, 이름:{self.name}, 주소:{self.address}')

#목록
def list():
    con = sqlite3.connet(db_name)
    cursor = con.cursor()
    sql = 'select seq, name, address from joojoo'
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

#검색
def search(value):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from joojoo where name like ? or address like ?"
    value = f'%{value}%'
    cursor.execute(sql, (value, value,))
    rows = cursor.fetchall()
    cursor.close()
    con.close()

#읽기
def read(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = 'select * from joojoo where seq=?'
    cursor.execute(sql, (seq,))
    row = cursor.fetchone()
    cursor.close()
    con.close()
    return row

#삭제
def delete(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "delete from joojoo where seq=?"
    cursor.execute(sql, (seq,))
    con.commit()
    cursor.close()
    con.close()

#입력
def insert(person):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "insert into joojoo(name, address) values(?,?)"
    cursor.execute(sql, (person.name, person.address, ))
    con.commit()
    cursor.close()
    con.close()

#수정
def update(person):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "update joojoo set name=?, address=? where seq=?"
    cursor.execute(sql, (person.name, person.address, person.seq,))
    con.commit()
    cursor.close()
    con.close()  