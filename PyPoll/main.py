import os
import pandas as pd


os.chdir('/Users/forrestbadgley/Documents/DataScience/git/NUCHI201801DATA4-Class-Repository-DATA/MWS/Homework/03-Python/Instructions/PyPoll/raw_data')

csv_path = "election_data_1.csv"
csv_path2 = "election_data_2.csv"

elect1_df = pd.read_csv(csv_path)
elect2_df = pd.read_csv(csv_path2)

#vertical stack of two dataframes
elect3_df = pd.concat([elect1_df, elect2_df], axis=0)


total_votes_cast = elect3_df['Voter ID'].value_counts(dropna=True)
elect3_df['Candidate']= elect3_df['Candidate']
candidates_list = elect3_df['Candidate'].unique()
    
elect3_group = elect3_df.groupby(['Candidate']).count()
total_votes_cast2=elect3_group['Voter ID'].sum()
elect3_group['Decimal']=((elect3_group['Voter ID']/total_votes_cast2)*100).round(2)

print("Election Results")
print("-----------------")
print("Total Votes: " + (str(total_votes_cast2)))
print("-----------------")
print(elect3_group.iloc([1]))
