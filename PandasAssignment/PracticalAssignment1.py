print("Practical Assignment 1")
import pandas as pd

# Q1: Create DataFrame
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Age": [20, 21, 22, 20, 23],
    "City": ["Pune", "Mumbai", "Pune", "Nashik", "Mumbai"],
    "Marks": [85, 78, 92, 70, 88]
}

df = pd.DataFrame(data)

# Q2: Display Complete DataFrame
print("Q2: Complete DataFrame")
print(df)

# Q3: First 3 Rows
print("\nQ3: First 3 Rows")
print(df.head(3))

# Q4: Last 2 Rows
print("\nQ4: Last 2 Rows")
print(df.tail(2))

# Q5: Shape
print("\nQ5: Shape")
print(df.shape)

# Q6: Column Names
print("\nQ6: Column Names")
print(df.columns)

# Q7: Dataset Information
print("\nQ7: Dataset Information")
print(df.info())

# Q8: Statistical Summary
print("\nQ8: Statistical Summary")
print(df.describe())

# Q9: Read CSV File
print("\nQ9: Read CSV File")
try:
    students = pd.read_csv("students.csv")
    print(students)
except FileNotFoundError:
    print("students.csv file not found.")

# Q10: Save DataFrame to CSV
df.to_csv("students_backup.csv", index=False)
print("\nQ10: DataFrame saved as students_backup.csv")

# Q11: Display Name Column
print("\nQ11: Name Column")
print(df["Name"])

# Q12: Display Name and Marks
print("\nQ12: Name and Marks")
print(df[["Name", "Marks"]])

# Q13: Marks Greater Than 80
print("\nQ13: Marks > 80")
print(df[df["Marks"] > 80])

# Q14: Age Greater Than 20
print("\nQ14: Age > 20")
print(df[df["Age"] > 20])

# Q15: Students from Pune
print("\nQ15: Students from Pune")
print(df[df["City"] == "Pune"])

# Q16: Marks Between 70 and 90
print("\nQ16: Marks Between 70 and 90")
print(df[(df["Marks"] >= 70) & (df["Marks"] <= 90)])

# Q17: City Mumbai and Marks > 75
print("\nQ17: Mumbai and Marks > 75")
print(df[(df["City"] == "Mumbai") & (df["Marks"] > 75)])

# Q18: Sort by Marks (Ascending)
print("\nQ18: Marks Ascending")
print(df.sort_values("Marks"))

# Q19: Sort by Marks (Descending)
print("\nQ19: Marks Descending")
print(df.sort_values("Marks", ascending=False))

# Q20: Unique Cities
print("\nQ20: Unique Cities")
print(df["City"].unique())

# Q21: Count Students in Each City
print("\nQ21: Students in Each City")
print(df["City"].value_counts())

# Q22: Display Duplicate Records
print("\nQ22: Duplicate Records")
print(df[df.duplicated()])

# Q23: Remove Duplicate Records
print("\nQ23: DataFrame After Removing Duplicates")
print(df.drop_duplicates())

# Q24: Check Missing Values
print("\nQ24: Missing Values")
print(df.isnull())

# Q25: Count Missing Values
print("\nQ25: Missing Values Count")
print(df.isnull().sum())
