# ********* never create file with same name as package ******** #

                                            ############   OS  ###########
# import os

# getcwd() ---> returns current working directory
# print(os.getcwd())                              

# mkdir('path with dir name') ---> creates diretory with given name in cwd 
                        # if a dir. with such name is alredy present the return error
                        # but it cannot create file or folder inside folder which also u creating
# os.mkdir('movies')
# os.mkdir('./movies')

# makedirs() --->  it is used to create file or folder inside just created folder
# os.makedirs('./movies/tiger/pors')

# path.exist('directory path') ---> return true if such dir exists in that path otherwise returns false
# print(os.path.exists('./movies'))


# checking existence and then creating directory:--
# if(os.path.exists('./movies')):
#     print('already exists')
# else:
#     os.mkdir('./movies')


# file creation
# 1) it will create if not created and doest not create duplicate file
# with open('file.txt','a') as f:
#     f.close()


# change the current woking directory:-
# chdir() returns nothing
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())


# get the list of files and directories of given path
# print(os.listdir('./'))


# how to join path-----
# get the path of each file in specific path:-
# os.chdir('../')
# cur_path = os.getcwd()
# for item in os.listdir(cur_path):
#     # print(os.getcwd() + '\\' + item)
#         ### or ##
#     print(os.path.join(cur_path,item))


# it performs file depth search on given path:
# or we can say it do tree type thing
# fileiter = os.walk('./')
# for current_path,folder_name,file_name in fileiter:
#     print(f'current path : {current_path}')
#     print(f'folder name : {folder_name}')
#     print(f'file name : {file_name}')



# to delete folder-----
# it creates only existing and empty folder
# non empty -- error  : folder isnot empty
# non existing -- error  : no such file or directory exists
# os.rmdir('movies')


# splitext(filename)  --->  it splits the path and filename and returns both of them
# it is function of submodule path of module os
# for item in os.listdir('./'):
#     filename,extension=os.path.splitext(item)
#     print(f'filename : {filename}\nextesion : {extension}')


# to print the size of file in KB
# print(os.stat('./virtualenv.txt').st_size)


                                            ############   shutil  ###########
# import shutil

# rmtree() ---> it can be used to delete even non empty folder which os.rmdir() cannot do
# shutil.rmtree('./movies')

# copytree(path1,path2) ---> to copy whole folder system to new place with same or new name
# path1 -- path with folder name to copy
# path2 -- paht with folder name(same or new) where we want to copy
# shutil.copytree('./movies','../pictures')
# coping movies folder from cwd to parent folder with name picture

# copy(path1,path2) ---> to copy file in same way as copytree()

# shutil.move('old path with name','new path with new or same name') ---> can be used to move a file or folder






                                            ############   time  ###########
# import time 
# initial=time.time()
# for i in range(50):
#     print('hello')
# print(time.time()-initial)

# print(time.localtime(time.time()))      # localtime returns in form of tuple
# print(time.asctime(time.localtime(time.time())))        # asctime changes in readable format
# time.sleep(2)
# print('hello')




# import sys
# print(sys.path)
# gives path for searching for modules







##################importing other files data###########
# when we import file it even executes the data in it 
# it does not do so when called in other file
# it is not executed only when data is main() in file1 which is imported in file2

# file1.py
# a=10

# file2.py
# import file1
# print(file1.a)

# or

# from file1 import a
# print(a)







# file1.py
# def fun(string):
#    print(f'hello {string}')

# fun('abhinav')                        # --> will get executed when file is imported
# or #
# if __name__ == "__main__":
#       fun('abhinav')                        # --> will not get executed when file is imported
#---------------
# file2.py
# import file1
# file1.fun('nandini')
