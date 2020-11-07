##single level inheritace-----
# class A:        ##super class/ parent class
#     def feature1(self):
#         print('feature 1 working') 

#     def feature2(self):
#         print('feature 2 working')

# class B(A):     ##sub class/ child class
#     def feature3(self):
#         print('feature 3 working') 

#     def feature4(self):
#         print('feature 4 working')


##multi-level inheritance-----
# class A:        ##super class/ parent class
#     def feature1(self):
#         print('feature 1 working') 

#     def feature2(self):
#         print('feature 2 working')

# class B(A):     ##sub class/ child class
#     def feature3(self):
#         print('feature 3 working') 

#     def feature4(self):
#         print('feature 4 working')

# class C(B):     ##sub class/ child class
#     def feature3(self):
#         print('feature 5 working') 

#     def feature4(self):
#         print('feature 6 working')


##mutiple inheritance-----
# class A:        ##super class/ parent class
#     def feature1(self):
#         print('feature 1 working') 

#     def feature2(self):
#         print('feature 2 working')

# class B:     ##sub class/ child class
#     def feature3(self):
#         print('feature 3 working') 

#     def feature4(self):
#         print('feature 4 working')

# class C(A,B):     ##sub class/ child class
#     def feature3(self):
#         print('feature 5 working') 

#     def feature4(self):
#         print('feature 6 working')

##heirarichal inheritance-----
# class A:        ##super class/ parent class
#     def feature1(self):
#         print('feature 1 working') 

# class B(A):     ##sub class/ child class
#     def feature2(self):
#         print('feature 3 working') 

# class C(A):     ##sub class/ child class
#     def feature3(self):
#         print('feature 3 working') 

# objB = B()
# objC = C()
# objB.feature1()
# objC.feature1()







# in cpp if constructor of child class is called, it automatically calls the constructor of parent class
# in python child class constructor does not automatically calls constructor of parent class bur we can call that using super method --> super().__init__()
# we can even use super() to call method of parent class in child class

# # for single or multilevel inheritence-----
# class A:        ##super class/ parent class
#     def __init__(self):
#         print('constructor of class A')

#     def feature1(self):
#         print('feature 1 working') 

#     def feature2(self):
#         print('feature 2 working')

# class B(A):     ##sub class/ child class
#     def __init__(self):
#         super().__init__()
#         print('constructor of class B')

#     def feature3(self):
#         print('feature 3 working') 

#     def feature4(self):
#         print('feature 4 working')

# a=B()




# # for multiple inheritence-----
# class A:        ##super class/ parent class
#     def __init__(self):
#         print('constructor of class A')
    
#     def extra(self):
#         print('extra function from class A')

# class B:     ##sub class/ child class
#     def __init__(self):
#         print('constructor of class B')
    
#     def extra(self):
#         print('extra function from class B')

# class C(B,A):     ##sub class/ child class
#     def __init__(self):
#         super().__init__()
#         print('by using class name:-')
#         A.__init__(self)
#         B.__init__(self)
#         print('constructor of class C')

#     # using super method to call parent class methods
#     def callfun(self):
#         super().extra()
#         A.extra(self)
#         B.extra(self)

# obj=C()
# print('calling extra function from main:-')
# A.__init__(obj)
# B.__init__(obj)
# print('calling extra function from function of class C:-')
# obj.callfun()
# class C(A,B)-->first it will call the constructor of class A then itself
# class C(B,A)-->first it will call the constructor of class B then itself
# class which it is inheriting first it will call only that class's contructor it is called MRO(method resolution order) if we use super keyword
# while we can use classname.__init__(self) to specifically call the contructor of which ever class we want
# ,,even of that class too that is inherited later
# it also works for methods if we have function of same name in two parent classes then it will call only method of first inheriting class
# MRO depends upon the way, names of base classes are written as a list for inheritance in subclass

# how to get mro:--->
# print(classname.mro())        # ---> returns in tuple format
# print(classname.__mro__)        # ---> returns in list format
# print(help(classname))





#### calling base class constructor to get data from user
# class edu:
#     def __init__(self):
#         self.a=input('enter marks of 12th = ')
#         self.b=input('enter marks of graduation = ')
# class job(edu):
#     def __init__(self):
#         super().__init__()
#         self.company=input('enter the name of company = ')
#         self.designation=input('enter your job designation = ')
#     def show(self):
#         print(f'{self.a}\n{self.b}\n{self.company}\n{self.designation}')

# obj = job()
# obj.show()


#### sending data to the base class
# class edu:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# class job(edu):
#     def __init__(self,m1,m2,company,designation):
#         super().__init__(m1,m2)
#         self.company=company
#         self.designation=designation
#     def show(self):
#         print(f'{self.a}\n{self.b}\n{self.company}\n{self.designation}')

# obj = job(74,83,'google','python dev')
# obj2 = edu(10,20)
# # obj.show()
# # print(help(job))    ## it tells us the mro
# # print(isinstance(obj,job))     # tells whether it is object of given class (True / False)
# # print(isinstance(obj,edu))
# # print(isinstance(obj2,edu))
# # print(isinstance(obj2,job))
# print(issubclass(job,edu))      # tells whether first class is subclass of second class








########  inheritance and variables #######
# class A:
#     x=10

# class B(A):
#     def __init__(self):
#         self.x=100
#     def show(self):
#         return (self.x)
#     @classmethod
#     def show1(cls):
#         return cls.x

# class C(A):
#     def __init__(self):
#         self.x=200
#     def show(self):
#         return (self.x)
#     @classmethod
#     def show1(cls):
#         return cls.x

# class D(B,C):
#     def __init__(self):
#         print(f"by class D init : {self.x}")
#     @classmethod
#     def show2(cls):
#         return(f"by class D show2 : {cls.x}")


# objB = B()
# print(objB.x)
# print(objB.show())
# print(objB.show1())
# objC = C()
# print(objC.x)
# print(objB.show())
# print(objC.show1())
# objD = D()
# print(objD.show2())






# class school:
#   __x=10
#   def __init__(self,num):
#     self.num=num

# class students(school):
#   def __init__(self, num):
#     super().__init__(num)

#   def show(self):
#     print(self._school__x)
#     print(self.num)
  
#   @classmethod
#   def show1(cls):
#     print(cls._school__x)
  
# obj = students(100)
# obj.show()
# obj.show1()