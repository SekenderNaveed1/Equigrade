

def get_int(prompt, max_len = 30):
    print(max_len)
    number = input(prompt).strip()
    while True:
        if number.isnumeric() and int(number) <= int(max_len):
            return number
        elif int(number) > int(max_len):
            number = input(f"Please enter an integer less than {int(max_len)+1}: ")
        else:
            number = input("Please enter a valid integer: ")


