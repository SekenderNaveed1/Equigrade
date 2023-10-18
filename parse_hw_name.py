import re

def split_name_num(input_string):
    parts = re.findall(r'([A-Za-z]+)|(\d+)', input_string)

    name = ""
    nums = ""
    
    for part in parts:
        if part[0]:  # Check if it's a letter (non-empty)
            name += part[0] + " "
        if part[1]:  # Check if it's a number (non-empty)
            nums += part[1]
    
    return name, nums

