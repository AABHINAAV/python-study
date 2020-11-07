# class Computer:     # acc. to convention we need to use capitalised name of class
#     # we can use any other word also instead of self but acc. to convention we use self
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def config(self):
#         print(f"{self.cpu}  :  {self.ram}")

# comp1 = Computer('i5',16)
# comp2 = Computer('ryzen 3',8)
# comp1.config()                  # calling function using class object
# Computer.config(comp2)          # calling function using class name and passing object
# print(comp1)
# print(type(comp1))
# print(id(comp1))     ##it will show id which is assigned to object during creation

# self represents the object with which class has been initialised and that object contains the
# variables that are being passed to class as an argument


# we can use any other too to show the object instead of self but that is against the conventions
# class Computer:
#     def __init__(details,brand,price):
#         details.brand=brand
#         details.price=price
#     def show(details):
#         print(f"{details.brand} : {details.price}")

# obj = Computer('hp',50000)
# obj.show()



# instance variable has different value for different objects-----
# class Computer:
#     x = 100
#     def __init__(self,num):
#         self.num = num      # instance variable
#         self.show()
#     def show(self):
#         print(self.num)
#         print(Computer.x)   # calling class variable
# obj= Computer(10)
# print(obj.__dict__)     # prints name and values of instance vairables of object





# self vs class name for class variables
# self.variable_name --> use them to get specific or changed value of class variable
# class_name.variable_name --> use them to have same value of class variable for all the time
# class Computer:
#     num = 10
#     def __init__(self,num):
#         self.num=num
#     def show1(self):
#         print(self.num)
#     def show2(self):
#         print(Computer.num)
    
# obj = Computer(100)
# obj.show1()
# obj.show2()
# obj.num = 100000        # changes the value of self type variable only
# obj.show1()
# obj.show2()







# program to find the number of isntances/objcets of a class
# class Computer:
#     count_instance = 0
#     def __init__(self):
#         Computer.count_instance += 1
# obj1=Computer()
# obj2=Computer()
# obj3=Computer()
# print(Computer.count_instance)



# using class method as constructor 
# or we can say user defined constructor for some other purpose
# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def show(self):
#         print(f"full name : {self.fname} {self.lname}")
#     @classmethod
#     def from_string(cls,string):
#         first,last,age=string.split(',')
#         return cls(first,last,age)

# obj1 = Person('abhi','garg',22)         # initialising values with constructor
# # obj2 = Person('jassi','rana',23)         # initialising values with constructor
# # obj2 = Person(1,2,3)                #same class diff object with diff type of data
# obj1.show()
# obj2.show()
# obj3 = Person.from_string('ankit,nau,25')         # initialising values with class method
# obj3.show()



# everuthing is public in python
# in python __name__ ---> it is a convention for private method
# they are also called dunder method/magic method






# __name ---> if we give such name to any instance variable then python changes it to:-
# _classname__name        so it can be accessed outside class by this name only
# it is still public but to give it a special meaning python did so
# it is sometimes useful in inheritance
# it is called name mangling

# class school:
#   __x=10

# class students(school):
#   def show(self):
#     print(f'by instance method : {self._school__x}')
  
#   @classmethod
#   def show1(cls):
#     print(f'by instance method : {cls._school__x}')
  
# obj1 = students()
# obj1.show()
# obj1.show1()
# print(f'by student class object method : {obj1._school__x}')
# obj2=school()
# print(f'by school class object method : {obj2._school__x}')
# print(f'by calling directly using student class : {students._school__x}')
# print(f'by calling directly using school class : {school._school__x}')








# in python everything is class
# l=[1,2,3,4,5]       # l is object of list class
# l.append(6)         # calling append function of list class using object l
# list.append(l,6)        # calling append function of list class with its name and passing object as argument------this is actual working-----above it is the shorthand of it-----l object goes to self argument in append function of list class




# class computer:
#     def __init__(self):
#         self.name='abhi'
#         self.age=22

#     def update(self):
#         self.age=50

#     def compare(self,obj1):
#         if self.age == obj1.age:
#             return True
#         return False

# c1=computer()
# c2=computer()
# c1.update()

# #it is not a built in function,,we are calling function with one object and passing another object as an argument
# if c1.compare(c2):
#     print('yes')
# else:
#     print('no')






# namespace -- it is an area where you create and store object/variable
# it is of 2 types:-
# class namespace -- where u store class variables
# instance namespace -- where u store instance variables





# there are 2 types of variables:--
# 1) static/class variables
# 2) instance variables
# class car:
#     wheels=4        ##class/static variables(changable in main())
#     def __init__(self):
#         self.mil=10     ##instance variables(changable in main())
#         self.com='bmw'     ##instance variables

# c1=car()
# c2=car()
# c2.com='audi'
# print(c1.com)
# print(c2.com)
# print(c1.wheels)
# print(c2.wheels)
# print(car.wheels)




# ACCESSORS --> the user defined functions to get the value of a variable which are also called getters in C, here called accessors
# MUTATORS --> the user defined functions to set the value of a variable which are also called setters in C, here called mutators





# there are three types of methods:-
# 1) instance methods  --> to work with instance variables we use instance method
# 2) class methods  --> to work with class variables we use class methods
# 3) static methods --> when we dont to work  with class variables or with instance variables....then we use static method
# class students:
#     school='garg'
#     def __init__(self,m1,m2,m3):    ##instance method
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
    
#     def avg(self):      ##instance method
#         return (self.m1+self.m2+self.m3)/3

#     @classmethod       ##decorators--to define class method
#     def getSchoolName(cls):      ##class method
#         return (cls.school)

#     @staticmethod     ##decorator--to define static method
#     def info():                 ##static method
#         print('it is printed using static method')

# s1=students(10,20,30)
# s2=students(50,60,70)
# ##calling instance method-----
# print(s1.avg())
# print(s2.avg())
# ##calling class method-----
# print(s1.getSchoolName())
# print(s2.getSchoolName())
# print(students.getSchoolName())
# ##calling static method-----
# s1.info()
# s2.info()
# students.info()







# object of inner class is created in constructor(__init__) of outer class
# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap = self.laptop()

#     def show(self):
#         print(self.name,self.rollno)

#     class laptop:
#         def __init__(self):
#             self.brand='hp'
#             self.ram=4
#             self.cpu='i5'

#         def show(self):
#             print(self.brand,self.cpu,self.ram)

# s1=student('abhi',1)
# # outer class variables-----
# print(s1.name)
# s1.show()
# # inner class variables-----
# print(s1.lap.brand)
# s1.lap.show()






##########  abstract method ##########
# from abc import ABCMeta , abstractmethod
# # class Shape():        ## not abstract class now
# class Shape(metaclass=ABCMeta):     ## became abs cls coz it has function without implementation
#     @abstractmethod
#     def printarea(self):
#         return 0
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=10
#         self.breadth=20
#     def printarea(self):
#         print(self.length*self.breadth)

# obj1 = Rectangle()
# obj1.printarea()
