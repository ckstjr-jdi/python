names = ['홍길동', '심청이', '강감찬']

print(1, names[2])

names.append('성춘향')
print(2, names)
names.insert(1, '유재석')
print(3, names)

print(6, len(names))
print(7, names.count('심청이'))
print(8, type(names))