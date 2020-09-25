import sys
args = sys.argv
#Define data
GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2
GET_EXIT = 3

APP_NAME = 'Brew Buddy'
Menu = f'''

Welcome to {APP_NAME} Version 0.01
Please select an option below:

[1] Get All People

[2] Get All Drinks

[3] Exit
'''

#Define names
people = ['Abdi', 'Bob', 'Tim', 'Sarah', 'Russ'] 
drinks = ['Apple Juice', 'Ginger Ale', 'Coffee', 'Espresso', 'Tea']

#Check arguments - Expect only one command at a time

if len(args) < 2:
    print('error detected, enter valid command')
    exit()

if len(args) > 2:
    print('I only have 2 hands, which one is it?')
    exit()

# Table outut helper funcs

def print_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print(f'| {item}')
    print_separator(width)

def print_header(title, width):
    print_separator(width)
    print(f'| {title}')
    print_separator(width)

def print_separator(width):
    print(f"+{'=' * width}")

def get_table_width(title, data):
    longest = len(title)
    additional_spacing = 2
    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + additional_spacing

while True:
    print(Menu)
    user_selection = int(input('Enter Your Selection'))
    
    
# Handle arguments
