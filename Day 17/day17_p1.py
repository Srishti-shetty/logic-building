'''Write a Program to Convert Binary Numbers to Decimal and Vice Versa
Manually:
Write a program that uses user-defined functions to convert binary numbers to
decimal and decimal numbers to binary. For example:
○ Input: Enter a binary number: 1010
○ Output: Decimal equivalent: 10
○ Input: Enter a decimal number: 10
○ Output: Binary equivalent: 1010

Binary to Decimal Conversion
Binary Number:
A binary number consists of 0 and 1 digits and follows base 2.
Instruction:
● Start from the rightmost digit (position = 0).
● Multiply each bit by 2position2^{position}2position.
● Add all the values to get the decimal number.
'''
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        digit = binary % 10
        decimal = decimal + digit * (2 ** power)
        binary = binary // 10
        power += 1
    return decimal
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        rem = decimal % 2
        binary = str(rem) + binary
        decimal = decimal // 2
    return binary
binary_num = int(input("Enter a binary number: "))
print("Decimal equivalent:", binary_to_decimal(binary_num))
decimal_num = int(input("Enter a decimal number: "))
print("Binary equivalent:", decimal_to_binary(decimal_num))

'''OUTPUT:
Enter a binary number: 1011
Decimal equivalent: 11
Enter a decimal number: 11
Binary equivalent: 1011'''