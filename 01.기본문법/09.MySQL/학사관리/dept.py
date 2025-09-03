import os
from db import *

def menuDept():
    os.system('cls')
    while True:
        print()
        print('**********학과관리**********')
        print('----------------------------')
        print('1.등록|2.목록|3.수정|0.종료|')
        print('----------------------------')
        menu = input('메뉴선택>')
        if menu == '0':
            break

        elif menu == '3':
            dept_code = inputCode('학과코드>',5)
            dept = readDept(dept_code)
            dept_name = input(f'학과이름:{dept.dept_name}>')
            if dept_name != '':dept.dept_name = dept_name
            updateDept(dept)
            
        elif menu == '1':
            dept_name = input('학과이름>')
            if dept_name=="":continue
            insertDept(dept_name)

        elif menu == '2':
            list = listDept()
            for dept in list:
                print(f'학과코드:{dept.dept_code}, 학과이름:{dept.dept_name}')