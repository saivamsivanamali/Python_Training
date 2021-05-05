'''Accept a list of numbers from user and

print a sum of those values
print minimum value
print only unique values from those
print the list of numbers in ascending order
print the list of numbers in descending order'''

num_list = input("Enter the number list: ") # Getting input from user e.g: 12 13 14 15 16 
new_list = [int(num) for num in num_list.split(" ")] # Actually we are getting the input as string. Using split method and int to standardize it 

#Minimum value
print(f'Minimum number in a list: {min(new_list)}')

#Unique values in list
print(f'Unique value of list : {list(set(new_list))}')

#ascending order
new_list.sort()
print(f'Ascending order: {new_list}')
#descending order
new_list.sort(reverse = True)
print(f'Descending order: {new_list}')

'''

$ python exercise1.py
Enter the number list: 36 26 1 26 1 62 36 8 8
Minimum number in a list: 1
Unique value of list : [1, 36, 8, 26, 62]
Ascending order: [1, 1, 8, 8, 26, 26, 36, 36, 62]
Descending order: [62, 36, 36, 26, 26, 8, 8, 1, 1]

'''
