import math

def sumofCubesUsingFormula(n):
    
    sum = 0
    ##for i in range(1, n+1):
    sum = int(sum + pow(((n/2) * (n+1)),2))
    return sum

def sumofCubes(n):
    i = 1
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i ** 3)
        i = i + 1
    return sum

if __name__ == "__main__":
    num = 5
    print(f"Sum of cubes of all numbers upto {num}th numbers are - {sumofCubesUsingFormula(num)}")
    print(f"Sum of cubes of all numbers upto {num}th numbers are - {sumofCubes(num)}")
