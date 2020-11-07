# f=open('file1.txt','r')  ## default is 'r'
# print(f'cursor position : {f.tell()}')
# print(f.read())         ## cursor has reached to last point of file
# print(f'cursor position : {f.tell()}')
# print(f.read())         ## so here no output
# print(f'cursor position : {f.tell()}')
# print('seek method:-')
# f.seek(0)
# print(f'cursor position : {f.tell()}')
# print(f.read())
# print(f'cursor position : {f.tell()}')
# f.close()


# f=open('file1.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline(),end='')
# print(f.readline(),end='')
# f.close()


# readlines() is basically used for file slicing:-
# f = open('file1.txt')
# lines=f.readlines()
# print(lines)
# print(type(lines))
# print(len(lines))
# f.close()


# f = open('file1.txt')
# print(f.name)
# print(f.closed)
# f.close()
# print(f.closed)


# file path in :-
# window ---> has \
# linux, mac ---> has /
# in python escape sequence uses \ like \n, \t so in window we write path like--
# f = open(r"E:\abhi\VIDA")


# file object is also iterable:-
# f = open('file1.txt')
# for line in f:
#     print(line)


# using with block:-
# if file is damaged then context manager does not opens it, closes file by itself
# we dont need to close the file
# with open('file1.txt','r') as f:
#     data = f.read()
#     print(data)
#     print(f.closed)
# print(f.closed)     #file closed own its own


# write:-----
# using with block:-
# with open('file2.txt','w') as f:
#     f.write('hello')      # creates file if not present and writes data
# with open('file2.txt','w') as f:
#     f.write('hi')         # overwrites the data

# using open:-
# f=open('file2.txt','w')
# f.write('hello')
# f.close()


# append:-----
# using with block:-
# with open('file.txt','a') as f:
#     f.write('hi')           # creates file if not present
# with open('file.txt','a') as f:
#     f.write('hello')        # appends data

# using open:-
# f=open('file.txt','a')
# f.write('\nabhinav')
# f.close()


# r+ mode ==> it allows read and write at same time:-
# it does not creates file just like read and append mode
# with open('file.txt','r+') as f:
#     print(len(f.read()))
#     print(f.tell())
#     f.seek(10)
#     print(f.tell())
#     f.write('yaso')
#     print(f.tell())

# file1.txt:-
# abhinav,100
# jassi,90
# ankit,80
# nimisha,70
# file2.txt:-
# hello abhinav, your salary is 100
# hello jassi, your salary is 90
# hello ankit, your salary is 80
# hello nimisha, your salary is 70
# with open('file1.txt') as rfile:
#     data = rfile.readlines()
#     with open('file2.txt','a') as wfile:
#         for line in data:
# name,salary=line.split(',')
# wfile.write(f'hello {name}, your salary is {salary}')


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>finding link using python</title>
# </head>
# <body>
#     <a href="www.youtube.com"></a>
#     <a href="www.github.com"></a>
#     <a href="www.npmjs.com"></a>
#     <a href="www.linkedin.com"></a>
# </body>
# </html>
# extract url form this file and store them in a new file:-
# it will extract only one link from a file:-
# with open('try.html') as rf:
#     with open('data.txt','a') as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                 first_quote=line.find('\"')+1
#                 second_quote=line.find('\"',first_quote+1)
#                 wf.write(line[first_quote:second_quote] + '\n')
# www.youtube.com
# www.github.com
# www.npmjs.com
# www.linkedin.com

# better solution:-
# with open('try.html') as rf:
#     with open('data.txt', 'a') as wf:
#         page = rf.read()
#         link_exist = True
#         while link_exist:
#             pos = page.find('<a href=')
#             if pos == -1:
#                 link_exist = False
#             else:
#                 first_quote = page.find('\"',pos)
#                 second_quote = page.find('\"', first_quote+1)
#                 wf.write(page[first_quote+1:second_quote] + '\n')
#                 page = page[second_quote:]






### checking encoding of file:
# with open('data.txt') as file:
#     print(file.encoding)    # ---> UTF-8

# if while reading file that has emojis gives error then we need to change its
# encoding and it solve our problem

# with open('data.txt',encoding='utf-8') as file:
#     pass