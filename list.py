# ordered collention
# comsumes more memory
# mutable
# dynamic
# slow


# creating
# len()
# append()
# extend()
# join()
# sort()
# reverse()
# clear()
# index()
# insert()
# count()
# remove()
# pop()
# min()
# max()
# copy()
# _add_()
# _sizeof_()

############################################################################

# creating list-----
# lst=list(i for i in range(1,11))
# print(lst)

# len()
# it returns the lenght of list or no. of items in the list
# lst=list(i for i in range(1,11))
# print(len(lst))

# append-----
# it adds a list/tuple/set as a list-----
# it adds single value as a list item-----
# lst=list(i for i in range(1,11))
# print(lst)
# lst.append([1,2,3,4])
# lst.append(100)
# print(lst)

# extend
# it extends values only string values but not integer values-----
# if there are multiple values in list/tuple/set it adds them to the list as it is
# if single string is given to extend to list it adds its characters one by one-----
# lst=list(i for i in range(1,11))
# print(lst)
# lst.extend(['1','2','3','4','abhi'])
# lst.extend('100')
# print(lst)

#join()
# it joins all list items as string with a given string in btw them
# lst=['abhi','nanu','jassi']
# x=' and '.join(lst)
# print(x)

# sort()
# tim sort algorithm is used in sort method of list
# this function returns nothing 
# it sorts list items in ascending order-----
# sort(reverse=True)
# it sorts list items in descending order-----
# lst=list(i for i in range(11,1,-1))
# print(lst.sort())
# print(lst)
# fruits=['mango','apple','banana','grapes']
# fruits.sort()
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)

# reverse()
# it reverses the list
# it returns none
# lst=list(i for i in range(1,11))
# print(lst.reverse())
# print(lst)

# clear()
# it clears the list
# it returns none
# lst=list(i for i in range(1,11))
# print(lst.clear())
# print(lst)

# index()
# it returns the index number of value if present in list otherwise error-----
# lst=list(i for i in range(1,11))
# print(lst.index(4))

# insert
# it returns nothing
# it adds item at given index position and rest are shifted backward-----
# lst=list(i for i in range(1,11))
# print(lst)
# print(lst.insert(4,100))
# print(lst)

# count()
# it reutrns the number of times a values is present in a list-----
# for this function 1 and 1.0 are same
# lst=list(i for i in range(1,11))
# print(lst.count(3))

# remove()
# it returns none
# it removes the given value from list if present otherwise returns error
# lst=list(i for i in range(1,11))
# print(lst.remove(5))
# print(lst)

# pop()
# it returns last item of list
# it pops the last item from list
# it can index number as an argument and pops that specific item
# lst=list(i for i in range(1,11))
# print(lst.pop())
# print(lst)
# print(lst.pop(7))
# print(lst)

# max --> it returns the maximum value 
# min --> it returns the minimum value 
# min() and max() accepts the list/tuple/set variable name
# they work only for integer but not for strings
# lst=list(i for i in range(1,11))
# print(max(lst))
# print(min(lst))

# copy()
# deep copy 
# it copies only data but not whole variable
# lst=list(i for i in range(1,11))
# l1=lst
# l2=lst.copy()
# l1.append(10000)
# print(lst)
# print(l1)
# print(l2)


# _add_()
# it returns the concatenation of two lists-----
# lst=list(i for i in range(1,6))
# l1=list(i for i in range(10,16))
# print(lst.__add__(l1))
# print(lst)

# _sizeof_()
# it returns the size of variable
# lst=list(i for i in range(1,111))
# print(lst.__sizeof__())
# x=10
# y=10000000
# print(x.__sizeof__())
# print(y.__sizeof__())


#############################################################################

# square of all list items
# def fun(l):
#     sqr=[]
#     for i in l:
#         sqr.append(i**2)
#     return sqr
# l=list(range(1,6))
# print(fun(l))


# reversing the list
# def fun(l):
# rev=[]
# for i in l:
#     rev.insert(0,i)
# return rev
####or####
# l.reverse()
# return l
####or####
# return l[::-1]
####or####
# rev=[]
# for i in range(len(l)):
#     rev.append(l.pop())
# return rev

# l=list(range(1,10))
# print(fun(l))




# reversing the string items in a list
# def fun(l):
# for i in l:
#     l[l.index(i)]=i[::-1]
# return l
####or####
# rev=[]
# for i in l:
#     rev.append(i[::-1])
# return rev

