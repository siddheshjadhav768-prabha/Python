class Hospital:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization

h1 = Hospital("Dr Sharma", "Cardiology")
h2 = Hospital("Dr Patil", "Neurology")

print(h1.doctor_name, h1.specialization)
print(h2.doctor_name, h2.specialization)