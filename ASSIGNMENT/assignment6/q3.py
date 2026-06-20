class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def code(self):
        print(self.name, "is coding")


class Manager(Employee):
    def manage(self):
        print(self.name, "is managing team")


class TechLead(Developer, Manager):
    pass


lead = TechLead("Amit")
lead.code()
lead.manage()