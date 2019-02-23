decimal_str = input("Enter a number: ")  # prompt for a number

decimal_int = int(decimal_str)  # Changing type from string to integer
final_string = ''  # initializing string

user_base_str = input("Enter what base: ")
user_base_int = int(user_base_str)


while decimal_int != 0:
    binary_int = decimal_int % user_base_int  # Finds modules
    decimal_int = decimal_int / user_base_int  # Divides users number by 2
    decimal_int = int(decimal_int)  # Changes from a float to an int
    binary_str = str(binary_int)  # Changes from int to string
    final_string = binary_str + final_string  # Concatenates answer onto the string

print("The output is: ", final_string)  # Outputs the binary


# Binary back to decimal
i = len(final_string) - 1
temp_total = 0
Total = 0
y = 0

while i >= 0:

    turn_back = int(final_string[i])
    temp_total = user_base_int**y * turn_back

    Total = Total + temp_total
    y = y + 1
    i = i - 1

print("\nYour number has been changed back to:", Total)

