#install xlrd using pip
# Reading an excel file using Python 
import xlrd 
import smtplib
import datetime
import xlwt

loc = ("librarylog2122proc1.xlsx")



# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
  
# Extracting number of rows 
print(sheet.nrows) 
print(sheet.ncols)



wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')



print("***************************")

#for i in range(sheet.nrows):
i=0
cntwt=0

ws.write(cntwt, 0, "ID" )
ws.write(cntwt, 1, "NAME")
ws.write(cntwt, 2, "CATEGORY")
ws.write(cntwt, 3, "LOGIN TIME")
ws.write(cntwt, 4, "LOGOUT TIME")
ws.write(cntwt, 5, "TIME IN MIN")
ws.write(cntwt, 6, "TIME IN SEC")

while i<sheet.nrows-2:
    try:    
        name=sheet.cell_value(i, 1)
        idjec=str(sheet.cell_value(i, 0))
        #print(type(idjec))
        cat=sheet.cell_value(i, 2)
        #excel_date=sheet.cell_value(i,5)    
        a = datetime.datetime(int(sheet.cell_value(i,7)) , int(sheet.cell_value(i,6)) , int(sheet.cell_value(i,5)) , int(sheet.cell_value(i,8)) , int(sheet.cell_value(i,9)) , int(sheet.cell_value(i,10)) )
        #b = datetime.datetime(2017, 5, 16, 8, 21, 10)
      
    # returns a timedelta object
        
        #print(name)
        #print(sheet.cell_value(i,4))
        n=i+1
        c=1
        while(name==sheet.cell_value(n, 1)):
            #print("same person")
            n=n+1
            c=c+1
        #print (c)
        #print ("diff is ", i+c-1,i)
        b = datetime.datetime(int(sheet.cell_value(i+c-1,7)) , int(sheet.cell_value(i+c-1,6)) , int(sheet.cell_value(i+c-1,5)) , int(sheet.cell_value(i+c-1,8)) , int(sheet.cell_value(i+c-1,9)) , int(sheet.cell_value(i+c-1,10)) )
        c = b-a 
        #print('Difference: ', c)
      
    # returns (minutes, seconds)
        minutes = divmod(c.total_seconds(), 60) 
        #print('Total difference in minutes: ', minutes[0], 'minutes',minutes[1], 'seconds')
        print(idjec,",",name,",",cat,",",a,",",b,",",int(minutes[0]),":",int(minutes[1]))
        #dur=(minutes[0])+":"+(minutes[1])  
        ws.write(cntwt+1, 0, idjec )
        ws.write(cntwt+1, 1, name)
        ws.write(cntwt+1, 2, cat)
        ws.write(cntwt+1, 3, str(a))
        ws.write(cntwt+1, 4, str(b))
        ws.write(cntwt+1, 5, int(minutes[0]))
        ws.write(cntwt+1, 6, int(minutes[1]))
        
        
        
        cntwt=cntwt+1

        
        i=n;
        #print("************")
    except:
        wb.save('example.xls')
wb.save('example.xls')    
    #print(sheet.cell_value(i, 1))
    #print(sheet.cell_value(i, 2))
    #print(sheet.cell_value(i, 3))
    

   
    
# For row 0 and column 0 
#print(sheet.cell_value(0, 0))
#print(sheet.cell_value(0, 1))
#print(sheet.cell_value(0, 2))


