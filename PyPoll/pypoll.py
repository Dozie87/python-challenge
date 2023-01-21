#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Dependencies
import csv
import os

#load dataset and read it into an ouput file
load_file = os.path.join(".", "Resources", "election_data.csv")
load_output = os.path.join(".", "election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate options and vote counters
candidate_votes = {}
candidate_options = []

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

with open(load_file) as election_data:
    reader = csv.reader(election_data)
    
    #excluding the header
    header = next(reader)
       
    for row in reader:
        total_votes += 1
        
        #get candidate name from each row
        candidate_name = row[2]
        
        #if candidate does not match any existing candidate...the loop is discovering candidate as it goes
        if candidate_name not in candidate_options:
            
            #add the list of candidates in the running
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
            

with open(load_output, "w") as txt_file:   
    election_results = (
    f"Election Results\n"
    f"------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------\n"
    )
        
    print(election_results, end="")
    
    txt_file.write(election_results)
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage =float(votes) / float(total_votes)* 100
        
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        print(voter_output, end="")
        txt_file.write(voter_output)
        
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------------\n"
    )
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)


# In[ ]:




