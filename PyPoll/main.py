# Election Results - PyPoll - Emily Boulware

import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# setting initial values to variables or creating empty lists to store data
total_votes = 0

candidate_name = []
candidate_votes = []


with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:

        # finding the total number of votes cast
        total_votes = total_votes + 1

        # build out the candidate name list and add up their votes
        name = str(row[2])
        if name in candidate_name:
            candidate_names = candidate_name.index(name)
            candidate_votes[candidate_names] = candidate_votes[candidate_names] + 1
        else:
            candidate_name.append(name)
            candidate_votes.append(1)

# calculating percentages and winning candidate after building out lists above
winning_votes = candidate_votes[0]
max_votes = 0
candidate_percent = []

for vote_count in range(len(candidate_name)):

    percent = round(candidate_votes[vote_count]/total_votes*100, 3)
    candidate_percent.append(percent)

    if candidate_votes[vote_count] > winning_votes:
        winning_votes = candidate_votes[vote_count]
        max_votes = vote_count
    
big_winner = candidate_name[max_votes]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for vote_count in range(len(candidate_name)):
    print(f"{candidate_name[vote_count]}: {candidate_percent[vote_count]}% ({candidate_votes[vote_count]})")
print("-------------------------")
print(f"Winner: {big_winner}")
print("-------------------------")

# now to write the results to a .txt file in the "Analysis" folder
election_txt = os.path.join("Analysis", "ElectionResults.txt")

with open(election_txt, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for vote_count in range(len(candidate_name)):
        text_file.write(f"{candidate_name[vote_count]}: {candidate_percent[vote_count]}% ({candidate_votes[vote_count]})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {big_winner}\n")
    text_file.write("-------------------------\n")