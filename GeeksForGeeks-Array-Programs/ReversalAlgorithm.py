## Time complexity: O(n), Auxiliary Space: O(1)

## https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

def reverseAnArray(arrayList, start, end):
    while (start < end):
        temp = arrayList[start]
        arrayList[start] = arrayList[end]
        arrayList[end] = temp
        start += 1
        end -= 1
        

def rotatebyn(arrayList, nr):
    l = len(arrayList)
    reverseAnArray(arrayList, 0,nr-1)
    print(arrayList)
    reverseAnArray(arrayList, nr, l-1)
    print(arrayList)
    reverseAnArray(arrayList,0,l-1)
    print(arrayList)
        

if __name__ == "__main__":
    arrayList = [12,35,31,28,79,98,23,65,72]
    rbyn = 2
    ##print(arrayList[-2])
    rotatebyn(arrayList, rbyn)
    print(f" Elements of Array after rotation by {rbyn} is {arrayList, rbyn}")

