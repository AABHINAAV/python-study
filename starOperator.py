# def fun(a,b):
#     print(a+b)
# fun(1,2,3,4)
#this function of taking only 2 parameters but we are passing more than 2 arguments so it will raise an error

# but we can solve this problem using *args
# it is passed as an argument it converts the parameters into the tuple

# def fun(*args):
#     print(args)
#     print(type(args))
#     total=0
#     for i in args:
#         total=total+i
#     print(total)
#     print(type(total))
# fun(1,2,3,4)

# we can use any variable instead of args on function parametric list but it is convention to use args


# def fun(*args): ##-->it can hold empty tuple
#     print(args)
#     print(type(args))
# fun()


# def fun(num,*args):
#     print(args)
#     print(type(args))
#     print(num)
#     print(type(num))
# fun()
#########----->> *args simple creates a tuple of numbers passsed as argument list and tuple can be empty   but   a normal variable cannot be empty so that will raise an error


# def fun(*args , num):
#     print(args)
#     print(type(args))
#     total=0
#     for i in args:
#         total=total+i
#     print(total)
#     print(type(total))
# fun(1,2,3,4)
##########------>>*args must be used in the end of parametric list
##-->>it is same as rest operator of JS


# how to pass a list or tuple to function with *args that carries tuples
# def fun(*args):
#     total=0
#     for i in args:
#         total= total+ i
#     print(total)
# # num=[1,2,3,4,5]    ##or##
# num=(1,2,3,4,5)
# fun(*num)  ##--->> putting * unpacks list items



##making list of power numbers of a given number:---
# def fun(num,*args):
#     lst=[i**num for i in args]
#     print(lst)

# nums=input('enter comma seperates numbers=').split(',')
# nums=[int(i) for i in nums]
# pwr=int(input('enter power number='))
# fun(pwr,*nums)





#####################################
##########keyword argument###########
#####################################
# it is used as **kwargs
# acc. to convention it is called as kwargs
# it is double star operator

# it takes arguments of key-value pairs format
# and converts it into a dictionary

# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for i,j in kwargs.items():
#         print(f"{i} : {j}")
# fun(fname='Abhinav',lname='Garg',age=22)


# kwargs with normal argument
# that normal variable will work as simple argument i.e. it will hold only value not the keyname
# def fun(num,**kwargs):
#     print(num)
#     print(kwargs)
#     print(type(kwargs))
#     for i,j in kwargs.items():
#         print(f"{i} : {j}")
# fun(1234,fname='Abhinav',lname='Garg',age=22)



# passing dictionary as an argument by unpacking its elements:------------
# def fun(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i} : {j}")
# d={
#     'fname':'abhinav',
#     'lname':'garg',
#     'age':22
# }
# fun(**d)



#############
# star operator or *args and double star operator or **kwargs   both has same functioning that is taking multiple arguments 
# *args converts it into a tuple 
# **kwargs converts it into a dictionary
# while they work same with normal argument
# *args uses single * for list depacking
# **kwargs uses double * for dictionary depacking



################PARAMETRIC ORDER################
# def fun(normal parameter, *args, default parameter, **kwargs)
        # PADK
        # parameter
        # args
        # default parameter
        # kwargs

# def fun(age, *marks, total=100, **id):
#     print(f"age : {age}")
#     print(f"marks : {marks}")
#     print(total)
#     print(id)

# lst=[50,60,70,80]
# fun(22,*lst,90,fname='abhinav',lname='garg')
#         #########or#########
# fun(22,50,60,70,80,90,fname='abhinav',lname='garg')



##reversing the strings of a list and capitalizing its first alphabet
# def fun(*args):
#     lst=[]
#     for i in args:
#         lst.append(i[::-1].title())
#     return lst
#             #or##    
#     # return [names[::-1].title() for names in args]
# lst=['abhinav', 'jassi', 'nimisha', 'ankit']
# print(fun(*lst))





# def fun(l , **kwargs):
#     if kwargs.get('reverse_str') == True:
#         return [i[::-1].title() for i in l]
#     else:
#         return [i.title() for i in l]
# lst=['abhinav', 'jassi', 'nimisha', 'ankit']
# print(fun(lst,reverse_str=True))
# -----------------
#####here reverse_str is just a variable which we are using that we have to reverse the strings or not we can do the same with args like this:--
# -----------------
# def fun(l , *args):
#     if args[0] == True:
#         return [i[::-1].title() for i in l]
#     else:
#         return [i.title() for i in l]
# lst=['abhinav', 'jassi', 'nimisha', 'ankit']
# print(fun(lst,True))