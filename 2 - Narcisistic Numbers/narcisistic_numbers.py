def narcissistic(val):
    numSize = len(str(val))
    leftover = val
    current = 0
    sum = 0
    for i in range(0,numSize):
        current = leftover % 10
        leftover = leftover // 10
        sum += current ** numSize
    return sum == val