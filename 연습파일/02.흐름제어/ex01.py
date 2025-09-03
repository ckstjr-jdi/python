num1 = input('숫자1>')
num2 = input('숫자2>')
num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(f'{num1}이(가) {num2}보다 큽니다.')
elif num1 == num2:
    print(f'{num1}이(가) {num2}와(과) 같습니다.')
else:
    print(f'{num1}이(가) {num2}보다 작습니다.')