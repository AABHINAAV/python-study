import tkinter as tk
from tkinter import ttk, messagebox as mbox
import mysql.connector

root = tk.Tk()
root.title('MYSQL GUI')
root.geometry('1000x600+200+70')

tk.Label(text='welcome to gui based mysql powered with python',font='arial 20 bold',fg='red',bg='yellow').pack(side=tk.TOP)

################ notebook contruction
options = ttk.Notebook(root)
options.pack(expand=True,fill='both',pady=20)

    # frames
db_names=ttk.Frame(options) #
create_db=ttk.Frame(options) #
delete_db=ttk.Frame(options) #
tbl_names=ttk.Frame(options) #
create_table=ttk.Frame(options) 
table_data=ttk.Frame(options) #
frames_dict={
    db_names:'show databases names',
    create_db:'create database',
    delete_db:'delete database',
    tbl_names:'table names',
    create_table:'create table',
    table_data:'table data'
}
for frame_var,frame_name in frames_dict.items():
    options.add(frame_var,text=frame_name)


#//////////////////////////////////////////////////////////////////////////////////////
################# for database names frame
    # show db button
show_db_names_btn = tk.Button(db_names,text='show databases')
show_db_names_btn.pack(side=tk.TOP,pady=10)

result_db_names=tk.Text(db_names,font='arial 14 bold',width=70,height=23)
result_db_names.pack(side=tk.TOP)


# /////////////////////////////////////////////////////////////////////////////////////
################# for create database frame
    # frame for centralising----->
f1=tk.LabelFrame(create_db,text='')
f1.pack(side=tk.TOP,pady=30)
    # label----->
tk.Label(f1,text='Enter the database name : ').grid(row=0,column=0,padx=20,pady=10)
    # entry field----->
create_db_entry = tk.Entry(f1,width=30)
create_db_entry.grid(row=0,column=1,padx=20,pady=10)
    # button----->
create_db_btn = tk.Button(create_db,text='create database')
create_db_btn.pack(side=tk.TOP)
    # status label----->
# create_db_status_var=tk.StringVar()
create_db_status_lbl=tk.Label(create_db)
create_db_status_lbl.pack(side=tk.TOP,pady=20)

# ////////////////////////////////////////////////////////////////////////////////////
################### for delete database frame
    # frame for centralising----->
f2=tk.LabelFrame(delete_db,text='')
f2.pack(side=tk.TOP,pady=30)
    # label----->
tk.Label(f2,text='Enter the database name : ').grid(row=0,column=0,padx=20,pady=10)
    # entry field----->
delete_db_entry = tk.Entry(f2,width=30)
delete_db_entry.grid(row=0,column=1,padx=20,pady=10)
    # button----->
delete_db_btn = tk.Button(delete_db,text='delete database')
delete_db_btn.pack(side=tk.TOP)
    # status label----->
# create_db_status_var=tk.StringVar()
delete_db_status_lbl=tk.Label(delete_db)
delete_db_status_lbl.pack(side=tk.TOP,pady=20)




# ////////////////////////////////////////////////////////////////////////////////////
################# for show tables names frame
    # frame for centralising----->
f3=tk.LabelFrame(tbl_names,text='')
f3.pack(side=tk.TOP,pady=30)
    # label----->
tk.Label(f3,text='Enter the database name : ').grid(row=0,column=0,padx=20,pady=10)
    # entry field----->
show_tables_entry = tk.Entry(f3,width=30)
show_tables_entry.grid(row=0,column=1,padx=20,pady=10)
    # button----->
show_tables_btn = tk.Button(tbl_names,text='show tables')
show_tables_btn.pack(side=tk.TOP)
    # showeing tables names in text area
result_tables_names=tk.Text(tbl_names,font='arial 14 bold',width=70,height=23)
result_tables_names.pack(side=tk.TOP)



# ////////////////////////////////////////////////////////////////////////////////////
################# for create tables frame




# ////////////////////////////////////////////////////////////////////////////////////
################# for show tables data frame
    # frame for centralising----->
f5=tk.LabelFrame(table_data,text='')
f5.pack(side=tk.TOP,pady=30)
    # label for db name----->
tk.Label(f5,text='Enter the database name : ').grid(row=0,column=0,padx=20,pady=10)
    # entry field for db name----->
db_name_show_entry = tk.Entry(f5,width=30)
db_name_show_entry.grid(row=0,column=1,padx=20,pady=10)
    # label for table name----->
tk.Label(f5,text='Enter the table name : ').grid(row=1,column=0,padx=20,pady=10)
    # entry field for table name----->
