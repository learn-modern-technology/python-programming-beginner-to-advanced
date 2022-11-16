def isMonotonicArray(arrayList):
    return (all(arrayList[i] <= arrayList[i+1] for i in range(0, len(arrayList)-1)) or
            all (arrayList[i] >= arrayList[i+1] for i in range(0, len(arrayList)-1)))

def isMonotonicUsingExtend(arrayList):
    a, b = [], []
    
    a.extend(arrayList)
    b.extend(arrayList)
    a.sort()
    b.sort(reverse=True)
    if (arrayList == a  or arrayList == b):
        return True
    return False

if __name__ == "__main__":
    ##arrayList = [100, 10, 5, 25, 35, 14]
    ##arrayList = [6, 5, 4, 4]
    arrayList = [100, 35, 25, 14, 10, 5]
    print(f"Array is {arrayList}")
    print(f" Array is Monotonic ? - {isMonotonicArray(arrayList)}")
    print(f"Array is {arrayList}")
    print(f" Array is Monotonic ? - {isMonotonicUsingExtend(arrayList)}")
    print(f"Array is {arrayList}")