# zipping same order lists
# l1=['a','b','c','d']
# l2=[1,2,3,4]
# print(zip(l1,l2))
# print(dict(zip(l1,l2)))
# print(tuple(zip(l1,l2)))
# print(list(zip(l1,l2)))

# l1=[1,2,3,4]
# l2=['abhi','jassi','nimisha','ankit']
# l3=['garg','rana','tulera','nautiyal']
# print(list(zip(l1,l2,l3)))
##we can convert the result of zip function into list, tuple or a dictionary
# if we are zipping only two lists then it is most preferred to convert into a dictionary and if there are more 2 lists then we convert into a tuple or list coz dict hold only two values at a time

# zipping different order lists
# l1=list(range(1,11))
# l2=['a','b','c','d']
# print(dict(zip(l1,l2)))







l=[(1,'a'),(2,'b'),(3,'c')]
# for i in l:
#     print(i)

#method 1:--
# d=dict(l)
# for i in d:
#     print(f"{i} : {d[i]}")

## method 2:--
# d=dict(l)
# for i,j in d.items():
#     print(f"{i} : {j}")

##method 3:-- * operator with zip
# print(zip(*l))          ## it actually generates an object that we need to convert to check the values it is holding
# print(list(zip(*l)))    #converting mixed list into tuple holding list

# l1,l2=list(zip(*l))     #list unpacking
# print(list(l1))         #converting tuple into list
# print(list(l2))





# l1=['a','b','c','d']
# l2=[1,2,3,4]
# for i in zip(l1,l2):
#     print(i)


### average of same position items of n number of lists
# def fun(*args):
#     average=[]
#     for pair in zip(*args):
#         if sum(pair)/len(pair)%2==0:
#             average.append(sum(pair)/len(pair))
#     return average
# print(fun([1,2,3],[4,5,6],[7,8,9]))

#####with lambda function
# average = lambda *args: [sum(pair)/len(pair) for pair in zip(*args) if (sum(pair)/len(pair))%2==0]
# print(average([1,2,3],[4,5,6],[7,8,9]))

# def fun(*args):
#     if sum(*args)/len(*args)%2==0:
#         return sum(*args)/len(*args) 
# print(list(map(fun,zip([1,2,3],[4,5,6],[7,8,9]))))
