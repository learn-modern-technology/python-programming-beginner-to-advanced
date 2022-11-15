def sum_of_square_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i * i)
    return sum

def sum_of_square_of_numbers_using_formula(n):
    sum = (n *(n+1)*(2*n+1))//6
    return sum

if __name__ == "__main__":
    number = 32
    print(f"Sum of squares of first {number} natural numbers is {sum_of_square_of_numbers(number)}")
    print(f"Sum of squares of first {number} natural numbers is {sum_of_square_of_numbers_using_formula(number)}")