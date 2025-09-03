from function import *
from productFile import *

def newCode(): #새로운 번호를 리턴 함수
    list = fileRead()
    if len(list) == 0: return 1
    codes = [p.code for p in list]
    return max(codes) + 1

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택:')
    if menu=="0":
        print('프로그램을 종료합니다.')
        break
    elif menu == '1': #입력
        product = Product()
        product.code = newCode()
        print(f'코드>{product.code}')
        if product.code == '': continue
        product.name = input('상품명>')
        if product.name == '': continue
        product.price = inputNum('가격>')
        fileAppend(product)
        product.print()

    elif menu == '2': #검색
        while True:
            value = input('상품명>')
            if value == '': break
            list = fileRead()
            result = [p for p in list if p.name.find(value) !=- 1]
            if len(result) == 0:
                print('검색상품이 없습니다.')
                continue
            for product in result:
                product.print()

    elif menu == '3': #목록
            while True:
                sort=inputNum('1.코드순|2.이름순|3.최저가|4.최고가>')
                if sort=='': break
                list = fileRead()
                result = []
                if sort==1:result = sorted(list, key=lambda p:p.code)
                if sort==2:result = sorted(list, key=lambda p:p.name)
                if sort==3:result = sorted(list, key=lambda p:p.price)
                if sort==4:result = sorted(list, key=lambda p:p.price, reverse=True)
                print()
                for p in result:
                    p.print()
                    
    elif menu == '4': #삭제
        code = inputNum('삭제코드>')
        list = fileRead()
        result = [p for p in list if p.code == code]
        if len(result)==0:
            print("삭자할 코드가 없습니다.")
            continue
        product = result[0]
        product.print()
        sel = input('삭제하시겠습니까?(Y)')
        if sel == 'Y' or sel == 'y':
            result = [p for p in list if p.code != code]
            fileWrite(result)
            print('삭제성공')
        
    elif menu == '5': #수정
        code = inputNum('삭제코드>')
        if code == "": continue
        list = fileRead()
        result = [p for p in list if p.code == code]
        if len(result)==0:
            print("삭제할 상품코드가 없습니다.")
            continue
        product = result[0]
        name = input(f'상품명:{product.name}>')
        if name != '': product.name = name
        price = inputNum(f'가격:{product.price}>')
        if price != '': product.price = price
        sel = input('수정하실겠습니까?(Y)')
        if sel == 'Y' or sel == 'y':
            product.print()
            fileWrite(list)
            print('수정완료')

    else:
        print('0~5 숫자를 입력하세요!')