print("Assignment 4")
import numpy as np

# Q1: Reshape 1D array into 3x4 matrix
arr = np.arange(1, 13)
print("Q1:")
print(arr.reshape(3, 4))

# Q2: Reshape 1D array into 4x4 matrix
arr = np.arange(1, 17)
print("\nQ2:")
print(arr.reshape(4, 4))

# Q3: Convert 1D array into 2x3x4 3D array
arr = np.arange(1, 25)
print("\nQ3:")
print(arr.reshape(2, 3, 4))

# Q4: Reshape 18 elements into 3x6 matrix
arr = np.arange(1, 19)
print("\nQ4:")
print(arr.reshape(3, 6))

# Q5: Reshape using -1
arr = np.arange(1, 21)
print("\nQ5:")
print(arr.reshape(4, -1))

# Q6: Reshape 3x4 matrix into 2x6 matrix
arr = np.arange(1, 13).reshape(3, 4)
print("\nQ6:")
print(arr.reshape(2, 6))

# Q7: Convert 3D array back to 1D
arr = np.arange(1, 13).reshape(2, 3, 2)
print("\nQ7:")
print(arr.flatten())

# Q8: Flatten 3x3 matrix
arr = np.arange(1, 10).reshape(3, 3)
print("\nQ8:")
print(arr.flatten())

# Q9: Ravel 4x2 matrix
arr = np.arange(1, 9).reshape(4, 2)
print("\nQ9:")
print(arr.ravel())

# Q10: Transpose
arr = np.arange(1, 9).reshape(2, 4)
print("\nQ10:")
print("Original:\n", arr)
print("transpose():\n", arr.transpose())
print(".T:\n", arr.T)

# Q11: Resize 3x3 matrix into 2x6 matrix
arr = np.arange(1, 10).reshape(3, 3)
print("\nQ11:")
print(np.resize(arr, (2, 6)))

# Q12: Resize 1D array into 3x3 matrix
arr = np.array([10, 20, 30])
print("\nQ12:")
print(np.resize(arr, (3, 3)))

# Q13: Flatten and modify
arr = np.array([[1,2,3],[4,5,6]])
flat = arr.flatten()
flat[0] = 100
print("\nQ13:")
print("Original:\n", arr)
print("Flattened:\n", flat)

# Q14: Ravel and modify
arr = np.array([[1,2,3],[4,5,6]])
rav = arr.ravel()
rav[0] = 100
print("\nQ14:")
print("Original:\n", arr)
print("Raveled:\n", rav)

# Q15: Concatenate
a = np.array([10,20,30])
b = np.array([40,50,60])
print("\nQ15:")
print(np.concatenate((a,b)))

# Q16: hstack
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print("\nQ16:")
print(np.hstack((a,b)))

# Q17: vstack
print("\nQ17:")
print(np.vstack((a,b)))

# Q18: Split into 4 parts
arr = np.arange(1,13)
print("\nQ18:")
print(np.split(arr,4))

# Q19: Split 4x2 matrix
arr = np.arange(1,9).reshape(4,2)
print("\nQ19:")
print(np.split(arr,2))

# Q20: Concatenate three arrays
a = np.array([1,2])
b = np.array([3,4])
c = np.array([5,6])
print("\nQ20:")
print(np.concatenate((a,b,c)))

# Q21: Broadcasting Bonus
salary = np.array([25000,30000,35000,40000,45000])
print("\nQ21:")
print(salary + 5000)

# Q22: Broadcasting Grace Marks
marks = np.array([[70,80,90],
                  [60,75,85]])
grace = np.array([5,5,10])
print("\nQ22:")
print(marks + grace)

# Q23: Copy
arr = np.array([10,20,30,40])
copy_arr = arr.copy()
copy_arr[0] = 999
print("\nQ23:")
print("Original:", arr)
print("Copy:", copy_arr)

# Q24: View
arr = np.array([100,200,300,400])
view_arr = arr.view()
view_arr[0] = 999
print("\nQ24:")
print("Original:", arr)
print("View:", view_arr)

# Q25: Mini Project
salary = np.array([[25000,30000,35000],
                   [40000,45000,50000]])

print("\nQ25:")
print("Original Matrix:\n", salary)

reshaped = salary.reshape(3,2)
print("\nReshaped (3x2):\n", reshaped)

print("\nFlattened:")
print(reshaped.flatten())

print("\nTranspose:")
print(salary.T)

print("\nSalary + 2000:")
print(salary + 2000)

copy_salary = salary.copy()
copy_salary[0,0] = 99999

view_salary = salary.view()
view_salary[0,1] = 88888

print("\nOriginal after View Modification:")
print(salary)

print("\nCopied Matrix:")
print(copy_salary)

print("\nView Matrix:")
print(view_salary)
