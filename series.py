# 1234567
# 123456
# 12345
# 1234
# 123
# 12
# 1
# for i in range(1,8):
#     for j in range(1,8-i+1):
#         print(j,end='')
#     print('')




# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000
# for i in range(4):
#     for j in range(9):
#         if i==j or j==4 or 8-i==j:
#             print('*',end="")
#         else:
#             print(0,end="")
#     print(f"\n")



# 5432*
# 543*1
# 54*21
# 5*321
# *4321
# num=int(input("enter number of rows= "))
# for i in range(1,num+1):
#     for j in range(num,0,-1):
#         if i==j:
#             print('*',end='')
#         else:
#             print(j,end="")
#     print("\n")




##swapping of two numbers
# x,y=10,20
# print(f"Before Swapping:-\nx={x}\ny={y}")
# x,y=y,x
# print(f"After Swapping:-\nx={x}\ny={y}")



#####counting the frequency of numbers in a list of numbers:---
# def fun(l):
#     d={}
#     for i in l:
#         d[i]=l.count(i)
#     return d
# num=input('enter the numbers = ').split(',')
# num=[int(i) for i in num]
# print(fun(num))




# *
# *1*
# *121*
# *12321*
# *121*
# *1*
# *
# num=int(input('enter the number of rows = '))
# print('*')
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         if j==1:
#             print('*',end='')
#         print(j,end='')
#     for j in range(i-1,0,-1):
#         print(j,end='')
#     print('*')
# for i in range(num-1,0,-1):
#     for j in range(1,i+1):
#         if j==1:
#             print('*',end='')
#         print(j,end='')
#     for j in range(i-1,0,-1):
#         print(j,end='')
#     print('*')
# print('*')



# enter the numbers list and make pairs that are equal to the subtraction of given number
# num=3 
# numbers=[5,4,6,7,9,8,1,17,14]
############output########
# (4 , 1),(7 , 4),(9 , 6),(8 , 5),(17 , 14)
# so number of results = 5
# numbers=input('enter comma seperated numbers = ').split(',')
# l=[int(i) for i in numbers]
# num=int(input('enter the number = '))
# count=0
# for i in l:
#     for j in l:
#         if i-j == num:
#             print(f"{i} : {j}")
#             count += 1
# print(f'so number of results = {count}')



#######number guessing game######
# import random
# choice1=input('shall we start the game (y/n) = ')
# count=1
# if choice1 == 'y':
#     num = random.randint(1,10)
#     while choice1=='y':
#         ans=int(input('enter the number of your choice = '))
#         if num==ans:
#             print(f'correct ans in {count} chances')
#             count=1
#             choice1=input('do you want to play again (y/n) = ')
#             num = random.randint(1,10)
#         else:
#             if ans>num:
#                 print('too high....try again')
#                 count +=1
#             else:
#                 print('too low......try again')
#                 count +=1


############o/p########
# enter then number of rows = 5
# ABCDEDCBA
# ABCD DCBA
# ABC   CBA
# AB     BA
# A       A
# #########program#########
# num=int(input("enter then number of rows = "))
# for i in range(1,num+1):
#     for j in range(65,65+num-i+1):
#         print(chr(j),end='')
#     if i==1:
#         for j in range(65+num-i-1,64,-1):
#             print(chr(j),end='')
#     else:
#         for j in range(0,(i*2)-3):
#             print(' ',end='')
#         for j in range(65+num-i,64,-1):
#             print(chr(j),end='')
#     print('')





##take string as input and remove every repeated character except for the lst even remove first one and print the resultant string as output
# enter your word = nextgencoder
# xtgncoder
# enter your word = hello
# helo
# enter your word = welcome
# wlcome
# word=input('enter your word = ')
# temp=''
# for i in word[::-1]:
#     if i not in temp:
#         temp = temp + i
# print(temp[::-1])



##returning the number of similar characters
# def fun(s1,s2):
#     count=0
#     temp=''
#     for i in s1:
#         if i not in temp:
#             temp=temp+i
#             if i in s2:
#                 count+=1
#     return count
# s1=input("enter the first string= ")
# s2=input("enter the second string= ")
# print(f"common number of characters= {fun(s1,s2)}")



# print(list(i for i in list(range(1,11)) if i%2==0))

# print(any(list(num%2==0 for num in list(range(1,11)))))



# finding the max among item pair of 2 lists
# l1=[1,3,5,7]
# l2=[2,2,6,4]
# res=[]
###  o/p -- [2, 3, 6, 7]
# #####old school:--
# # for i in zip(l1,l2):
# #     res.append(max(i))
# # print(res)
# #####comprehensed:--
# print(list(max(i) for i in zip(l1,l2)))



#####
#program to find the number of trailing zeros in factorial of a nummber
# def factorial(number):
#     if number==1 or number==0:
#         return 1
#     else:
#         return number * factorial(number-1)

# def trailingZerosInFactorial(number):
#     # 100! =100//5 + 100//(5*5)----
#     count=0
#     i=5
#     while number//i!=0:
#         count += number//i
#         i = i * 5
#     return count