table_name_show_entry = tk.Entry(f5,width=30)
table_name_show_entry.grid(row=1,column=1,padx=20,pady=10)
    # button----->
show_table_data_btn = tk.Button(table_data,text='show tables')
show_table_data_btn.pack(side=tk.TOP)
    # showeing tables names in text area
result_tables_data=tk.Text(table_data,font='arial 14 bold',width=70,height=23)
result_tables_data.pack(side=tk.TOP)




####################### functionalities ##########
    # legendary funtions:-
def connect_to_mysql(db=''):
    conn=mysql.connector.connect(host='localhost',username='root',password='',database=db)
    return conn
def disconnect_from_mysql(conn):
    conn.commit()
    conn.close()


# called to show db names ----->
def show_db_names_func():
    conn = connect_to_mysql()
    my_cursor = conn.cursor()
    my_cursor.execute('show databases')
    result_db_names.delete(1.0,tk.END)
    for name in my_cursor:
        result_db_names.insert(tk.END,f'\t{name[0]}\n')
    disconnect_from_mysql(conn)
show_db_names_btn['command']=show_db_names_func



# called to create the database ----->
def create_db_func():
    try:
        create_db_status_lbl.delete(1.0,tk.END)
        name = create_db_entry.get()
        conn=connect_to_mysql()
        my_cursor = conn.cursor()
        my_cursor.execute('show databases')
        exist=False
        for i in my_cursor:
            if i[0]==name:
                exist=True
                create_db_status_lbl['text']=f'database with such name already present...please use some other name'
        if not exist:
            my_cursor.execute(f'create database {name}')
            create_db_status_lbl.insert(1.0,'database created sucessfully')
        disconnect_from_mysql(conn)
    except:
        return
create_db_btn['command']=create_db_func



# called to delete the database ----->
def delete_db_func():
    try:
        name = delete_db_entry.get()
        conn=connect_to_mysql()
        my_cursor = conn.cursor()
        my_cursor.execute(f'drop database {name}')
        delete_db_status_lbl['text']=f'database {name} deleted sucessfully'
        disconnect_from_mysql(conn)
    except:
        delete_db_status_lbl['text']=f'no such database exists'
delete_db_btn['command']=delete_db_func



# called to show tables names button ----->
def show_tables_names_func():
    try:
        result_tables_names.delete(1.0,tk.END)
        name = show_tables_entry.get()
        if name=='':
            result_tables_names.insert(1.0,'\n\tplease enter the database name')
        else:
            conn=connect_to_mysql()
            my_cursor=conn.cursor()
            db_exist=False
            my_cursor.execute('show databases')
            for i in my_cursor:
                if i[0] ==name:
                    db_exist=True
                    pass
            number_of_tbls=0
            if db_exist:
                my_cursor.execute(f'use {name}')
                my_cursor.execute(f'show tables')
                for i in my_cursor:
                    result_tables_names.insert(tk.END,f'\n\t{i[0]}\n')
                    number_of_tbls += 1
                if number_of_tbls==0:
                    result_tables_names.insert(1.0,'\n\tdatabase is empty')
            else:
                result_tables_names.insert(1.0,'\n\tno such database present')
            disconnect_from_mysql(conn)
    except:
        return
show_tables_btn['command']=show_tables_names_func



# called for showing table data:-
def show_table_data_func():
    try:
        result_tables_data.delete(1.0,tk.END)
        db_name = db_name_show_entry.get()
        table_name = table_name_show_entry.get()
        if db_name=='' or table_name=='':
            result_tables_data.insert(1.0,'\n\tplease enter the database name as well as table name')
        else:
            conn=connect_to_mysql()
            my_cursor=conn.cursor()
            db_exist=False
            my_cursor.execute('show databases')
            for i in my_cursor:
                if i[0] ==db_name:
                    db_exist=True
                    pass
            number_of_tbls=0
            if db_exist:
                my_cursor.execute(f'use {db_name}')
                my_cursor.execute(f'show tables')
                tb_exist=False
                for i in my_cursor:
                    if table_name == i[0]:
                        tb_exist=True
                        my_cursor.execute(f'select * from {table_name}')
                        for i in my_cursor:
                            result_tables_data.insert(tk.END,f'\n\t{i}\n')
                if tb_exist==False:
                    result_tables_data.insert(1.0,'\n\tno such table exists')
            else:
                result_tables_data.insert(1.0,'\n\tno such database present')
            disconnect_from_mysql(conn)
    except:
        return
show_table_data_btn['command']=show_table_data_func





root.mainloop()