print("Numpy Practical Assignment")
import numpy as np

# Q1: Import NumPy
print("Q1: NumPy Imported Successfully")

# Q2: 1D Array (1 to 10)
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print("\nQ2: 1D Array")
print(arr1)

# Q3: 3x3 2D Array
arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print("\nQ3: 3x3 Array")
print(arr2)

# Q4: 2x2x3 3D Array
arr3 = np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
print("\nQ4: 3D Array")
print(arr3)

# Q5: Number of Dimensions
print("\nQ5: Number of Dimensions")
print(arr2.ndim)

# Q6: Shape of 3D Array
print("\nQ6: Shape of 3D Array")
print(arr3.shape)

# Q7: Total Number of Elements
print("\nQ7: Total Elements")
print(arr3.size)

# Q8: Data Type
print("\nQ8: Data Type")
print(arr3.dtype)

# Q9: 5x5 Zero Matrix
zero_matrix = np.zeros((5,5))
print("\nQ9: Zero Matrix")
print(zero_matrix)

# Q10: 4x4 Ones Matrix
ones_matrix = np.ones((4,4))
print("\nQ10: Ones Matrix")
print(ones_matrix)

# Q11: 3x3 Matrix Filled with 100
full_matrix = np.full((3,3),100)
print("\nQ11: Full Matrix")
print(full_matrix)

# Q12: 5x5 Identity Matrix
identity5 = np.eye(5)
print("\nQ12: Identity Matrix")
print(identity5)

# Q13: arange() from 10 to 50
arr_range = np.arange(10,51)
print("\nQ13: arange(10,50)")
print(arr_range)

# Q14: arange() with Step Size 5
step_array = np.arange(0,51,5)
print("\nQ14: arange() Step Size 5")
print(step_array)

# Q15: linspace() from 1 to 100 with 10 values
line1 = np.linspace(1,100,10)
print("\nQ15: linspace(1,100,10)")
print(line1)

# Q16: Decimal Values using linspace()
line2 = np.linspace(0.5,5.5,10)
print("\nQ16: Decimal Values")
print(line2)

# Q17: Student Marks Array
marks = np.array([78,85,90,67,88,92,75,81,69,95])
print("\nQ17: Student Marks")
print(marks)

# Q18: Student Marks Properties
print("\nQ18: Student Marks Properties")
print("Shape:", marks.shape)
print("Size:", marks.size)
print("Dimensions:", marks.ndim)
print("Data Type:", marks.dtype)

# Q19: 2x5 Array
arr25 = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
print("\nQ19: 2x5 Array")
print(arr25)

# Q20: 3x4 Array
arr34 = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])
print("\nQ20: 3x4 Array")
print(arr34)

# Q21: Floating-Point Array
float_array = np.array([1.1,2.2,3.3,4.4,5.5])
print("\nQ21: Floating-Point Array")
print(float_array)
print("Data Type:", float_array.dtype)

# Q22: String Array
string_array = np.array(["Apple","Banana","Cherry","Mango"])
print("\nQ22: String Array")
print(string_array)
print("Data Type:", string_array.dtype)

# Q23: Boolean Array
bool_array = np.array([True, False, True, False])
print("\nQ23: Boolean Array")
print(bool_array)
print("Data Type:", bool_array.dtype)

# Q24: 6x6 Zero Matrix
zero6 = np.zeros((6,6))
print("\nQ24: 6x6 Zero Matrix")
print(zero6)

# Q25: 10x10 Identity Matrix
identity10 = np.eye(10)
print("\nQ25: 10x10 Identity Matrix")
print(identity10)
