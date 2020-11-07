# sum of digits:-
# num=int(input("enter the number="))
# sum=0
# while num>0:
#     temp=num%10
#     sum+=temp
#     num=num//10
# print(f"sum={sum}")

# name=input("sdf=")
# sum=0
# for i in range(0,len(name)):
# for i in name:
# sum+=int(i)
# print(i)
# print(sum)


# odd or even number:-
# def fun(num):
#     return num%2==0
# print(fun(11))


# def fun(a,b):
#     if a>b:
#         return "first number"
#     elif a<b:
#         return "second number"
#     return "equal"
# print(fun(2,2))


# def fun(a,b,c):
#     if a>b:
#         if a>c:
#             return a
#         return c
#     else:
#         if b>c:
#             return b
#         return c
# print(fun(3,5,1))


# def big(a,b):
#     if a>b:
#         return a
#     return b

# def fun(a,b,c):
#     x=big(a,b)
# return big(x,c)
####or####
# def fun(a,b,c):
#     return big(big(a,b),c)

# def fun(a,b,c):
#     return (a>b)?((a>c)?a:c):((b>c)?b:c)
# print(fun(10,20,30))


####string pallindrome or not####
# def fun(name):
#     if(name==name[::-1]):
#         return "pallindrome"
#     return "not pallindrome"
####or####
# def fun(name):
#     x=0
#     for i in range((len(name)//2)):
#         if name[i]==name[-i-1]:
#             x+=1
#     if x==0:
#         return 'false'
#     else:
#         return 'true'
####or####
# def fun(name):
#     return name==name[::-1]

# name=input("enter your name= ")
# print(fun(name))


# fibonacci series:-
# a=0
# b=1
# num=int(input("enter size= "))
# if(num==1):
#     print(a)
# elif num==2:
#     print(f"{a} {b}")
# else:
#     print(f"{a} {b}",end=" ")
#     for i in range(num-2):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c


# global keyword gives the access of outer most variable
# x=10                #global variable declaration and initialisation
# print(x)
# def fun():
#     x=20            #local variable declaration and initialisation
#     print(x)
# fun()
# print(x)            #accessing global vairable


# x=10                #global variable declaration and initialisation
# print(x)
# def fun():
#     global x        #taking access to change global variable
#     x+=20            #global variable
#     print(x)
# fun()
# print(x)


# x=10                      # global variable
# print(x)                  # printing global variable
# def a():
#     x=20                  # creating local variable
#     print(x)              # printing local variable
#     def b():
#         global x          # tacking access of global var
#         print(x)           # printing global var
#         x=100             # changing globa var
#         print(x)          # changing global var with new value
#     b()
#     print(x)              # printing local var
# a()
# print(x)                  # printing global var with new val


# if(print('hello world')):
#     pass


import random
num = random.random()
print(num)