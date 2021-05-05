'''
Write a name creator app

Ask user's first name
Ask user's last name
Print like Firstname Lastname (capialized first and last names)

'''

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")

print(f'{first_name.capitalize()} {last_name.capitalize()}')

'''
$ python exercise2.py
Enter your first name : fazil
Enter your last name : sha
Fazil Sha

'''
