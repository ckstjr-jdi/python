java = {'유재석', '홍길동', '심청이'}
print(1, java, type(java))

python = {'심청이', '강호동', '이순신'}
print(2, python, type(python))

print(3, java.intersection(python)) #교집합
print(4, java.union(python)) #합집합
print(5, java.difference(python)) #차집합