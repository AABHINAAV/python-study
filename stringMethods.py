# name='abhinav garg'

#index()
# it returns the index of first occurence of char in string
# if not present then error
# print(name.index('z'))

##find()
# it returns the index of first occurence of char in string
# if not present then returns -1
# print(name.find('a'))
# print(name.find('m'))

##rfind()
# it returns the index of last occurence of char in string
# if not present then returns -1
# print(name.rfind('a'))

##isaplha()
# it returns true if all characters are alphabetic not number,symbol or space
# print(name.isalpha())

##isdigit()
# it returns true if all characters are digits not alphabet,symbol or space
# print(name.isdigit())

##isalpha()
# it returns true if all characters are digits or numbers but not symbols
# s='123as'
# print(s.isalnum())

##isupper()
# it returns true if all characters are in upper case
# print(name.isupper())

##islower()
# it returns true if all characters are in lower case
# print(name.islower())

##isspacer()
# it returns true if all characters are whitespace
# print(name.isspace())

##partition()
# it takes only one argument( single character or multiple characters )
# it returns tuple with value before charater, character and after character
# if not present it gives whole strig as first value then econd and third values are ''
# print(name.partition('a'))
# print(name.partition('nav'))

##join()
# if puts the given string btw each pair of characters
# x=' and '.join(name)
# print(x)

##replace()
# it returns a string with replaces series of characters
# if not present then it returns the original string
# third argument defines how many occurences we need to replace
# name='abhinav garg abhinav abhinav abhinav'
# print(name.replace('abhinav','nandini'))
# print(name.replace('xyz','nandini'))
# print(name.replace('abhinav','nandini',2))

##endswith()
# returns ture if string ends with given character or stirng
# print(name.endswith('g'))

##startswith()
# returns true if string starts with given character or stirng
# print(name.startswith('ab'))

##capitalize()
# returns first word capitalized while others are as it is
# print(name.capitalize())

##title()
# return string with all words capitalised
# print(name.title())

name='abhinav garg'
print(name[0:5])