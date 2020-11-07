##############################
#########dictionaries#########
##############################
# creating
# clear()
# copy()
# update()
# fromkeys()
# items()
# keys()
# values()
# get()
# popitem()
# pop()

# sorted()

###################################################################33

##creating technique 1:---------professional way
# x={'name':'abhinav','age':22}
# print(x)

##creating technique 2:---------unprofessional way
# x=dict(name='abhinav',age=22)
# print(x)
# print(type(x))

person={
    'name':'abhinav',
    'age':22,
    'gender':'male',
    'address':{
        'hno':76,
        'colony':'vasant vihar',
        'city':'haridwar',
        'state':'uttarakhand'
    },
    'marks':list(range(50,110,10)),
    'previous-marks':tuple(range(10,60,10))
}

##clear==============
# it removes everything from targetted dictionary and makes it empty
# it returns none
# print(person.clear())
# print(person)

##copy==============
# it makes as deep copy
# duplicate1 = person
# duplicate2 = person.copy()
# duplicate1['package']='60 lakh'
# print(duplicate1)
# print(person)
# print(duplicate2)

##update=============
# it takes a dictionary as an argument and updates the values of targetted dictionary
# if such values of new dictionary are not present in targetted dictionary then it adds those key value pair to it
# it returns nothing
# extra ={
#         'age':23,
#         'package':'60 lakh'
# }               ###age is updated and package is added
# print(person.update(extra))
# print(person)

##fromkeys()============
# it creates and returns the dictionary
# we can give key names and a value that will be set to all those keys
# print(person.fromkeys(['age','name'],'unknown'))
#                 ##or##
# person2 = dict.fromkeys(['age','name'],'unknown')
# print(person2)

##items()==============
# it returns list of tuples containing key and value
# print(person.items())
# for i,j in person.items():
#         print(f"{i}  :  {j}")

##keys()===============
# it returns list of keys of dictionary
# print(person.keys())

##values()==============
# it returns the list of values of each key of dictionary
# print(person.values())

##get()================
# it is used to get the value of specific key
# if that key is not present then o/p will be none
# we can even give user defined o/p if key is not present
# print(person.get('name'))
# print(person.get('status'))     #as it no such key in dictionary so output will be 'none'
# print(person.get('status','no such key present'))       #user defines output if key is not present

##popitem()============
# it pop out the last key value pair and returns the value
# print(person.popitem())
# print(person)

##pop()================
# it takes one key name as as argument and deletes that key value pair 
# it returns the value of deleted key
# print(person.pop('name'))
# print(person)

# del =============
# it can be used to delete the specific key value pair by specifying key 
# print(person)
# del person['gender']
# print(person)

# sorted()=============
# sort() is not present in dictionay just like list
# it is used to sort many dictionaries
# students = [
#     {'name': 'abhinav', 'age': 22},
#     {'name': 'jassi', 'age': 23},
#     {'name': 'ankit', 'age': 25}
# ]
# print(sorted(students,key=lambda item:item['age']))
# print(sorted(students,key=lambda item:item['age'], reverse = True))
# students={
#     'abhinav':{'age':22,'lname':'garg'},
#     'jaspal':{'age':23,'lname':'rana'},
#     'ankit':{'age':25,'lname':'nautiyal'}
# }
# print(sorted(students,key=lambda item:students[item]['age']))






# person={
#     'name':'abhinav',
#     'age':22,
#     'gender':'male',
#     'address':{
#         'hno':76,
#         'colony':'vasant vihar',
#         'city':'haridwar',
#         'state':'uttarakhand'
#     },
#     'marks':list(range(50,110,10)),
#     'previous-marks':tuple(range(10,60,10))
# }
# ##accessing data of a dictionary:----
# print(person)
# print(f"type of 'name'={type(person['name'])}")
# print(f'type of "gender"={type(person["age"])}')
# print(f'type of "address"={type(person["address"])}')
# print(f'type of "marks"={type(person["marks"])}')
# print(f'type of "pervious-marks"={person["previous-marks"]}')
# print(f"data of 'name'={person['name']}")
# print(f"data of 'age'={person['age']}")
# print(f"data inside address={person['address']['hno']}")
# print(f"data inside marks={person['marks'][2]}")
# print(f"data inside previous-marks={person['previous-marks'][4]}")

# ##adding data to already created dictionary:--
# person['looks']='sexy'        ##adding string
# person['height']=174          ##adding numeric
# person['fav movies']=['asd','sdfa']   ##adding list
# person['tpl']=[1,2,3]                 ##adding tuple
# person['fav']={'first':'a',             ##adding dict
#                 'second':'b'}
# print(f"\n\nafter adding data:-\n{person}")


# ##updating values of existing keys in dictionary:-------
#dict_name['key_name']='new_value'

##update method:-----------
#it is used to add the key value pairs from a dictionary to targetteg dictionary
#if we give new value to the already present key it updates its to hold the new value
# fav={
#     'first':'a',
#     'second':123,
#     'third':['x','xx','xxx'],
#     'fourth':('a','aa','aaa'),
#     'fifth':{
#                 'fruit':'apple',
#                 'car':'mclarabe'
#      }
# }
# person.update(fav)
# print(person)
# person.update({})   ##data remains same. it means we haven't added any data




