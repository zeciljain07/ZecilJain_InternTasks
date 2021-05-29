import mysql.connector as z

#connecting to the database
conn= z.connect(host="localhost", user="root", passwd="", database="college_db")
cur= conn.cursor()

#Create table
cur.execute("create table  if not exists std (S_id int, S_name VARCHAR(50))")

#Performing CRUD FUNCTIONS
ans='y'
while ans=='y' or ans=='Y':
    user=int(input("CRUD operations : \n 1. C-Insert Data \n 2. Read/Display Data \n 3. Update Data \n 4. Delete Data \n  "))

    #Inserting values in the function
    if user==1:
        more='y'
        while more=='y' or more=='Y':
            sid=int(input("Enter student id:"))
            sname=input("Enter student name:")
            cur.execute("insert into std values({},'{}')".format(sid, sname))
            conn.commit()
            more=input("Do you want to insert more data ? (y/n)")

    #Diplaying values from the tables
    if user==2:
        cur.execute("select * from std")
        data=cur.fetchall()
        for i in data:
            print(i)

    #Updating values of the table
    if user==3:
        update_user=input("What do you want to update? \n A. Student ID \n B. Student Name \n")
        if update_user=='A' or update_user=='a':
            sid_old=int(input("Enter the existing Student ID: "))
            sid_new=int(input("Enter the new Student ID: "))
            cur.execute("update std set S_id={} where S_id={}".format(sid_new, sid_old))
            conn.commit()
            print("Data updates successfully.")
        if update_user=='B' or update_user=='b':
            sid=int(input("Enter the Student ID to update Student name:"))
            sname=input("Enter the new Student name:")
            cur.execute("update std set S_name='{}' where S_id={}".format(sname, sid))
            conn.commit()
            print("Data updated successfully.")

    #Deletingt values from the table
    if user==4:
        delete_user=input("Press \n A. Delete Entire Data \n B. Delete Selected Data\n")
        if delete_user=='A' or delete_user=='a':
            cur.execute("delete from std")
            conn.commit()
            print("Entire Data deleted.")
        if delete_user=='B' or delete_user=='b':
            sid=int(input("Enter the Student ID record to be deleted:"))
            cur.execute("delete from std where S_id={}".format(sid))
            print("Data deleted successfully.")
    ans=input("Run again? (y/n)")
