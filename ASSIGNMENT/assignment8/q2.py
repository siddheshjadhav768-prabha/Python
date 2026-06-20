#handle invalid number input
try:                    
    
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result of {numerator} divided by {denominator} is {result}.")
except ZeroDivisionError:  
        print("Error: Division by zero is not allowed.")
except ValueError:
        print("Error: Please enter valid integers for numerator and denominator.")

            