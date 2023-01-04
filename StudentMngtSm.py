import mysql.connector
import os
exitval='n'

while(exitval=='n'):
    os.system('cls')
    print('-'*90)
    print('|'+' '*31+'STUDENT MANAGEMENT SYSTEM'+' '*32+'|')
    print('-'*90)
    print('| [I]nsert Record |',end='')
    print('  [V]iew Record   |',end='')
    print('  [U]pdate Record |',end='')
    print('  [D]elete Record |',end='')
    print('    [E]XIT   |')
    print('-'*90)
    ch=input('YOUR Choice (I/V/U/D/E):')
    ch=ch.upper()
    print(ch)

    if(ch=='I'):


        connection=mysql.connector.connect(host="localhost",user="root",passwd="",db="test")
        mycursor=connection.cursor()

        choice='y'
        while(choice=='y'):

            sno=input('enter the roll number of student ')
            sname=input('enter the name of student ')
            
            Qry="INSERT INTO class12 (sno, sname) VALUES (%s, %s)"
            print(Qry)
            data=(int(sno),sname)
            print(data)
            
            mycursor.execute(Qry,data)
            print('RECORD INSERTED SUCCESSFULLY')

            choice=input('do you with to insert more records (y/n)')
            if(choice=='y'):
                continue
            connection.commit()
            connection.close()

    elif(ch=='V'):
        connection=mysql.connector.connect(host="localhost",user="root",passwd="",db="test")
        mycursor=connection.cursor()

        choice='y'
        while(choice=='y'):
            rno=int(input('enter the roll number of student whose record you want to search '))
            Qry="SELECT * FROM class12 WHERE sno=%s;"
            print(Qry)
            data=(rno,)
            mycursor.execute(Qry,data)
            myresult = mycursor.fetchall()
            count=0
            
            for x in myresult:
                print(x)

            choice=input('do you with to search more record(y/n)')
            if(choice=='y'):
                continue

    exitval=input('\t\t Do you wish to exit the program(y/n)')
