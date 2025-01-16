import csv
import os

file_to_load = os.path.join("/users/samibsata/desktop/STARTER_CODE/PyPoll/Resources/election_data.csv")
file_to_output = os.path.join("/users/samibsata/desktop/STARTER_CODE/PyPoll/Analysis/election_analysis.txt")

total_votes = 0
candidate_votes = {}

with open(file_to_load) as csvfile:
    data = csv.reader(csvfile)

    header = next(data)

    for r in data:
        votes = r[0]
        candidate_names = r[2]

        total_votes += 1

        if candidate_names not in candidate_votes:
            candidate_votes[candidate_names] = 0
        candidate_votes[candidate_names] += 1


total_votes = sum(candidate_votes.values())


output = "Election Results\n"
output += "------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += "------------------------\n"
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {votes} votes ({percentage:.2f}%)\n"
output += "------------------------\n"
for candidate, votes in candidate_votes.items():
    max_candidate = max(candidate_votes, key=candidate_votes.get)
output += f"Winner: {max_candidate}\n"


# Print the output when needed
print(output)

with open(file_to_output, mode ='w') as txt_file:
    txt_file.write(output)        

