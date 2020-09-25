import sys
args = sys.args
#Define data
GET_PEOPLE_ARG = 'get-people'
GERT_DRINKS_ARG = 'get-drinks'
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
# Handle arguments
command = args[1]
if command == GET_PEOPLE_ARG:
    print_table('People', people)
elif command == GET_DRINKS_ARG:
    print_table('Drinks With A Really Long Title', drinks)
else:
    print(f'"{command}" is not an command that I recognise.')