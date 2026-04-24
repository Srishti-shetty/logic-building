'''Write a Program to Find the Quotient and Remainder of Two Integers:
Write a program where the user enters two integers (divisor and dividend) and
calculates their quotient and remainder. For example:
○ Input: Dividend: 22, Divisor: 7
○ Output:Quotient: 3
Remainder: 1'''

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
quotient = dividend 
remainder = dividend % divisor
print("Quotient:", quotient)
print("Remainder:", remainder)