# decorators --> enhances the functionality of other functions

# def func1(any_function):
#     def wrapper_function():
#         print('this is function 1')
#         any_function()
#     return wrapper_function

# def func2():
#     print('this is function 2')

# (func1(func2))()


# @ --> is syntactic sugar which is like a shortcut used to make decorators run

# def func1(any_function):
#     def wrapper_function():
#         '''yo'''
#         print('this is function 1')
#         any_function()
#     return wrapper_function

# @func1
# def func2():
#     '''honey singh'''
#     print('this is function 2')

# func2()
# print(func2.__doc__)


# but if we pass an argument to func2() it will give error coz wrapper_func() does not takes any argument
# so its solution is passing *args and **kwargs
# and if we pass such a function that return a value instead of printing
# so we always return wrapper_function()
# it will return if it of return type otherwise only do the functionality
# now if we print the name and doc string of func2(), interpreter will print that of wrapper function
# so we use functool module

# from functools import wraps
# def func1(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args,**kwargs):
#         '''this is wrapper function'''
#         print('this is function 1')
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @func1
# def func2(x):
#     '''this is function 2'''
#     print(f'this is function 2 with argument {x}')

# # func2(100)

# @func1
# def func3(a,b):
#     return a+b

# # print(func3(10,20))
# print(func2.__doc__)
# print(func2.__name__)








# from functools import wraps
# def print_function_data(any_function):
#     @wraps(any_function)
#     def wrapper_func(*args,**kwargs):
#         '''doc string of wrapper function'''
#         print(f'msg from wrapper function of name : {any_function.__name__}')
#         print(f'doc string of wrapper function : {any_function.__doc__}')
#         return any_function(*args,**kwargs)
#     return wrapper_func

# @print_function_data
# def add(a,b):
#     '''this function is used to add two numbers'''
#     return a + b

# print(add(4,5))








# from functools import wraps
# def ony_int_allow(function):
#     @wraps(function)
#     def wrapper_func(*args,**kwargs):
#         # datatypes = []
#         # for arg in args:
#         #     datatypes.append(type(arg) == int)
#         # if all(datatypes):
#         #     print('yes')
#         #     return function(*args,**kwargs)
#         # else:
#         #     print('invalid arguments')
#             ##or###
#         if all([type(arg)==int for arg in args]):
#             print('yes')
#             return function(*args,**kwargs)
#         print('invalid arguments')

#     return wrapper_func

# @ony_int_allow
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_all(1,2,3,4))
# print(add_all(1,2,3,4,[10,20]))








##############  decorator with argumenst  ##########
# from functools import wraps
# def only_data_type_allow(data_type):
#     def decorator(function):
#         @wraps(function)
#         def wrapper_func(*args,**kwargs):
#             if all([type(arg)==data_type for arg in args]):
#                 return function(*args,**kwargs)
#             print('invalid argument')
#         return wrapper_func
#     return decorator

# @only_data_type_allow(str)
# def string_join(*args):
#     string =''
#     for i in args:
#         string+=i
#     return string

# print(string_join('abhinav','garg'))

# @only_data_type_allow(int)
# def list_sum(*args):
#     string =0
#     for i in args:
#         string+=i
#     return string
# print(list_sum(1,2,3,4))
