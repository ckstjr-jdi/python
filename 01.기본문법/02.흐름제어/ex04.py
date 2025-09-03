#1~100 합계
sum = 0
for i in range(1, 101):
    sum += i #sum=sum+1 (i를 누적해서 sum)
print(sum)

#2~100 짝수합계
tot = 0
for i in range(2, 101, 2):
    tot += i
print(tot)

#1~99 홀수합계
t = 0
for j in range(1, 100, 2):
    t += j
print(t)