# if __name__ == "__main__":
#     number=int(input('enter the number='))
#     fac=factorial(number)
#     print(fac)
#     print(trailingZerosInFactorial(number))




# take input as string and check if each is only once then duplicate it otherwise no need.....
# input       ----- ouput
# abhinav           abbhhiinnavv
# string = input('enter the string = ')
# res = []
# for i in string:
#     res.append(i)
#     if(string.count(i) == 1):
#         res.append(i)
# print(''.join(res))



# write a program which checks each string from a list and gives total number of upper case letters as output.....
# ['Next','Gen','Cooder']  ---> 3
# ['next','gen','cooder']  ---> 0
# ['Next',78,'Cooder']  ---> only alpha allowed
# ['NEXT','GEN','CODER']  ---> ALL
# import time
# start = time.time()
# lst = ['Next','Gen','Cooder']
# string = ''.join(lst)
# if string.isalpha():
#     if string.isupper(): print('all')
#     else:print(sum([1 if i.isupper() else 0 for i in string]))
# else: print('only alph allowed')
# end = time.time()
# print(start)
# print(end)
# print(end - start)





# enter the number of rows = 10
#          * 
#         * * * 
#        * * * * * 
#       * * * * * * * 
#      * * * * * * * * * 
#     * * * * * * * * * * * 
#    * * * * * * * * * * * * * 
#   * * * * * * * * * * * * * * * 
#  * * * * * * * * * * * * * * * * * 
# * * * * * * * * * * * * * * * * * * * 
# n=int(input('enter the number of rows = '))
# for i in range(1,n+1):
#     print(f'{" "*(n-i)}{"* "*(2*i-1)}')








# enter the number of rows = 10
#          A 
#         C C C 
#        E E E E E 
#       G G G G G G G 
#      I I I I I I I I I 
#     K K K K K K K K K K K 
#    M M M M M M M M M M M M M 
#   O O O O O O O O O O O O O O O 
#  Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q 
# S S S S S S S S S S S S S S S S S S S 
# n=int(input('enter the number of rows = '))
# for i in range(1,n+1):
#     print(f'{" "*(n-i)}{(str(chr(64+(2*i-1))+" "))*(2*i-1)}')








# enter the number of rows = 5
#      1 
#     1 2 3 
#    1 2 3 4 5 
#   1 2 3 4 5 6 7 
#  1 2 3 4 5 6 7 8 9 
# n=int(input('enter the number of rows = '))
# for i in range(0,n):
#     print(f"{' '*(n-i)}",end='')
#     for j in range(0,2*i+1):
#         print(j + 1,end=' ')
#     print()




# enter the number of rows = 5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# n=int(input('enter the number of rows = '))
# for i in range(1,n+1):
#     print(f"{' '*(n-i)}{'*'*(2*i-1)}")
# for i in range(n-1,0,-1):
#     print(f"{' '*(n-i)}{'*'*(2*i-1)}")








# import time
# x=time.localtime()
# print(x)
# print(type(x))

##### user defined switch case #####
# switch = {
#     0:'zero',
#     1:'one',
#     2:'two',
#     3:'three',
#     4:'four'
# }
# print(switch.get(0,'nothing'))
# print(switch.get(5,'nothing'))









# take input of list of numbers
# split them in two arrays such that sum of their numbers is least
# # # input ------
# [2,5,6,7,15,20] 
# # # output -----
# list 1 = [20, 5, 2]
# list 2 = [15, 7, 4]
# difference between lists = 1
# nums = [2,5,4,7,15,20]
# nums.sort()
# nums.reverse()
# lst1=[]
# lst2=[]
# lst1.append(nums[0])
# lst2.append(nums[1])
# for i in range(2,len(nums)):
#     if (sum(lst1) + nums[i]) > (sum(lst2) + nums[i]):
#         lst2.append(nums[i])
#     else: lst1.append(nums[i])

# print(f"list 1 = {lst1}")
# print(f"list 2 = {lst2}")
# print(f"difference between lists = {sum(lst1)-sum(lst2)}")






# enter the number of rows = 5
#     A 
#    A B A 
#   A B C A B 
#  A B C D A B C 
# A B C D E A B C D 
# n=int(input('enter the number of rows = '))
# for i in range(1,n+1):
#     print(f"{' '*(n-i)}",end='') 
#     for j in range(1,i+1):
#         print(f"{chr(64+j)} ",end='')
#     for j in range(1,i):
#         print(f"{chr(64+j)} ",end='')
#     print()






# enter the number of rows = 5
#     A 
#    A B A 
#   A B C B A 
#  A B C D C B A 
# A B C D E D C B A 
# n=int(input('enter the number of rows = '))
# for i in range(1,n+1):
#     print(f"{' '*(n-i)}",end='') 
#     for j in range(1,i+1):
#         print(f"{chr(64+j)} ",end='')
#     for j in range(i-1,0,-1):
#         print(f"{chr(64+j)} ",end='')
#     print()