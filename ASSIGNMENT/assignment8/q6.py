numbers = [10, 20, 30, 40, 50]

try:
    num = int(input("Enter a number: "))
    index = int(input("Enter index: "))

    print("Element:", numbers[index])

except ValueError:
    print("Invalid input.")

except IndexError:
    print("Index out of range.")