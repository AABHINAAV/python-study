# most probably (,) is the delimiter for csv file
# but it can be comprised of other delimiter like * \ |
# extension for csv file for good colouring of data ---> rainbow csv

# file.csv--->
# name,email,phone
# harshit,harshit@gmail.com,1234
# abhi,abhi@gmail.com,3456


# reader function returns the data in form of list-----
# from csv import reader
# with open('file.csv','r') as f:
#     csv_reader = reader(f)
#     # csv_reader is iterator so we can use loop on it but only once
#     next(csv_reader)
#     for row in csv_reader:
#         print(row[1])


# DictReader is better than reader function of csv module coz it gives data in form of ordered dictionary-----
# it does not shows first line(header line) as result
# it uses headers as keys-----
# from csv import DictReader
# with open('file.csv','r') as f:
#     csv_reader = DictReader(f)
#     for row in csv_reader:
#         print(row['name'])
#         print(row['phone'])







# file.csv--->
# name|email|phone
# harshit|harshit@gmail.com|1234
# abhi|abhi@gmail.com|3456

# now i have changed the delimiter form (,) to (|) so above 2 codes will give error
# so we pass an argument delimiter='|(seperator)' in reader or DictReader function

# from csv import DictReader
# with open('file.csv',"r") as f:
#     csv_reader = DictReader(f,delimiter='|')
#     for row in csv_reader:
#         print(row)
#         print(row['email'])






# from csv import reader
# with open('file.csv',"r") as f:
#     csv_reader = reader(f,delimiter='|')
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)






# from csv import writer
# with open('file.csv','w',newline='') as f:     # w or a --> both modes are ok
#     # newline='' to not paste blank line if giving in csv file
#     csv_writer = writer(f)
#     # methods ---> writerrow , writerows

#     # writerow([]) ---> writes single row at a time
#     # csv_writer.writerow(['name','country'])
#     # csv_writer.writerow(['abhi','India'])
#     # csv_writer.writerow(['jassi','Nepal'])
#     # csv_writer.writerow(['ankit','Portugal'])

#     # writerows([[]]) ---> writes multiple row at a time
#     csv_writer.writerows([['name','country'],['abhi','India'],['jassi','Nepal'],['ankit','Portugal']])






# from csv import DictWriter
# with open('file.csv', 'a') as f:
#     # open can have one more argument newline='' to remove empty line(if showing)
#     csv_writer = DictWriter(f, fieldnames=['name', 'country'])
#     csv_writer.writeheader()
#     # methods ---> writerow , writerows

#     # writerow({}) --->
#     # csv_writer.writerow({
#     #     'name':'abhi',
#     #     'country':'India'
#     # })
#     # csv_writer.writerow({
#     #     'name':'jassi',
#     #     'country':'Nepal'
#     # })
#     # csv_writer.writerow({
#     #     'name':'ankit',
#     #     'country':'Portugal'
#     # })

#     # writerows([{},{},{},....])
#     csv_writer.writerows([

#         {
#             'name': 'abhi',
#             'country': 'India'
#         },
#         {
#             'name': 'jassi',
#             'country': 'Nepal'
#         },
#         {
#             'name': 'ankit',
#             'country': 'Portugal'
#         }
#     ])





# file.csv--->
# name,country
# abhi,India
# jassi,Nepal
# ankit,Portugal
# file1.csv--->
# name,rollno
# ABHI,1
# JASSI,2
# ANKIT,3
# from csv import DictReader, DictWriter
# with open('file.csv','r') as rf:
#     with open('file1.csv','w') as wf:
#         csv_reader=DictReader(rf)
#         csv_write=DictWriter(wf,fieldnames=['name','rollno'])
#         csv_write.writeheader()
#         i=1
#         for row in csv_reader:
#             csv_write.writerow({
#                 'name':row['name'].upper(),
#                 'rollno':i
#             })
#             i += 1

