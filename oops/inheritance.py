#single inheritance

class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def manage(self):
        print("Manager is managing the team")

# Usage
m = Manager()
m.work()
m.manage()

#Multilevel Inheritance
class Company:
    def company_info(self):
        print("Company")

class Department(Company):
    def department_info(self):
        print("Department")

class Team(Department):
    def team_info(self):
        print("Team")

# Usage
t = Team()
t.company_info()
t.department_info()
t.team_info()

#Multiple Inheritance
class HR:
    def hr_policies(self):
        print("HR")

class Finance:
    def finance_policies(self):
        print("Finance")

class Admin(HR, Finance):
    def admin_info(self):
        print("Admin: Coordinates HR and Finance")

# Usage
a = Admin()
a.hr_policies()
a.finance_policies()
a.admin_info()

#Hierarchical Inheritance
class Employee:
    def employee_info(self):
        print("Employee details")

class Developer(Employee):
    def dev_role(self):
        print("Developer")

class Tester(Employee):
    def tester_role(self):
        print("Tester")


dev = Developer()
dev.employee_info()
dev.dev_role()

test = Tester()
test.employee_info()
test.tester_role()

#hybrid inheritance
class Person:
    def person_info(self):
        print("Person: Basic personal details")

class Employee(Person):
    def employee_info(self):
        print("Employee: General employee info")

class Consultant:
    def consultant_info(self):
        print("Consultant: Works part-time")

class FreelanceConsultant(Employee, Consultant):
    def freelance_info(self):
        print("Freelance Consultant: Works remotely")

# Usage
fc = FreelanceConsultant()
fc.person_info()
fc.employee_info()
fc.consultant_info()
fc.freelance_info()
