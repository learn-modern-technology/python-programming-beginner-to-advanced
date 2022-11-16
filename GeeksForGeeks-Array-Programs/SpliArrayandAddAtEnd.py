## https://www.geeksforgeeks.org/python-program-for-split-the-array-and-add-the-first-part-to-the-end/

# Python program to split array and move first
# part to end.

def splitArrayandAddAttheEnd(arrayList, sizeOfArray, degree):
    for i in range(0,degree):
        x = arrayList[0]
        for j in range(0, sizeOfArray-1):
            arrayList[j] = arrayList[j+1]
        arrayList[sizeOfArray-1] = x

if __name__ == "__main__":
    arrayList = [12,35,31,28,79,98,23,65,72,100]
    degree = 4
    print(f" Array before rotation is {arrayList}")
    splitArrayandAddAttheEnd(arrayList, len(arrayList),degree)
    print(f" Array after rotation by {degree} is {arrayList}")