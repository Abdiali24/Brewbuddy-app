



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

def print_table(title, data):
    width = get_table_width(title, data)
    print_header(title, width)
    for item in data:
        print(f'| {item}')
    print_separator(width)