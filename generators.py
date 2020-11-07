# list,tuple,set,dict is iterable 
    # they take more memory coz when they are called in any for loop all data items are
    # taken and converted into list all together and stored in memory
    # they can be iterated more than once
    # filter returns iterable object

# generators are iterator
    # they take less memory coz when they are called in any for loop only one data items 
    # goes into it at a time so it saves memory
    # they can be iterated only once
    # map function returns iterator object




# if we define all values one by one within () then , it creates a tuple
    # t=(1,2,3,4,5)
# if we define all values within () with loop or function then , it creates a generator 
    # t=(i for i in range(10000))


# range() is a generator that's why it is fast and memory efficient


# two ways to create a generator:
    # 1) generator function
    # 2) generator comprehension





# def nums(n):
#     for i in range(1,n+1):
#         # yield(i)  ##or
#         yield i

# # for number in nums(10):
# #     print(number)

# number = nums(10)       ## yha pr generate ho rhi hai
# for i in number:        ## yha use kr k memory khali kr di
#     print(i)
# for i in number:        ## memory khali h so no output
#     print(i)

# for i in nums(10):      ## yha fir se generate kr rhe hai and next line me khali kr diya so we get output
#     print(i)













################generator comprehension################
# it is generated using list comprehension, but using () instead of []
# square = (i**2 for i in range(1,11))
# print(square)
# for num in square:
#     print(num)
# for num in square:
#     print(num)




# import time
# ls_time1=time.time()
# ls = [i**2 for i in range(10000000)]
# ls_time2=time.time()
# print(f"time for list creation : {ls_time2 - ls_time1}")

# gen_time1=time.time()
# gen = (i**2 for i in range(10000000))
# print(type(gen))
# t=(i for i in range(10))
# print(type(t))
# gen_time2=time.time()
# print(f"time for generator creation : {gen_time2 - gen_time1}")




# fibonacci series with generator-----
# def fibo(num):
#     a=0
#     yield a
#     b=1
#     yield b
#     for i in range(3,num+1):
#         c=a+b
#         yield c
#         a=b
#         b=c

# num = int(input('enter the number = '))
# fibSrs = fibo(num)
# for i in fibSrs:
#     print(i)



# factorial with generator-----
def fact(num):
    res = 1
    for i in range(1,num+1):
        res *= i
    yield res

num = int(input('enter the number = '))
res = fact(num)
for i in res:
    print(i)