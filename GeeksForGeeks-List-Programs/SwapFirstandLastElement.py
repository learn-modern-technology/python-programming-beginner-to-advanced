def swap_first_and_last_element(list1):
    temp = list1[0]
    list1[0] = list1[len(list1)-1]
    list1[len(list1)-1] = temp
    
if __name__ == "__main__":
    myList= [100, 10, 5, 25, 35, 14]
    print(f"myList - {myList}")
    swap_first_and_last_element(myList)
    print(f"myList - {myList}")
