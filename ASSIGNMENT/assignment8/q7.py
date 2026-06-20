class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError

    print("You entered:", num)

except NegativeNumberError:
    print("Negative numbers are not allowed.")