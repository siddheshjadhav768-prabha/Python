print("Practical Assignment 2")
import numpy as np

# Q1: First Element
arr = np.arange(1, 21)
print("Q1:")
print(arr[0])

# Q2: Last Element using Negative Indexing
print("\nQ2:")
print(arr[-1])

# Q3: Third Element
print("\nQ3:")
print(arr[2])

# Q4: Last Five Elements
print("\nQ4:")
print(arr[-5:])

# Q5: Elements from Index 3 to 8
print("\nQ5:")
print(arr[3:9])

# Create 4x4 Matrix for Q6-Q13
matrix = np.arange(1, 17).reshape(4, 4)

# Q6: First Row
print("\nQ6:")
print(matrix[0])

# Q7: Last Row
print("\nQ7:")
print(matrix[-1])

# Q8: First Column
print("\nQ8:")
print(matrix[:, 0])

# Q9: Last Column
print("\nQ9:")
print(matrix[:, -1])

# Q10: Middle Two Rows
print("\nQ10:")
print(matrix[1:3])

# Q11: Middle Two Columns
print("\nQ11:")
print(matrix[:, 1:3])

# Q12: First 2x2 Sub-Matrix
print("\nQ12:")
print(matrix[:2, :2])

# Q13: Last 2x2 Sub-Matrix
print("\nQ13:")
print(matrix[2:4, 2:4])

# Create 3D Array
arr3d = np.arange(1, 25).reshape(2, 3, 4)

# Q14: First Matrix
print("\nQ14:")
print(arr3d[0])

# Q15: Second Matrix
print("\nQ15:")
print(arr3d[1])

# Q16: Specific Element
print("\nQ16:")
print(arr3d[1, 2, 3])

# Q17: Even Numbers
arr = np.arange(1, 21)
print("\nQ17:")
print(arr[arr % 2 == 0])

# Q18: Odd Numbers
print("\nQ18:")
print(arr[arr % 2 != 0])

# Q19: Numbers Greater Than 10
print("\nQ19:")
print(arr[arr > 10])

# Q20: Numbers Less Than 15
print("\nQ20:")
print(arr[arr < 15])

# Q21: Fancy Indexing
print("\nQ21:")
print(arr[[0, 2, 4, 6]])

# Q22: First and Last Elements
print("\nQ22:")
print(arr[[0, -1]])

# Q23: 5x5 Matrix
matrix5 = np.arange(1, 26).reshape(5, 5)
print("\nQ23:")
print("First Row:")
print(matrix5[0])
print("Last Row:")
print(matrix5[-1])
print("First Column:")
print(matrix5[:, 0])
print("Last Column:")
print(matrix5[:, -1])

# Q24: 4x5 Matrix
matrix45 = np.arange(1, 21).reshape(4, 5)
print("\nQ24:")
print(matrix45[:, :3])

# Q25: Final Challenge
matrix = np.arange(1, 26).reshape(5, 5)

print("\nQ25:")
print("Original Matrix:")
print(matrix)

print("\nFirst Row:")
print(matrix[0])

print("\nLast Row:")
print(matrix[-1])

print("\nFirst Column:")
print(matrix[:, 0])

print("\nLast Column:")
print(matrix[:, -1])

print("\nMiddle Row:")
print(matrix[2])

print("\nMiddle Column:")
print(matrix[:, 2])

print("\nTop Left 2x2 Matrix:")
print(matrix[:2, :2])

print("\nBottom Right 2x2 Matrix:")
print(matrix[3:, 3:])

print("\nEven Numbers:")
print(matrix[matrix % 2 == 0])

print("\nOdd Numbers:")
print(matrix[matrix % 2 != 0])

print("\nNumbers Greater Than 15:")
print(matrix[matrix > 15])

print("\nNumbers Less Than 10:")
print(matrix[matrix < 10])

print("\nFancy Indexing (1, 7, 13, 19, 25):")
print(matrix[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])

print("\nNegative Indexing (25, 24, 23):")
print(matrix[-1, -1])
print(matrix[-1, -2])
print(matrix[-1, -3])

print("\nLast Three Rows:")
print(matrix[-3:, :])

print("\nFirst Three Columns:")
print(matrix[:, :3])
