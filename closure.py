# # setting function to a new variable
# def square(a):
#     return a**2

# s = square
# # both are same
# print(s)
# print(square)






###################passing function as an argument#################

# # making our own map function-----
# def square(a):
#     return a**2
# l=[1,2,3,4]

# # without list comprehension-----
# def my_map(func,l):
#     new_list=[]
#     for i in l:
#         new_list.append(func(i))
#     return new_list
# # with list comprehension-----
# def my_map2(func,l):
#     return [func(i) for i in l]

# # passing predefined function to a userdefined map function-----
# print(my_map(square,l))
# # passing user defined function to a userdefined map function-----
# print(my_map(lambda a : a**3,l))









# using predefined map functions-----
# l=[1,2,3,4]
# print(list(map(lambda a : a**2,l)))












############################returning function#################
# def outer_func1():
#     def inner_func():
#         print('inside inner function')
#     return inner_func()

# def outer_func2():
#     def inner_func():
#         print('inside inner function')
#     return inner_func

# # printing result of inner_func inside outer_func1()
# outer_func1()
# #making vaiable of of inner_func inside outer_func1()
# var1 = outer_func1
# var1()

# # no result coz name of inner_fun() inside outer_func2() is passed
# outer_func2()
# #making vaiable of of inner_func inside outer_func1()
# var2 = outer_func2()
# var2()











############example of passing and returning function##############
# def outer_fun1():
#     def inner_fun1():
#         return 'hello every1'
#     return inner_fun1

# def outer_fun2(msg):
#     def inner_fun2():
#         print(f'message is {msg}')
#     return inner_fun2

# (outer_fun2((outer_fun1())()))()







def outer(x):
    def inner(n):
        print(x**n)
    return inner

# var = outer(5)
# var(2)
        ###or##
(outer(5))(2)