# person={
#     'name':'abhinav',
#     'age':22,
#     'gender':'male',
#     'address':{
#         'hno':76,
#         'colony':'vasant vihar',
#         'city':'haridwar',
#         'state':'uttarakhand'
#     },
#     'marks':list(range(50,110,10)),
#     'previous-marks':tuple(range(10,60,10))
# }
#value funtion:-----
# x=person.keys()
# print(x)
# y=person.values()
# print(y)

##checking for the key in dictionary:-
# if 'name' in person:
#     print('yes')
# else:
#     print('no')

# ##checking values in dictionary:-
# if '22' in person.values():    ##checking single value
# # if {                         ##checking multiple values
# #     'hno':76,
# #     'colony':'vasant vihar',
# #     'city':'haridwar',
# #     'state':'uttarakhand'
# #     } in person.values():
#     print('yes')
# else:
#     print('no')

###looping in dictionaries:----
# for i in person:
        ##or##
# for i in person.keys():
#     print(i)                ##it will print keynames

# for i in person.values():
#     print(i)              ## it will print values

##using keys to get values in loop:--
# for i in person:
#     print(f"key is= {i} and value is= {person[i]}")

#items_method:------*******
# print(person.items())
##it retuns the list of tuples containing the key-values pair

# for i in person.items():
#     print(i)

# for key,value in person.items():
#     print(f"key is= {key} and value is= {value}")




# person={
#     'name':'abhinav',
#     'age':22,
#     'gender':'male',
#     'address':{
#         'hno':76,
#         'colony':'vasant vihar',
#         'city':'haridwar',
#         'state':'uttarakhand'
#     },
#     'marks':list(range(50,110,10)),
#     'previous-marks':tuple(range(10,60,10))
# }
##pop method:------
##we give key name and it deletes that key
# print(f"before pop method:-\n{person}")
# person.pop('previous-marks')
# print(f"\nafter pop method:-\n{person}\n")

##popitem method:------
##it always pops the last item
# person.popitem()
# print(person)


####when we want to give same value to many keys:------
##adding keys using list:
# person=dict.fromkeys(['name','age'],"unknown")
##adding keys using tuple:
# person=dict.fromkeys(('name','age'),'unknown')
##adding keys by deforming the string:
# person=dict.fromkeys('abcd',["unknown",])
# print(type(person['a']))


##get method:------------------
#it is used to get key values
#get method returns none if key is not present in dict.
#it is more used professionally
# print(person['names'])   #----->it will give an error
# print(person.get('names'))      #----->it will give an none
# print(person.get('names','not found'))   #-->giving user defined output instead of none

# if 'name' in person:
        ####or###
# if person.get('name'):
#     print('present')
# else:
#     print('absent')

##clear method:----------
#it clear the dictionary
# print(person)
# person.clear()
# print(person)

##copy method:-----------
# it creates new dictionary and copies tha data in it from older one
# person2=person.copy()
# print(person2)
# print(person == person2)        ##true coz same data
# print(person is person2)     #false coz different dictionaries

# but 
# person2=person
# it does not creates new disctionary rather it gives a new identifier name to existing dictionary. so when we perform operation using new dictionary name it changes the overall data coz it is same dictionary



####function returning a dictionary:------
# def fun(num):
#     # d={}
#     d=dict()
#     i=0
#     while i<=num:
#         d[i]=i**3
#         i+=1
#     return d
# x=int(input("enter the number="))
# print(fun(x))



##alphabet counter:-------------
# def fun(wrd):
#     d={}
#     for i in wrd:
#         d[i]=wrd.count(i)
#     return d
# word=input('enter your word=')
# print(fun(word))



# name=input('enter your name=')
# age=input('enter your age=')
# fav=[]
# fav.extend(input('enter your fav movies(,)=').split(','))
# person={
#         'name':name,
#         'age':age,
#         'fav-movies':fav
# }
# for i,j in person.items():
#     print(f"{i}=={j}")




#################dictionary comprehension#############
# d={num:num**2 for num in range(1,11)}
# print(d)
# d={f"square of {num} is ":num**2 for num in range(1,11)}
# print(d)

##counting number of characters:------------
# wrd='abhinav garg'
# d={chr:wrd.count(chr) for chr in wrd}
# print(d)

##checking even or odd number:-------------
# d={i:'even' if i%2==0 else 'odd' for i in range(1,11)}
# print(d)



# dictionary unpacking
# d={
#         'fname':'abhinav',
#         'lname':'garg',
#         'age':22
# }
# print(d)
# n1,n2,n3=d
# print(f"{n1} : {d[n1]}")
# print(f"{n2} : {d[n2]}")
# print(f"{n3} : {d[n3]}")


# converting list of tuples into dictionary
# l=[('a',1),('b',2),('c',3),('d',4)]
# print(l)
# print(dict(l))





