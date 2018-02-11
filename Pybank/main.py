import os
import csv
os.chdir('/Users/forrestbadgley/Documents/DataScience/git/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyBank/raw_data')


csvpath = "budget_data_1.csv"


# Open the CSV; the encoding line was added after getting error in reading the file and searching google for how to solve
# use with so that don't have to expliciting open and then close the csv file after using; will automatically close
with open(csvpath, newline="", encoding = "ISO-8859-1") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    
    for row in csvreader:
        print(row[0])