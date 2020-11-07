# dick typing-----
# passing different values to the object, typically changes its behaviour
# class A:
#     def fun(self):
#         print('class A')
# class B:
#     def fun(self):
#         print('class B')
# class C:
#     def doit(self,obj):
#         obj.fun()
# obj1=C()
# obj2=B()
# obj1.doit(obj2)
# obj2=A()
# obj1.doit(obj2)


##############operator overloading##############
# print(10 + 20)
# print('a' + 'b')
# internal working or second way o write all this:-
# a=10
# b=20
# print(int.__add__(a,b))
# s1='a'
# s2='b'
# print(str.__add__(s1,s2))
# behind the scene they call these functions-----
# + --> __add__()
# - --> __sub__()
# * --> __mul__()
# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2

#     def __add__(self,other):
#         m1=self.m1 + other.m1
#         m2=self.m2 + other.m2
#         s3=student(m1,m2)
#         return s3

#     def __sub__(self,other):
#         s3.m1=self.m1 - other.m1
#         s3.m2=self.m2 - other.m2
#         return s3

#     def __gt__(self, other):
#         s1 =self.m1 + other.m1
#         s2=self.m2+other.m2
#         if s1 > s2:
#             return True
#         else:
#             return False

#     def __str__(self):
#         return (f"{self.m1} : {self.m2}")

# s1=student(10,20)
# s2=student(50,60)
# s3= s1+s2                       ## student.__add__(s1,s2)
# s3=s1=s2                        ## student.__sub__(s1,s2)
# print(s3.m1)
# if s1 > s2:
#     print('s1')
# else:
#     print('s2')

# # giving same o/p
# # module name
# # class name
# # object address
# print(s1)
# print(s1.__str__())


#########method overloading###########
# python does not have method overloading
# but I can do it with basic knowledge ----->
# class student:
#     def total(self,*args):
#         sum=0
#         for i in range(len(args) + 1):
#             sum = sum + i
#         print(sum)

# obj=student()
# obj.total(1,2,3,4)
# obj.total(1,2,3,4,5)
# obj.total(1,2,3,4,5,6)


############method overriding##############
# it checks in current class first 
# if that method is not present in child class then only it will for that method in parent class
# class A:
#     def show(self):
#         print('class A')

# class B(A):
#     def show(self):
#         print('class B')

# obj=B()
# obj.show()
