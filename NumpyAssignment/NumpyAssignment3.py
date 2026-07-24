print("Assignment 3")
import numpy as np

# Q1: Addition
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([5,10,15,20,25])
print("Q1: Addition")
print(arr1 + arr2)

# Q2: Subtraction
print("\nQ2: Subtraction")
print(arr1 - arr2)

# Q3: Multiplication
print("\nQ3: Multiplication")
print(arr1 * arr2)

# Q4: Division
print("\nQ4: Division")
print(arr1 / arr2)

# Q5: Floor Division, Modulus, Power
arr = np.array([12,24,36,48,60])
print("\nQ5: Operations")
print("Floor Division by 5:", arr // 5)
print("Modulus by 5:", arr % 5)
print("Power of 2:", arr ** 2)

# Q6: Salary Bonus
salary = np.array([25000,30000,35000,40000,45000])
print("\nQ6: Salary with Bonus")
print(salary + 5000)

# Q7: Student Marks Increase
marks = np.array([65,70,75,80,85])
print("\nQ7: Marks after +5")
print(marks + 5)

# Q8: Comparison Operators
arr = np.array([15,25,35,45,55])
print("\nQ8: Comparison")
print("Greater than 30:", arr[arr > 30])
print("Less than 40:", arr[arr < 40])

# Q9: Greater than or Equal / Less than or Equal
arr = np.array([50,60,70,80,90])
print("\nQ9:")
print(">=70:", arr[arr >= 70])
print("<=60:", arr[arr <= 60])

# Q10: Elements Equal to 20
arr = np.array([10,20,30,20,40,20])
print("\nQ10:")
print(arr[arr == 20])

# Q11: Even and Odd Numbers
arr = np.array([12,15,18,21,24,27,30])
print("\nQ11:")
print("Even:", arr[arr % 2 == 0])
print("Odd:", arr[arr % 2 != 0])

# Q12: Total and Average Marks
marks = np.array([75,82,90,68,88])
print("\nQ12:")
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))

# Q13: Median, Minimum, Maximum
print("\nQ13:")
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

# Q14: Salary Statistics
salary = np.array([25000,30000,35000,45000,55000])
print("\nQ14:")
print("Total Salary:", np.sum(salary))
print("Average Salary:", np.mean(salary))
print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))

# Q15: Variance and Standard Deviation
arr = np.array([20,30,40,50,60])
print("\nQ15:")
print("Variance:", np.var(arr))
print("Standard Deviation:", np.std(arr))

# Q16: Sorting
arr = np.array([45,12,78,25,60,30])
print("\nQ16:")
print("Ascending:", np.sort(arr))
print("Descending:", np.sort(arr)[::-1])

# Q17: Salary Ascending
salary = np.array([35000,25000,60000,45000,30000])
print("\nQ17:")
print(np.sort(salary))

# Q18: Salary Descending
print("\nQ18:")
print(np.sort(salary)[::-1])

# Q19: Index Position of 30
arr = np.array([10,20,30,40,50,30])
print("\nQ19:")
print(np.where(arr == 30))

# Q20: Searchsorted for 18
arr = np.array([5,10,15,20,25,30])
print("\nQ20:")
print(np.searchsorted(arr,18))

# Q21: Searchsorted for 350
arr = np.array([100,200,300,400,500])
print("\nQ21:")
print(np.searchsorted(arr,350))

# Q22: Unique Values
arr = np.array([10,20,20,30,40,40,50])
print("\nQ22:")
print(np.unique(arr))

# Q23: Unique Marks
marks = np.array([70,80,70,90,80,95])
print("\nQ23:")
print(np.unique(marks))

# Q24: Student Marks Operations
marks = np.array([78,65,90,55,88,72,95])
print("\nQ24:")
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Ascending:", np.sort(marks))
print("Descending:", np.sort(marks)[::-1])

# Q25: Employee Salary Operations
salary = np.array([25000,30000,45000,30000,60000,45000,70000])
print("\nQ25:")
print("Total Salary:", np.sum(salary))
print("Average Salary:", np.mean(salary))
print("Highest Salary:", np.max(salary))
print("Lowest Salary:", np.min(salary))
print("Unique Salaries:", np.unique(salary))
print("Ascending:", np.sort(salary))
print("Descending:", np.sort(salary)[::-1])
print("Salary > 40000:", salary[salary > 40000])
