# Asrar Abdelgaber OSman Marae - 20230783
# Lina Mahmoud Ahmed Omer      - 20230780
# Osama Mohammed Bay           - 20230740



#A Function to convert from binary to decimal
def bin_to_dec(binary):
    decimal = 0
    binary = binary[::-1]
    # Reverse the binary string for easier processing
    for i in range(len(binary)):
        bit = int(binary[i])
        decimal += bit * (2 ** i)
    return decimal


# Function to convert from decimal to binary
def dec_to_bin(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary or "0"


# Function to convert from binary to octal
def bin_to_oct(binary):
    decimal = bin_to_dec(binary)
    octal = dec_to_oct(decimal)
    return octal


# Function to convert from decimal to octal
def dec_to_oct(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    return octal or "0"


# Function to convert from octal to decimal
def oct_to_dec(octal):
    decimal = 0
    octal = octal[::-1]  
    # Reverse the octal string for easier processing
    for i in range(len(octal)):
        digit = int(octal[i])
        decimal += digit * (8 ** i)
    return decimal


# Function to convert from decimal to hexadecimal
def dec_to_hex(decimal):
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal //= 16
    return hexadecimal or "0"


# Function to convert from hexadecimal to decimal
def hex_to_dec(hexadecimal):
    decimal = 0
    hex_digits = "0123456789ABCDEF"
    hexadecimal = hexadecimal[::-1].upper()  
    # Reverse the hexadecimal string for easier processing
    for i in range(len(hexadecimal)):
        digit = hex_digits.index(hexadecimal[i])
        decimal += digit * (16 ** i)
    return decimal


# Function to convert from binary to hexadecimal
def bin_to_hex(binary):
    decimal = bin_to_dec(binary)
    hexadecimal = dec_to_hex(decimal)
    return hexadecimal


#Functions to check the validity of numbering systems 
def is_valid_binary(binary_num):
    for digit in binary_num:
        if digit not in '01':
            return False
    return True


def is_valid_octal(number_str):
    for digit in number_str:
        if digit not in '01234567':
            return False
    return True


def is_valid_decimal(number_str):
    decimal_check = False  
    # Flag to check if a decimal point is encountered
    for char in number_str:
        if char.isdigit():
            continue
        elif char == '.' and not decimal_check:
            decimal_check = True
        else:
            return False
    return True


def is_valid_hexadecimal(number_str):
    hex_digits = set('0123456789ABCDEFabcdef')
    for digit in number_str:
        if digit not in hex_digits:
            return False
    return True


def menu_1():
    while True:
        print("\nNumbering System Converter")
        print("A) Insert a new number")
        print("B) Exit program")
        choice = input("Please select a choice: ").upper()

        if choice == 'A':
            num = input("Please insert a number: ")
            menu_2(num)
        elif choice == 'B':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Please select a valid choice.")


def menu_2(num):
    while True:
        print("\nMenu 2 - Please select the base you want to convert a number from")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")
        base_from = input("Please select a choice: ").upper()

        if base_from in ('A', 'B', 'C', 'D'):
            if base_from == 'A':
                valid_input = is_valid_decimal(num)
            elif base_from == 'B':
                valid_input = is_valid_binary(num)
            elif base_from == 'C':
                valid_input = is_valid_octal(num)
            elif base_from == 'D':
                valid_input = is_valid_hexadecimal(num)

            if valid_input:
                menu_3(num, base_from)
                return  # to exit the function after Menu 3
            else:
                print(f"Invalid input for base {base_from}. Please try again.")
        else:
            print("Please select a valid choice.")


def menu_3(num, base_from):
    while True:
        print("\nMenu 3 - Please select the base you want to convert a number to")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")
        base_to = input("Please select a choice: ").upper()

        if base_to in ('A', 'B', 'C', 'D'):
            convert_and_display(num, base_from, base_to)
            break
        else:
            print("Please select a valid choice.")


def convert_and_display(num, base_from, base_to):
    if base_from == 'A':
        decimal_num = int(num)
    elif base_from == 'B':
        decimal_num = bin_to_dec(num)
    elif base_from == 'C':
        decimal_num = oct_to_dec(num)
    elif base_from == 'D':
        decimal_num = hex_to_dec(num)

    """Here the function, If there is no direct way to convert from number system to other, 
    it converts to decimal then to the base we want to convert to"""

    if base_to == 'A':
        result = decimal_num
    elif base_to == 'B':
        result = dec_to_bin(decimal_num)
    elif base_to == 'C':
        result = dec_to_oct(decimal_num)
    elif base_to == 'D':
        result = dec_to_hex(decimal_num)
    print(f"Result: {num} ({base_from}) is {result} ({base_to})")

# Main program starts here
menu_1()
