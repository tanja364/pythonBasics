def inputGrades(x):
    grades = []
    for i in range(0, x, 1):
        prompt = float(input('Please Enter Your Grades: '))
        grades.append(prompt)
    return grades
def printGrades(x, y):
    for i in range(0, x, 1):
        print(y[i])
    return y
def avGrades(x,y):
    bucket = 0
    for i in range(0, x, 1):
        bucket = bucket + y[i]
    return bucket
def lowHigh(x):
    lowVal = 100
    highVal = 0
    for i in x:
        if i < lowVal:
            lowVal = i
        if i > highVal:
            highVal = i
    return lowVal, highVal
def bubble(x, y):
    swapper = 0
    for i in range(0, x-1, 1):
        for i in range(0, x-1, 1):
            if y[i] < y[i+1]:
                swapper = y[i]
                y[i] = y[i+1]
                y[i+1] = swapper
    return y


numGrades = 2
iG = inputGrades(numGrades)
pG = printGrades(numGrades, iG)
aG = avGrades(numGrades, iG)
low, high = lowHigh(iG)
average = aG / numGrades
bub = bubble(numGrades, iG)
print('Your Sum Is: ', aG)
print('Your Average Is: ', average)
print('Your Highest Grade Is: ', high)
print('Your Lowest Grade Is: ', low)
print('Here Is Your Sorted List: ', bub)