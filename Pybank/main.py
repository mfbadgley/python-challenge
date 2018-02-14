import os
import csv
os.chdir('/Users/forrestbadgley/Documents/DataScience/git/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyBank/raw_data')


csvpath = "budget_data_1.csv"

# creat lists to hold data
Total_Months = []
Total_Revenue = 0
Revenue_Change = []
Greatest_Increase_Date =[]
mydict = []
Greates_Increast_Amt =[]
Greatest_Decrease_Date =[]
Greatest_Decrease_Amt =[]


# Open the CSV; the encoding line was added after getting error in reading the file and searching google for how to solve
# use with so that don't have to expliciting open and then close the csv file after using; will automatically close
with open(csvpath, newline="", encoding = "ISO-8859-1") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) #so loop starts after headerrows

    for row in csvreader:
        #put all the months into a list
        Total_Months.append(row[0])
        #add up the revenue column
        Total_Revenue+=(int(row[1]))
        #put the revenue numbers into a list
        Revenue_Change.append(int(row[1]))

    
    #absolute value of the incremental change between revenue nums
    v = [abs((Revenue_Change[i+1]-Revenue_Change[i])) for i in range(len(Revenue_Change)-1)]
    #create a list of the revenue changes, called c
    c = [((Revenue_Change[i+1]-Revenue_Change[i])) for i in range(len(Revenue_Change)-1)]
    
    #calc average of the list, assign to variable
    Average_Revenue_Change = int(sum(c)/(len(c)))
    #remove first month from month list, so lines up with revenue changes
    Tot_months = Total_Months[1:]
    #create a dictionary of the months, lined up with the revenue changes, where key is revenue change
    mydicty = dict(zip(c, Tot_months))

   #find the min and max revenue change #'s
    max_increase_revenue = max(c)
    max_decrease_revenue = min(c)
    
   
      
print("Financial Analyis")
print("-----------------")
print("Total Months: " + str(len(Total_Months)))
print("Total Revenue: " + "$"+"{:,}".format((Total_Revenue)))
print("Average Revenue Change: " + "$"+"{:,}".format(Average_Revenue_Change))
print("Maximum Revenue Increase: " + (mydicty[max_increase_revenue]) + " " + "$"+"{:,}".format(max_increase_revenue))
print("Maximum Revenue Decrease: " + (mydicty[max_decrease_revenue]) + " " + "$"+"{:,}".format(max_decrease_revenue))



#print(c.index(max_increase_revenue))
    #print(c.index(max_decrease_revenue))