def toFindMax(a,b,c):
    c.sort()
    maxNum = c[-int(b):]
    result = []
    for i in maxNum:
        for g in c:
            if i==g:
                result.append(g)
    sumof = 0
    for i in result:
        sumof += i
    return sumof
    


a,b = input().split()
numberOfArrays = input().split()
listOfint = []
for i in numberOfArrays:
    listOfint.append(int(i))
output = toFindMax(a,b,listOfint)
print(output)