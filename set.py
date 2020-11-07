##it is unordered collection of unique items
##we can only store number and strings in it
##we cannot store a list, tuple or dictionary.
##for a set 1 and 1.0 are same it keeps only 1 not 1.0

# copy()
# sorted()
# add()
# pop()
# remove()
# discard()
# intersection --> &
# union --> |
# difference --> -
# symmetric difference --> ^

# s=set(range(1,11))
##cleat()========
# it returns none
# it empties the set
# print(s.clear())
# print(s)

##copy()=========
# it cretes a copy of same value i.e. deep copy
# duplicate1=s
# dulplicate2=s.copy()
# duplicate1.clear()
# print(s)
# print(duplicate1)
# print(dulplicate2)

##sorted()========
# it sorts the value of set items
# it returns the list of sorted set items
# fruits={'banana','mango','apple'}
# print(sorted(fruits))
# print(sorted(fruits,reverse=True))

##add()==========
# it adds the only value at a time, which is given as an argument to the targetted set
# it returns nothing
# print(s.add('100'))
# print(s)

##pop()=========
# by deafult in set it pops out first item in casse of set
# it takes no argument
# it returns the popped out item
# print(s.pop())
# print(s)

##remove()======
# it removes the value from set which is passed as an argument
# it returns nothing
# it gives error if no such value present in set
# print(s.remove(4))
# print(s)
# s.remove(50)  ##error

##discard()=======
# it removes the value from set which is passed as an argument
# it returns nothing
# it do nothing if no such value present in set
# print(s.discard(4))
# print(s)
# s.discard(50)

###################################################################3
s1=set(range(1,8))
s2=set(range(5,11))
##set intersection=======
# it returns a set that contains the intersection values
# print(s1 & s2)

##set union==============
# it returns a set that contains the union value
# print(s1 | s2)

##set difference========
# it returns a set that contains values that are only in first set
# print(s1-s2)

##symmetric difference=====
# it returns a set that contains values that are either in first set or in second set but not in both
# print(s1 ^ s2)











# s1={7,11,99,22,12,1,2,3,4,5,1,2,3,4,5}
# print(s1)

# s2={'ankit','abhinav','nimisha','jaspal',1,2,1.1233}
# print(s2)

##how to make a list hold unique data only just like a set:--
# s=[2,4,2,5,8,5,3,6,8,4,2,5,6,4,6,7,8,5,2,4]
# s=list(set(s))
# print(s)


# s={1,6,2,26,8,3,1,2,3,26}
# s.add('sexy')
# s.add(5)
# s.add(5)
# s.remove(26)
# s.remove(22)    #-------------->raises error
# s.discard('22')    #------------->no error
# print(s)
# s.clear()
# print(s)


# s=set(i for i in range(1,11))
# print('original set :- ')
# print(s)
# s1=s
# s2=s.copy()
# s1.add(100000)

# print('original set after :-')
# print(s)
# print('shallow copy :-')
# print(s1)
# print('deep copy :-')
# print(s2)



# s=set(range(10,110,10))
# for i in s:
#     print(i)

# if 100 in s:
#     print('yes')
# else:
#     print('no')



# s1=set(range(10,50,10))
# s2=set(range(40,80,10))
# s3=s1|s2
# print(f'union={s3}')
# s4=s1&s2
# print(f'intersection={s4}')


#########set comprehension############
##it is used very less
# s={i**2 for i in range(1,11)}
# print(s)

# names=['abhinav','jaspal','ankit','nimisha']
# s={i[0] for i in names}
# print(s)