# printing longest word-----
# lst = ['abhinav', 'jaspal', 'ankit']

# method 1-----
# def fun(item):
#     return len(item)
# print(max(lst,key=fun))

# method 2-----
# print(max(lst, key=lambda item: len(item)))




# printing whole info on basis of one data-----
# students = [
#     {'name': 'abhinav', 'age': 22},
#     {'name': 'jassi', 'age': 23},
#     {'name': 'ankit', 'age': 25}
# ]
# # whole data on basis of name length-->
# print(max(students,key=lambda item:len(item['name'])))
# # whole data on bases of age-->
# print(max(students, key=lambda item: item['age']))
# # name on basis of age-->
# print(max(students, key=lambda item: item['age'])['name'])





# students={
#     'abhinav':{'age':22,'lname':'garg'},
#     'jaspal':{'age':23,'lname':'rana'},
#     'ankit':{'age':25,'lname':'nautiyal'}
# }
# print(max(students, key=lambda item:students[item]['age']))
# print(students[max(students, key=lambda item:students[item]['age'])]['lname'])






#############advance sorted function###############

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
