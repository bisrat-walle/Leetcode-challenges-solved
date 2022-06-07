n = int(input())
input_ = [int(i) for i in input().split()]

zero = 0
pos = 0
neg = 0
cost = 0

for i in input_:
    if i < 0:
        cost += -1*i - 1
        neg += 1
    elif i == 0:
        zero += 1
    else:
        pos += 1
        cost += i-1

if neg % 2 == 0:
    cost += zero
else:
    if zero > 0:
        cost += zero
    else:
        cost += 2
print(cost)

