class Employee():
    company="TCS"

    def show(self):
        print(f"The name of {self.name} is available")


class programmer(Employee):
    def showlanguag(self):
        print(f"The programmer is {self.languag} languaag")        

a=    Employee()   
b=programmer()
 
print(a.company,b.company)