import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
attendance = [40, 42, 39, 45, 44]

plt.figure(figsize=(8,5))

plt.plot(days, attendance,
         color="purple",
         marker="D")

plt.title("Attendance Chart")
plt.xlabel("Days")
plt.ylabel("Attendance")

plt.show()