# l=['abc','xyz','pqr']
# print(fun(l))






# seperating odd and even numbers in different lists
# def fun(l):
#     odd=[]
#     even=[]
#     for i in l:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     l.clear()
#     l.append(odd)
#     l.append(even)
#         ##or###
#     # l=[odd,even]
#     return l

# l=list(range(1,11))
# print(fun(l))







# writing out common items of two lists
# res=[]
# for i in l1:
#     if i in l2:
#         res.append(i)
# return res

# l1=[1,2,5,8]
# l2=[1,2,7,6]
# print(fun(l1,l2))





# predefined datatype in python:-
# int
# float
# str






# there are two types of lists-----
#### 1) 2d list-----all its inner lists are of same lenght
                    # lst=[[1,2,3],[100,200,300],[10,20,30]]
#### 2) ragged list-----all its inner lists are of different lenght
                    # lst=[[1,2,3][10],[100,200]]






# creating user defines multidimensional list-----
# rows=int(input('enter the number of rows = '))
# columns=int(input('enter the number of columns ='))
# lst=[]
# for i in range(rows):
#         temp=[]
#         for j in range(columns):
#                 listItem=input('enter the number = ')
#                 temp.extend(listItem)
#         lst.append(temp)
# print(lst)







#### an unindexed list has length 0
        #we can put elements into it only by append() and _add_()----
        #by simple element putting method we will get an index out of range error-----
# lst=[]
# lst[0]=1
# lst[1]=2
# lst[2]=3
# print(lst)






# nested list-----
# x=[1,2,3]
# y=[10,20,x]
# z=[100,200,y]
# print(z)
# print(z[1])         #200
# print(z[2][1])      #20
# print(z[2][2][1])   #1








# returning the number of lists in a given list
# def fun(l):
#     count=0
#     for i in l:
#         if type(i)==list:
#             count+=1
#     return count
# l=[1,2,3,4,5,[1,2,3],['a','b','abhi'],['a','b',1,2.3,'abih']]
# print(f"number of lists in \n{l}\nare:-\n{fun(l)}")
# print(len(l))







####list unpacking 1####
# it requires the same number of variables as the number of list items
# lst=[1,2,3]
# n1,n2,n3=lst
# print(n1)
# print(n2)
# print(n3)






# list unpacking- 2----
# lst=[[1,2,3],[1,2,3],[1,2,3]]
# for i,j,k in lst:
#     print(i)
#     print(j)
#     print(k)







###########list comperhensions########
# list with square of numbers:-------
# lst=[]
# for i in range(1,11):
#     lst.append(i**2)
# print(lst)
###or####
# lst=[i**2 for i in range(1,11)]
# print(lst)




# list with negative numbers:-------
# lst=[-i for i in range(1,11)]
# print(lst)




# list with reverse of each list items:------
# lst1=['abhinav','ankit','nimisha','jaspal','monika']
# lst2=[i[::-1] for i in lst1]
# print(lst2)
#########or########
# def fun(lst1):
#     lst2=[wrd[::-1] for wrd in lst1]
#     return lst2
# lst=['abhinav','ankit','nimisha','jaspal','monika']
# print(fun(lst))





# list comprehension using if condition:--------
# list holding even numbers:-------
# lst=[]
# for i in range(1,11):
#     if i%2==0:
#        lst.append(i)
# print(lst)
#             ##########or##########
# even_lst=[i for i in range(1,11) if i%2==0]
# print(even_lst)
# odd_lst=[i for i in range(1,11) if i%2 != 0]
# print(odd_lst)





# list comprehension with if-else condition:---------
# lst=list(range(1,11))
# new_lst=[i**2 if i%2==0 else -i for i in lst]
# print(new_lst)




# nested list comprehension:----------
# lst=[[i for i in range(1,4)] for j in range(3)]
# print(lst)

# lst=[tuple(i for i in range(1,4)) for j in range(3)]
# print(lst)





# lst1=[['a',11],['b',12],['c',13]]
# lst2=[num for txt,num in lst1 if txt=='b' or txt=='c']
# print(lst2)






# lst=[]
# for i in range(5,10):
#     if i>7:
#         for j in range(2,5):
#             if j>3:
#                 lst.append(i*j)
# print(lst)
#####or#####
# lst=[i*j for i in range(5,10) if i>7 for j in range(2,5) if j>3]
# print(lst)
