import random
import string

from emp.models import Employee_data

# exec(open(r'E:\PYTHON_B6\Python_Code\Django\Employee_Record\emp\db_shell.py').read())

# Creating the random data for 50 employees for all fileds that we have mentioned in class.

des = ['Python Devloper', 'Soft. Engg.', 'Lenus Administrator', 'Associates', 'Data scientist', 'Jave devloper'] 

for i in range(50):

    # For generating 50 Random strings as an employee Name of 10 letters in lowercase.
    letters = string.ascii_lowercase
    name =  ("".join(random.choice(letters) for i in range(10)) )

    # For generating 50 Random numbers as an employee Salary of 5 digits.
    letters = string.digits
    sal =  ("".join(random.choice(letters) for i in range(5)))
    
    # For generating 50 Random strings as an employee Company name of 10 letters in uppercase.
    letters = string.ascii_uppercase
    comp = ("".join(random.choice(letters) for i in range(6)) )

    # For generating Random employee designation.
    design =  random.choice(des)

    # creating employee object

    emp = Employee_data(name=name, salary=sal, company=comp , designation=design)
    emp.save()





    
