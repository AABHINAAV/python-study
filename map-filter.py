# iterable ---> uses __iter__() or __getitem__() and produces the iterator
                # can be traversed many times
# iterator ---> uses __next__() and gets the next value
                # can be traversed only once


#########
# map function returns a map object 
# map objects are iterator 
# we can use loop on map objects only once
# they use __next() inside them



# without map function:--
# l=list(range(1,11))
# def fun(l):
#     return [i**2 for i in l]
# print(fun(l))

# with list comprehension and without map function:--
# l=list(range(1,11))
# print([i**2 for i in l])

##with map function:---
# syntax:----- map(function name , iterable name)
# l=list(range(1,11))
# def fun(num):
#     return num**2

# # res=list(map(fun,l))
# # print(res)
# ######or#########
# print(list(map(fun,l)))



# map function with lambda expression:---
# l=list(range(1,11))
# print(list(map(lambda num:num**2 , l)))



# l=list(range(1,11))
# def fun(num):
#     return num**2
# res = map(fun,l)
# for i in res:
#     print(i)
# for i in res:
#     print(i)        ##no output this time coz res is a map object and map objects can be iterated only once coz they are iterators

###professionals use map objects mostly with predefined function like 'len' and use list compreshension with lambda function for most of the other purposes

###map function with predefined function:---
# l=['abhinav','jassi','nimisha tulera','ankit']
# res = list(map(len,l))
# print(res)



# map function returns the result for a condition of all items
# filter function returns the items that satisfies the condition
# filter function returns an iterable object by default
# l=list(range(1,11))
# def fun(num):
#     return num%2==0
# res1=list(map(fun,l))

# for i,j in enumerate(res1):
#     if j==True:
#         print(l[i])  #map function
# res2=list(filter(fun,l))
# print(res2)       #filter function
# #filter function with lamda expression
# print(list(filter(lambda num:num%2==0,list(range(1,11)))))
# #list comprehension
# print([i for i in range(1,11) if i%2==0])


#####iterator vs iterable########
# numbers=[1,2,3,4]                       #iterables
# sqrs=map(lambda num:num**2 , numbers)   #iterators

# # this is how for loop works:--
# itr=iter(numbers)       #---> itr is iterator of iterable 'numbers'
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print('')
# print(next(sqrs))
# print(next(sqrs))
# print(next(sqrs))
# print(next(sqrs))




# if we use iterator then python will firstly convert them into iterables then use a loop on them
# while if we use iterables python weill do that for us






# #########  reduce ########## #
# from functools import reduce
# lst=[1,2,3,4]
# num=reduce(lambda x,y:x+y,lst)
# print(num)