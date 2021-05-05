'''
Accept 2 lists of numbers from user and

print numbers present in both the lists
print numbers in one list and not another and vice versa

'''

list_1 = input("Enter the first list: ") # Getting input from user e.g: 12 13 14 15 16
list_2 = input("Enter the second list: ")
new_list1 = set([int(num) for num in list_1.split(" ")])
new_list2 = set([int(num) for num in list_2.split(" ")])

print(f'Intersection of List: {new_list1 & new_list2}')

print(f"Differ from List2: {new_list1 - new_list2}")
print(f"Differ from List 1: {new_list2 - new_list1}")

'''
$ python exercise3.py
Enter the first list: 1 2 3 4 5 6
Enter the second list: 4 5 6 7 8 9
Intersection of List: {4, 5, 6}
Differ from List2: {1, 2, 3}
Differ from List 1: {8, 9, 7}

'''
