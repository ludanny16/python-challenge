#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:19:08 2017

@author: chao_lu
"""

# Dependencies
import csv


#input and output files 
file_to_load = "election_data_2.csv"
file_to_output = "election_data_2.txt"


# Read the csv and convert it into a list of dictionaries

Candidates=[]

with open(file_to_load, newline="") as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")

    # Skip Headers  
    next(csv_reader, None)

    # Loop 
    for row in csv_reader:
        Candidates.append(row[2]) # Update candidate list


# Vote Summary
total_votes=len(Candidates)
c_list=set(Candidates)
c_list=[i for i in c_list]
vote_counts=[Candidates.count(i) for i in c_list]
vote_percent= [((Candidates.count(i)/total_votes)*100) for i in c_list]
vote_percent= [round(i,3) for i in vote_percent]

max_vote=max(vote_counts)


mx, vid = max( (vote_counts[i],i) for i in range(len(vote_counts)) )

win=c_list[vid]
        
    
# printing vote summary 
    
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes) )
print('-------------------------')

c_num=0
for i in c_list:
    print(i + ': ' + str(vote_percent[c_num])+'% '+ '(' + str(vote_counts[c_num]) + ')' )
    c_num+=1

print('-------------------------')

print('Winner: ' + str(win)) 

print('-------------------------')

#export to text file
myfile= open(file_to_output,'w')
myfile.write('Election Results'+ '\n')
myfile.write('-------------------------'+ '\n')
myfile.write('Total Votes: ' + str(total_votes)+ '\n')
c_num=0
for i in c_list:
    myfile.write(i + ': ' + str(vote_percent[c_num])+'% '+ '(' + str(vote_counts[c_num]) + ')'+ '\n')
    c_num+=1
myfile.write('-------------------------'+ '\n')
myfile.write('Winner: ' + str(win)+ '\n')
myfile.write('-------------------------'+ '\n')

myfile.close