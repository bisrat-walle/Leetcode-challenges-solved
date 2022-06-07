T = int(input())
testcases = []
for i in range(T):
    n = int(input())
    red = [int(i) for i in input()]
    blue = [int(i) for i in input()]
    testcases.append((red, blue))

for red, blue in testcases:
    red_ = 0
    k = 0
    while k < len(red):
        if red[k] > blue[k]:
            red_ += 1
        elif red[k] < blue[k]:
            red_ -= 1
        k += 1
    if red_ == 0:
        print("EQUAL")
    elif red_ > 0:
        print("RED")
    else:
        print("BLUE")
    