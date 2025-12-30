class Employee():
    __country = "India" # PRIVATE CLASS VARIABLE

    def set_info(self, n, d): # PUBLIC METHOD # SETTER METHOD
        self.__name = n         # e1._Employee__name = 'Akshay'
        self.__designation = d

    def get_info(self): # PUBLIC METHOD # GETTER METHOD
        print(f"NAME:{self.__name}, DESG: {self.__designation}")

    def __employeeSalary(self): # PRIVATE METHOD
        print('employee Salary')


e1 = Employee()
#print(e1.country)# AttributeError: 'Employee' object has no attribute 'country'


e1.set_info('Akshay', 'manager')

#print(e1.name)# AttributeError: 'Employee' object has no attribute 'name'
#print(e1._Employee__name)  # name Mangling # NOT Recommended

#print(e1.__name) # AttributeError: 'Employee' object has no attribute '__name'

e1.get_info()

#e1.employeeSalary() # AttributeError: 'Employee' object has no attribute 'employeeSalary'
#e1.__employeeSalary() # AttributeError: 'Employee' object has no attribute '__employeeSalary'

#e1._Employee__employeeSalary() # name Mangling # NOT Recommended
print(Employee.__dict__)









