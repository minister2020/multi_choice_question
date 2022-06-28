"""


class Security:
    motto = "Oluwa nii oluso Guntan yin!"

    def open(self):
        return "No Oka is allow here from 10PM"

    def close(self):
        return "The gate will be free by 5AM"

class Bft(Security):
    motto = "Education is the key"

    def admin(self):
        name = "Jadesola"
        role = "project manager"
        return f"Hi, I'm {name}, the current {role} of BFT our motto is {self.motto}"

    def coo(self):
        name = "Tela"
        role = "COO"
        return f"Hi, I'm {name}, the current {role} of BFT"

    def ceo(self):
        name = "Mr Hafeez"
        role = "CEO"
        return f"Hi, I'm {name}, the current {role} of BFT"

new_bft = Bft()
foo = Bft()

# print(new_bft.motto)
# print(foo.admin())


class Student(Bft):
    sologan = "Student is ..."
    def student_admin(self):
        name = "Abd Rasheed"
        role = "SUG"
        return f"Hi, I'm {name}, the current {role} of BFT our motto is {self.motto}"

    def student_coo(self):
        name = "Balikis"
        role = "COO"
        return f"Hi, I'm {name}, the current {role} of BFT"

    def student_ceo(self):
        name = "Telma"
        role = "CEO"
        return f"Hi, I'm {name}, the current {role} of BFT"




student = Student()

print(student.admin())
print(student.open())
print(student.close())



class Person:
   # counter = 0
     
    def __init__(self, name, age):
        self.name = name
        self.age = age
       # Person.counter += 1
    def greet(self):   
        return f"Hi, it is {self.name}, and am {self.age}years old" 


p1 = Person('John', 25)
#p2 = Person('Jane', 22)
print(hex(id(p1.greet())))


      

class Table:
    def table1(self): 
       return "This table belongs to bigfix"



class Table2(Table):

    def table2(self):
        return "this table belong to big_fix"


    


new_tab = Table2()    
new = Table2()


print(new.table2())
print(new_tab.table1())




   
      
num = int(input("enter a number: "))
for i in range(1, 13):
    print(num, "x", i,"=", num * i)
"""
      




class Computer:
    def __init__(self):
        self.name = "Base"
        self.age = 23

   

    def compare(self, other):
       if self.age == other.age:
           return True
       
       else:

          return False
   

c1 = Computer()
c1.age = 12
c2 = Computer()

if c1.compare(c2):
 print('they are the same')
 
print(c1.name)
print((c2.age))
#print(id(c3))