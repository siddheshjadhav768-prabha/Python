from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Developer writes code")

class Designer(Employee):

    def work(self):
        print("Designer creates UI designs")

employees = [Developer(), Designer()]

for emp in employees:
    emp.work()