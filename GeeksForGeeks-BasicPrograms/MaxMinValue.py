def max_value_in_list(numlist):
    return max(numlist)

def min_value_in_list(numlist):
    return min(numlist)   
    
if __name__ == "__main__":
    a = 100
    b = 700
    c = 250
    max_value = max(a,b,c)
    min_value = min(a,b,c)
    print(f"Maximum of three numbers {a}, {b}, {c} is - {max_value}")
    print(f"Minimum of three numbers {a}, {b}, {c} is - {min_value}")
    number_list=[12,24,31,98,15,18,18,34,43,52,91]
    print(f"Maximum of list is - {max_value_in_list(number_list)}")
    print(f"Minimum of list is - {min_value_in_list(number_list)}")
