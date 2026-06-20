class Person:
    def __init__(self, name):
        self.name = name


class Doctor(Person):
    def treat(self):
        print(self.name, "treats patients")


class Nurse(Person):
    def assist(self):
        print(self.name, "assists doctor")


class HeadNurse(Nurse):
    def supervise(self):
        print(self.name, "supervises nurses")


head_nurse = HeadNurse("Priya")
head_nurse.assist()
head_nurse.supervise()