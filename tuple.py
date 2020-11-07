########################
#########tuples#########
########################
# unordered collention
# comsumes less memory
# immutable
# static
# fast

##only two functions works with tuple :--
#1: index
#2: count


# fruits=('banana','mango','apple')
# print(type(fruits))
# print(fruits)
# print(sorted(fruits))
# fruits = fruits + (1,20)      # adding data to tuple
# print(fruits)

# tpl=(1,2,3,4.5,5.22342432424,'a','b',"abhinav",[1,2.233333,'A',"nimisha"])
# print(type(tpl))                        #type
# print(tpl)                              #printing tuple
# print(len(tpl))                         #tuple length
# print(tpl.count('a'))                   #count method
# print(tpl.index("abhinav"))             #index method
# print(tpl[::2])                         #tuple slicing
# x=tpl[4]                                #coping item value in a variable
# print(x)                    
# y=tpl                                   #copying whole tuple
# print(y)


#'tuple' object does not support item assignment
# x=tuple(range(1,11))
# print(x)
# print(x[3])
# x[3]='a'                                #invalid
# print(x)



#looping in tuples:--------
# tpl=tuple(range(1,11))
# for i in tpl:
#     print(i)
# i=0
# while i<len(tpl):
#     print(tpl[i])
#     i+=1





#tuple with one element:--------
# tpl1=(1)
# print(tpl1)
# print(type(tpl1))
# tpl2=('a')
# print(tpl2)
# print(type(tpl2))
# tpl3=("abdih")
# print(tpl3)
# print(type(tpl3))
# tpl4=(1,)
# print(tpl4)
# print(type(tpl4))
# tpl5=('a',)
# print(tpl5)
# print(type(tpl5))



#tuple without paranthesis:---------------
# cars='mclarane','ferrari','aston martin','koninsseg'
# print(cars)
# print(type(cars))
# num=1,2,3,4,5
# print(num)
# print(type(num))




#tuple unpacking:---------------
# tpl=(1,2,3,4,5)
# # num1,num2,num3,num4=tpl             #Error: too many values to unpack (expected 4)
# num1,num2,num3,num4,num5=tpl
# print(num1)


#list inside tuple:-------
# tpl=(list(range(1,11)),'abhi')
# print(tpl)
# print(type(tpl))
# print(tpl[1])
# print(tpl[0])
# tpl[0].pop()
# print(tpl[0])


#tuple functions:-----------------
# x=tuple(range(1,11))
# print(min(x))
# print(max(x))
# print(sum(x))



#function returning more than one value:--------
# def fun(x,y):
#     add=x+y
#     mul=x*y
#     return add,mul
# # print(fun(10,20))             ##returning two values as tuple items
# a,b=fun(10,20)                  ##unpacking returned tuple
# print(f"addition={a}\nmultiplication={b}")





##tuple, list and string conversions among them:-------
# tpl=tuple(range(1,11))
# print(tpl)
# print(type(tpl))
# lst=list(tpl)
# # lst=list(tuple(range(1,11)))        ##can do in that way too
# print(lst)
# print(type(lst))
# string=str(tpl)
# print(string)
# print(type(string))
# t1=tuple(lst)
# print(type(t1))
# t2=tuple(string)
# print(type(t2))