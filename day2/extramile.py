'''
Try reversing the name app above
Accept a name from a user
Print First and Last name separately

'''

name = input("Enter your full name: ")
first_name,last_name  = name.split(" ")

print(f'First name: {first_name.upper()} Last name: {last_name.upper()}')

'''
$ python extramile.py
Enter your full name: fazil sha
First name: FAZIL Last name: SHA


'''
