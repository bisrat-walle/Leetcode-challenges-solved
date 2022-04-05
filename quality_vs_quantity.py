no_of_testcase = int(input())
testcases = []
for i in range(no_of_testcase):
    n = int(input())
    input_ = [int(i) for i in input().split()]
    testcases.append(input_)
    

for testcase in testcases:
    testcase.sort()
    red_sum = testcase[-1]
    blue_sum = testcase[0] + testcase[1]
    if red_sum > blue_sum:
        print("YES")
        continue
    i, j, possible = 2, len(testcase)-2, False
    while i < j:
        red_sum += testcase[j]
        blue_sum += testcase[i]
        if red_sum > blue_sum:
            possible = True
            break
        i += 1
        j -= 1
    if possible:
        print("YES")
    else:
        print("NO")
        