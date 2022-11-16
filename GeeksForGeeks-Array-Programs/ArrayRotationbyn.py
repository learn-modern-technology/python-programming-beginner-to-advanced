## https://www.geeksforgeeks.org/python-program-for-program-for-array-rotation-2/

def rotatebydegree(arrList, degree):
    tempList= arrList
    arrList = []
    sizeOfList=len(tempList)
    for x in range(degree, sizeOfList):
        arrList.append(tempList[x])
    
    for x in range(0, degree):
        arrList.append(tempList[x])

    ##arrList = tempList
    return arrList
    
if __name__ == "__main__":
    arrayList = [12,35,31,28,79,98,23,65,72]
    rbyn = 2
    print(arrayList[-2])
    print(f" Array before rotation is {arrayList}")
    newarrayList = rotatebydegree(arrayList, rbyn)
    print(f" Array after rotation by {rbyn} is {newarrayList}")