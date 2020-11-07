import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root', password='')
    ## we can provide db name to connect directly to existing db(if exists)
        # otherwise don't need to provide that argument
# print(conn)       ## it will print mysql connection object 

my_cursor = conn.cursor()




# query = 'create database abcd'
# my_cursor.execute(query)




# query = 'show databases'
# my_cursor.execute(query)

# for database_name in my_cursor:
#     print(database_name)
        ### or ##
# print(my_cursor.fetchall())         # ---> it will return list of all databases names







# query = 'create table student(roll int primary key,name varchar(50),marks int)'
# my_cursor.execute(query)            # it will create table in already existing db that is connected in starting





# query = 'show tables'
# for table_name in my_cursor.execute(query):
#     print(table_name)





# query = 'insert into student values(%s,%s,%s)'
# values = [
#     (1,'abhi',100),
#     (2,'ankit',90),
#     (3,'jassi',80),
#     (4,'nimisha',70)
# ]
# my_cursor.executemany(query,values)






# query='select * from employee'
# my_cursor.execute(query)
# for row in my_cursor:
#     print(row)




# my_cursor.execute('use test')
# my_cursor.execute('show tables')
# for i in my_cursor:
#     print(type(i))
#     print(len(i))
#     print(i)

# my_cursor.execute('use test')
# my_cursor.execute('select * from employee')
# for i in my_cursor:
#         print(i)





my_cursor.execute('select column_name from information_schema.columns where table_name = "employee"')
print(my_cursor)



# conn.commit()       ## not needed everytime but its a good practise
conn.close()
