import os
import csv

pypoll_csv = os.path.join("Resources", "03-Python_Homework_PyPoll_Resources_election_data.csv")

#finds the max value of dictionary and returns the associated key
def winner_finder(dictionary):  
     v=list(dictionary.values())
     k=list(dictionary.keys())
     return k[v.index(max(v))]

#read in the csv file
with open(pypoll_csv, "r") as csvfile:

    #split the data on the commas
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header row
    header = next(csvreader)

    #defining lists to hold all names in candidates column and a list of each of the candidate names
    candidate_column = []
    candidate_list = []

    #loop through rows in csvreader
    vote_counter = 0
    for row in csvreader:
        #put candidate column into list
        candidate_column.append(row[2])
        #put each of the distinct candidate names into list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        #count the number of votes
        vote_counter += 1

    #create dictionary with each candidate names and their vote totals
    vote_totals = {}
    vote_totals = dict((x,candidate_column.count(x)) for x in set(candidate_column))



#print results to terminal
print("Election Results")
print("-------------------------")
print(f'Total votes: {vote_counter}')
print("-------------------------")
#prints the candidate names, percent of total votes earned, and number of votes earned
for candidate in candidate_list:
    percent_earned = vote_totals[candidate]/vote_counter * 100
    print(f'{candidate}:  {percent_earned:.3f}% ({str(vote_totals[candidate])})')
print('-------------------------')
print(f'Winner: {winner_finder(vote_totals)}')
print('-------------------------')

#print results to analysis.txt file
analysis_file = open(r"Analysis/analysis.txt", "w")
analysis_file.write("\n")
analysis_file.write("Election Results")
analysis_file.write("\n")
analysis_file.write("-------------------------")
analysis_file.write("\n")
analysis_file.write(f'Total votes: {vote_counter}')
analysis_file.write("\n")
analysis_file.write("-------------------------")
analysis_file.write("\n")
#prints the candidate names, percent of total votes earned, and number of votes earned
for candidate in candidate_list:
    percent_earned = vote_totals[candidate]/vote_counter * 100
    analysis_file.write(f'{candidate}:  {percent_earned:.3f}% ({str(vote_totals[candidate])})')
    analysis_file.write("\n")
analysis_file.write('-------------------------')
analysis_file.write("\n")
analysis_file.write(f'Winner: {winner_finder(vote_totals)}')
analysis_file.write("\n")
analysis_file.write('-------------------------')