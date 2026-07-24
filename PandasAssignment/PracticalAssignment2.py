import pandas as pd

print("Practical Assignment 2")

# Create Dataset
data = {
    "Name":["Amit","Priya","Rahul","Sneha","Arjun","Amit"],
    "Age":[20,21,19,22,None,20],
    "Gender":["Male","Female","Male","Female","Male","Male"],
    "City":["Pune","Mumbai","Pune","Delhi","Mumbai","Pune"],
    "Course":["Python","AI","Python","Data Science","AI","Python"],
    "Marks":[85,90,72,78,None,85],
    "Attendance":[92,95,88,91,75,92],
    "Purchased":["Yes","Yes","No","Yes","No","Yes"]
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("students_2.csv", index=False)

print("\nOriginal Data")
print(df)


# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Attendance"].fillna(df["Attendance"].mean(), inplace=True)


# Remove Duplicates
print("\nDuplicates")
print(df[df.duplicated()])

df.drop_duplicates(inplace=True)


# Filtering
print("\nMarks > 80")
print(df[df["Marks"] > 80])

print("\nAttendance > 90")
print(df[df["Attendance"] > 90])


# Statistics
print("\nMaximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())
print("Average Marks:", df["Marks"].mean())


# Unique and Count
print("\nCourses")
print(df["Course"].unique())

print("\nCity Count")
print(df["City"].value_counts())


# GroupBy
print("\nAverage Marks by Course")
print(df.groupby("Course")["Marks"].mean())


# Correlation
print("\nCorrelation")
print(df.select_dtypes("number").corr())


# Encoding
df["Gender"] = df["Gender"].map({"Male":1,"Female":0})
df["Purchased"] = df["Purchased"].map({"Yes":1,"No":0})


# One Hot Encoding
df = pd.get_dummies(df, columns=["City","Course"], dtype=int)

print("\nEncoded Data")
print(df)


# Features and Target
X = df[["Age","Attendance","Marks","Gender"]]
y = df["Purchased"]

print("\nFeatures")
print(X)

print("\nTarget")
print(y)


# Save Clean Dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully")
