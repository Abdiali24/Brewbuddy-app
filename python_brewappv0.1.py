import sys
args = sys.argv


#Define data

GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2
GET_EXIT = 5
ADD_PEOPLE = 3
ADD_DRINKS = 4

APP_NAME = 'Brew Buddy'
Menu = f'''

Welcome to {APP_NAME} Version 0.01
Please select an option below:

[1] Get All People

[2] Get All Drinks

[3] Add Person

[4] Add Drink

[5] Exit
'''

#Define names
people = ['Abdi', 'Bob', 'Tim', 'Sarah', 'Russ'] 
drinks = ['Apple Juice', 'Ginger Ale', 'Coffee', 'Espresso', 'Tea']

#Check arguments - Expect only one command at a time


#define functions for next commands

def tabulate():
    table.print_table()


def get_people():
    tabulate('people', people)

def get_drinks():
    tabulate('drinks', drinks)

def add_element(new_elements, data) :
    new_elements_list = new_elements.split(',')
    for i in range(len(new_elements_list)):
        new_elements_list[i] = new_elements_list[i].strip()
    data += new_elements_list

def wait():
    input('Press ENTER to return to menu')

# def GET_EXIT():
#     input('Press Enter')

def done():
    print(f'Thank You')


# Table output helper funcs

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
    user_selection = int(input('Enter Your Selection: '))

 
    
    if user_selection == GET_PEOPLE_ARG: 
        print_table('People', people)
        wait()
        

    elif user_selection == GET_DRINKS_ARG:
        print_table('Drinks', drinks)
        wait()

    
        
    elif user_selection == ADD_DRINKS:
        user_addition =  input('Enter New Drink: ')
        drinks.append(user_addition)
        print(drinks)
    
    elif user_selection == ADD_PEOPLE:
        user_addition = input(' Enter a new name:\n ')
        people.append(user_addition)
        print(people)

    elif user_selection == GET_EXIT:
        print('Goodbye from Brew Buddy, Please rate us 5 stars on App store!')
        exit()

    else:
        print(f'{user_selection}'' is not a valid command.')
        wait()
   

    
   
# Handle arguments
