import os
import csv

os.chdir('/Users/forrestbadgley/Documents/DataScience/git/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyBoss/raw_data')

csvpath = "employee_data1.csv"
csvpath2 = "employee_data2.csv"

emp_id = []
name = []
dob = []
ssn = []
state = []




with open(csvpath, newline="", encoding = "ISO-8859-1") as csvfile, open(csvpath2, newline="", encoding = "ISO-8859-1") as csvfile2:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvreader2 = csv.reader(csvfile2, delimiter=",")
    header = next(csvreader) #so loop starts after headerrows
    header2 = next(csvreader2)
    
    for row in csvreader:
        #put all the emp id's in List
        emp_id.append(row[0])
        #put all the names in
        name.append(row[1])
        #put the dob'sinto a list
        dob.append(row[2])
        #put the ssn's into list
        ssn.append(row[3])
        #put the state's into list
        state.append(row[4])

    for row in csvreader2:
        #put all the emp id's in List
        emp_id.append(row[0])
        #put all the names in
        name.append(row[1])
        #put the dob'sinto a list
        dob.append(row[2])
        #put the ssn's into list
        ssn.append(row[3])
        #put the state's into list
        state.append(row[4])
        
        
        
