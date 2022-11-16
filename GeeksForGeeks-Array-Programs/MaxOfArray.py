## Time complexity: O(n), Auxiliary Space: O(1)

def maximum_of_array(arrayList):
    return max(arrayList)

def minimum_of_array(arrayList):
    return min(arrayList)

if __name__ == "__main__":
    arList = [12,35,31,28,79,98,23,65,72]
    print(f"Maximum of all Elements of Array is {maximum_of_array(arList)}")
    print(f"Minimum of all Elements of Array is {minimum_of_array(arList)}")
    