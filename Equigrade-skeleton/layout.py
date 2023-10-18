import shutil

def print_divider():
    console_width = shutil.get_terminal_size().columns
    dashed_line = "-" * console_width

    print(dashed_line)

def command_table():
    print_divider()
    print("""Valid commands: \n
        substitute           : customize assignment grading with substitutions\n
        exit                 : exit program""")
    print_divider()

def sub_options():
    print_divider()
    print("""Substitution methods: \n
        average              : take the average of multiple user-selected assignments\n
        waverage             : take the weighted average of multiple user-selected assignments\n
        max                  : use the substitution method that yields the highest grade\n
        direct               : use another assignment score as a direct substitution""")
    print_divider()