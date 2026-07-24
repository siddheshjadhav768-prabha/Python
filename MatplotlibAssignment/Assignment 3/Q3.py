import matplotlib.pyplot as plt

subjects = ["Eng","Math","Sci","Comp"]
marks = [75,85,80,90]
attendance = [40,42,39,45]
hours = [2,3,4,5]

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(subjects, marks)
plt.title("Student Marks")

plt.subplot(2,2,2)
plt.bar(subjects, attendance)
plt.title("Attendance")

plt.subplot(2,2,3)
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Subject Distribution")

plt.subplot(2,2,4)
plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")

plt.tight_layout()
plt.show()
