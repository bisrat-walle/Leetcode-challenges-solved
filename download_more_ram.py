t = int(input())
testcases = []
for i in range(t):
    n, k = [int(i) for i in input().split()]
    temp = {}
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    for i in a:
        temp[i] = 0
    for i, j in zip(a, b):
        temp[i] += j
    testcases.append([k, temp])

for i in testcases:
    i[1] = dict(sorted(i[1].items(), key=lambda k:k[0]))

for i in testcases:
    k, d = i
    current_ram = k
    printed = False
    for j in d:
        if j > current_ram:
            print(current_ram)
            printed = True
            break
        current_ram += d[j]
    if not printed:
        print(current_ram)
