print("Mini Project")

import pandas as pd

# Create Dataset

data = {
    "Student_ID":[101,102,103,104,105,106,107,108,109,110,111,112,113],
    "Name":["Raj","Amit","Priya","Sneha","Rahul","Pooja","Karan","Neha","Akash","Komal","Vikas","Riya","Raj"],
    "Age":[21,22,20,23,21,22,20,21,24,23,None,22,21],
    "Gender":["Male","Male","Female","Female","Male","Female","Male","Female","Male","Female","Male","Female","Male"],
    "City":["Pune","Mumbai","Nashik","Pune","Mumbai","Pune","Nashik","Pune","Mumbai","Pune","Pune","Mumbai","Pune"],
    "Course":["Python","AI","Python","Data Science","AI","Python","Data Science","AI","Python","Data Science","Python","AI","Python"],
    "Attendance":[90,80,95,88,75,98,82,91,85,96,90,None,90],
    "Marks":[85,75,92,81,65,96,79,89,72,94,None,85,85],
    "Purchased":["Yes","No","Yes","Yes","No","Yes","No","Yes","No","Yes","Yes","No","Yes"]
}

df = pd.DataFrame(data)

df.to_csv("student_performance.csv", index=False)


# Load Dataset

df = pd.read_csv("student_performance.csv")

print("\nComplete Dataset")
print(df)


# Data Exploration

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nSummary")
print(df.describe())


# Data Cleaning

print("\nMissing Values")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())


# Duplicate Records

print("\nDuplicate Records")
print(df[df.duplicated()])

df.drop_duplicates(inplace=True)


# Selection

print("\nName and Marks")
print(df[["Name","Marks"]])

print("\nName City Course")
print(df[["Name","City","Course"]])


# Filtering

print("\nMarks > 80")
print(df[df["Marks"] > 80])

print("\nPune Students")
print(df[df["City"]=="Pune"])

print("\nFemale Students")
print(df[df["Gender"]=="Female"])

print("\nAI Students")
print(df[df["Course"]=="AI"])


# Sorting

print("\nMarks Descending")
print(df.sort_values("Marks",ascending=False))


# Unique Values

print("\nCities")
print(df["City"].unique())

print("\nCourses")
print(df["Course"].unique())


# Value Counts

print("\nCity Count")
print(df["City"].value_counts())

print("\nCourse Count")
print(df["Course"].value_counts())


# GroupBy

print("\nAverage Marks by Course")
print(df.groupby("Course")["Marks"].mean())


print("\nCourse Statistics")
print(
    df.groupby("Course").agg(
        Total_Marks=("Marks","sum"),
        Average_Marks=("Marks","mean"),
        Max_Marks=("Marks","max"),
        Min_Marks=("Marks","min")
    )
)


# Correlation

print("\nCorrelation")
print(df.select_dtypes("number").corr())


# Encoding

df["Gender"] = df["Gender"].map({
    "Male":1,
    "Female":0
})

df["Purchased"] = df["Purchased"].map({
    "Yes":1,
    "No":0
})


# One Hot Encoding

df = pd.get_dummies(
    df,
    columns=["City","Course"],
    dtype=int
)


# Features and Target

X = df[["Age","Attendance","Marks","Gender"]]

y = df["Purchased"]


print("\nFeatures")
print(X)

print("\nTarget")
print(y)


# Save Cleaned Dataset

df.to_csv(
    "cleaned_student_performance.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully")
