def RemOfArrayMltiplication(arrList, divideby):
    multiplyRem = 1
    remainder = 0
    for i in range(0, len(arrList)):
        arrList[i]= arrList[i] % divideby
        multiplyRem = multiplyRem * arrList[i]
    print(f"Multiplication of Remainder - {multiplyRem}")
    
    if (multiplyRem > divideby):
        remainder = multiplyRem % divideby
    
    return remainder

if __name__ == "__main__":
    ##arrayList = [12,35,31,28,79,98,23,65,72]
    arrayList = [100, 10, 5, 25, 35, 14]
    divideby = 11
    result = RemOfArrayMltiplication(arrayList, divideby)
    print(f" Remainder of array multiplication divided by {divideby} is {result}")


