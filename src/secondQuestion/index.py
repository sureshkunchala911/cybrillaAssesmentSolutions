listOfArray = [-1, 0, 1, 2, -1, 4]
lengthofarray = len(listOfArray)
for i in range(lengthofarray-2):
    first = listOfArray[i]
    for h in range(i,lengthofarray-2):
        second = listOfArray[h]
        third = listOfArray[h+1]
        if first+second+third==0:
            print(first,second,third)
    