# syntax error

# indentation error

# name error ---> using an undefined variable

# type error ---> print(5 + 'a')  ---> wrong operation performed on wrong data type

# index error ---> l=[1,2,3]
#                    print(l[4])----> list index out of range

# value error ---> when dataype is correct but we type wrong value
#                   s='5'
#                   print(int(s)) ===> correct
#                   but
#                   s='a'
#                   print(int(s)) ===> error

# attribute error ---> when we use such a attribute or function on an object that is not pre-present
#                   l=[1,2,3]
#                   l.push(5) ===> no push method present in list

# key error ---> calling value of a key that is not present
#                   d={'name':'abhi'}
#                   print(d['age'])


# def add(a,b):
#     if((type(a) is int) and (type(b) is int)):
#         return a+b
#     raise TypeError('sldjfla')

# print(add(1,2.3))


# a function which has no implementation is called abstract method
# it is not present in python
# so simply a method that is raising NotImplementedError,,is needed to be overloaded in its subclasses
# such a method is working like abstract method in python
# class animals:
#     def sound(self):
#         raise NotImplementedError('sub class should have its own sound method')
# class cat(animals):
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         return 'meow meow'
# class dog(animals):
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         return 'bhow bhow'
# obj1=cat('meowth')
# print(obj1.sound())
# obj2=dog('blacky')
# print(obj2.sound())








# while True:
#     try:
#         age = int(input('enter your age = '))
#     except ValueError:
#         print('value error present')
#     except TypeError:
#         print('type error present')
#     except:
#         print('invalid input....')
#     else:
#         if age > 18:
#             print('you can play')
#         else:
#             print('you cannot play')
#         break
#     finally:
#         print(f'finally block.....')







# def divide(a,b):
#     try:
#         result=a/b
#     except ZeroDivisionError:
#         print('you divided by zero')
#     except TypeError:
#         print('one of the input is string, not a number')
#     except:
#         print('invalid input')
#     else:
#         print(f'result : {result}')
#     finally:
#         print('thank you for using our service')
# divide(1,0)
# divide(1,'1')
# divide(10,2)







######  custom exception  #####
class NameTooShort(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NameTooShort('name is too short')

name = input('enter your name = ')
validate(name)
print(f'input by user : {name}')