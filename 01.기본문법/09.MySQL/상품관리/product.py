from db import *
from classes import *
from function import *

def list():
    try:
        sql = 'select * from product'
        cur.execute(sql)
        rows = cur.fetchall()
        products = []
        for row in rows:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.cost_price = row['cost_price']
            products.append(product)
        return products
    except Exception as err:
        print('상품목록오류:', err)

def insert(product):
    try:
        sql = 'insert into product(code, name, cost_price) values(%s, %s, %s)'
        cur.execute(sql, (product.code, product.name, product.cost_price))
        con.commit()
        print('상품등록완료!')
    except Exception as err:
        print('상품입력오류:', err)
  
def search(value):
    try:
        sql = 'select * from product where code like %s or name like %s'
        value = f'%{value}%'
        cur.execute(sql, (value,value))
        rows = cur.fetchall()
        if rows != None:
            search_products = []
            for row in rows:
                product = Product()
                product.code = row['code']
                product.name = row['name']
                product.cost_price = row['cost_price']
                search_products.append(product)
            return search_products  
    except Exception as err:
        print('상품검색오류:', err)

def read(code):
    try:
        sql = 'select * from product where code=%s'
        cur.execute(sql, (code))
        row = cur.fetchone()
        if row != None:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.cost_price = row['cost_price']
            return product
    except Exception as err:
        print('상품읽기오류:', err)

def inputCode(title):
    while True:
        code = input(title)
        if code=='': return code
        if len(code) != 3 or not code.isnumeric():
            print('상품코드는 3자리 숫자로 입력하세요!')
        else:
            return code
            
def inputCost_price(title):
    while True:
        cost_price = input(title)
        if cost_price == '':
            return ''
        elif not cost_price.isnumeric():
            print('가격은 숫자로 입력하세요')
        else:
            return int(cost_price)
        
def update(product):
    try:
        sql = 'update product set name=%s, cost_price=%s where code=%s'
        cur.execute(sql, (product.name, product.cost_price, product.code))
        con.commit
    except Exception as err:
        print('상품수정오류:', err)

if __name__=='__main__':
    price = inputCost_price('상품가격>')
    print('가격:', price)