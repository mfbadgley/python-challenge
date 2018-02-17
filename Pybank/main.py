import os
import csv
import datetime
import pandas as pd

os.chdir('/Users/forrestbadgley/Documents/DataScience/git/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyBank/raw_data')

csvpath = "budget_data_1.csv"
csvpath2= "budget_data_2.csv"

# creat lists to hold data
Total_Months = []
Total_Revenue = 0
Revenue_Change = []
Total_Months2 = []
Total_Revenue2 = 0
Revenue_Change2 = []
Date_format = []
Date_format2 = []

#doing everything 2x to open and load data for the two files
# Open the CSV; the encoding line was added after getting error in reading the file and searching google for how to solve
# use with so that don't have to expliciting open and then close the csv file after using; will automatically close
with open(csvpath, newline="", encoding = "ISO-8859-1") as csvfile, open(csvpath2, newline="", encoding = "ISO-8859-1") as csvfile2:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvreader2 = csv.reader(csvfile2, delimiter=",")
    header = next(csvreader) #so loop starts after headerrows
    header2 = next(csvreader2)
    
    for row in csvreader:
        #put all the months into a list
        Total_Months.append(row[0])
        #add up the revenue column
        Total_Revenue+=(int(row[1]))
        #put the revenue numbers into a list
        Revenue_Change.append(int(row[1]))

    for row in csvreader2:
        #put all the months into a list
        Total_Months2.append(row[0])
        #add up the revenue column
        Total_Revenue2+=(int(row[1]))
        #put the revenue numbers into a list
        Revenue_Change2.append(int(row[1]))
    
    #absolute value of the incremental change between revenue nums
    v = [abs((Revenue_Change[i+1]-Revenue_Change[i])) for i in range(len(Revenue_Change)-1)]
    #create a list of the revenue changes in csv file 1, called c
    c = [((Revenue_Change[i+1]-Revenue_Change[i])) for i in range(len(Revenue_Change)-1)]
    #create a list of the revenue changes in csv file2, called d
    d = [((Revenue_Change2[i+1]-Revenue_Change2[i])) for i in range(len(Revenue_Change2)-1)]
    
    
    #calc average of the list, assign to variable
    Average_Revenue_Change = int(sum(c)+ sum(d))/(len(c)+len(d))
    #remove first month from month list, so lines up with revenue changes
    Tot_months = Total_Months[1:]
    Tot_months2 = Total_Months2[1:]
    #convert dates to same format
    Tot_months = (datetime.datetime.strptime(i, "%b-%y") for i in Tot_months)
    Tot_months2 = (datetime.datetime.strptime(i,"%b-%Y") for i in Tot_months2)

    #for date in Tot_months:
       # Date_format.append(datetime.datetime.strftime(date, "%Y-%m-%d"))
       #Tot_months3 = (datetime.datetime.strptime(i, "%Y-%m-%d") for i in Tot_months)

    #create a dictionary of the months, lined up with the revenue changes
    
    #d1 = dict(zip(Tot_months,c))
    #d2 = dict(zip(Tot_months2, d))
    
    d2_df = pd.DataFrame(list(zip(Tot_months, c)))
    d2_df.columns=["Date","Revenue"]
   # d2_df['Date'] = pd.to_datetime(d2_df['Date'])
    #d2_df['Date'] = d2_df['Date'].dt.strftime('%m/%Y')
    #d2_df.Date = pd.to_datetime(d2_df.Date)
    #df2.month = pd.to_datetime(df2.month)
    
    d1_df = pd.DataFrame(list(zip(Tot_months2, d)))
    d1_df.columns=["Date","Revenue"]
    #d1_df['Date'] = pd.to_datetime(d1_df['Date'])
    #d1_df['Date'] = d1_df['Date'].dt.strftime('%m/%Y')
    
    #left outer join of dataframes
    d3_df = pd.merge(d1_df, d2_df, on='Date', how='left')
    d3_df.fillna(0, inplace=True)
    
    #create new column, sum of the two revenue change columns, 
    d3_df["Sum"] = d3_df["Revenue_x"]+d3_df["Revenue_y"]
  
    #d2_df = pd.DataFrame([d2])
    #d1_df = pd.DataFrame(d1, columns=['Date', 'Revenue'], index=0)  
    #d1_df = d1_df.set_index('Date')  

   #find the min and max revenue change #'s
    max_increase_revenue = d3_df['Sum'].max()
    max_decrease_revenue = d3_df['Sum'].min()
    #find total number of months
    months_count = d3_df['Date'].count()
    
    #locate the dates associated with min and max revenue change #'s in dataframe
    date_max=d3_df.loc[d3_df['Sum'] == int(max_increase_revenue), 'Date']
    date_min=d3_df.loc[d3_df['Sum'] == int(max_decrease_revenue), 'Date']
    #change back to required date format
    date_max = date_max.dt.strftime("%b-%y")
    date_min = date_min.dt.strftime("%b-%y")

print("Financial Analysis")
print("-----------------")
print("Total Months: " + (str(months_count)))
print("Total Revenue: " + "$"+"{:,}".format((Total_Revenue+Total_Revenue2)))
print("Average Revenue Change: " + "$"+"{:,}".format(Average_Revenue_Change))
print("Maximum Revenue Increase: " + (date_max.to_string(index=False)) + " " + "$"+"{:,}".format(int(max_increase_revenue)))
print("Maximum Revenue Decrease: " + (date_min.to_string(index=False)) + " " + "$"+"{:,}".format(int(max_decrease_revenue)))

output = ['Financial Analysis: ' , 'Total Months: ' + (str(months_count)), "Total Revenue: " + "$"+"{:,}".format((Total_Revenue+Total_Revenue2)), "Average Revenue Change: " + "$"+"{:,}".format(Average_Revenue_Change), "Maximum Revenue Increase: " + (date_max.to_string(index=False)) + " " + "$"+"{:,}".format(int(max_increase_revenue)), "Maximum Revenue Decrease: " + (date_min.to_string(index=False)) + " " + "$"+"{:,}".format(int(max_decrease_revenue))]

output_path = ('/Users/forrestbadgley/Documents/DataScience/python-challenge/Pybank/outputfile')
with open(output_path, 'w', newline='') as text_file:
        text_file.writelines('\n'.join(output))



#import sys
#filename = open("/Users/forrestbadgley/Documents/DataScience/python-challenge/Pybank/outputfile",'w')
#3sys.stdout 
#text_file.writelines(output)


   