import os
import csv

csvpath = os.path.join('election_data.csv')

candidate_list = []
votes = []
names = []
percentage = []
total_votes = 0
unique_candidate = 0

with open (csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        csvheader = next(csvreader)
        for row in csvreader:
                candidate_list.append(row[2])
                total_votes = len(candidate_list)

for i in set(candidate_list):
        candidate_vote = candidate_list.count(i)
        votes.append(candidate_vote)
        names.append(i)
        total_percent = round((candidate_vote/total_votes) * 100, 3)
        percentage.append(total_percent)
        unique_candidate = unique_candidate + 1

winner = names[votes.index(max(votes))]

print("Election Results")
print("-----------------------------------")

print(f'Total Votes: {total_votes}')
print("-----------------------------------")

for i in range(unique_candidate):
        print(f'{names[i]}: {percentage[i]}%  ({votes[i]})')
print("-----------------------------------")

print(f'Winner: {winner}')
print("-----------------------------------")


output_file = open("output_data_file.txt", "w")
output_file.write("Election Results \n")
output_file.write("-----------------------------------\n")
output_file.write("Total Votes: " +str(total_votes)+ "\n")
output_file.write("-----------------------------------\n")
for i in range(unique_candidate):
        output_file.write(f'{names[i]}: {percentage[i]}%  ({votes[i]})')
        output_file.write("\n")
output_file.write("-----------------------------------\n")
output_file.write("Winner: " +str(winner)+ "\n")
output_file.write("-----------------------------------\n")