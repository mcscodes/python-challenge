import os
import csv

# Initialize variables
total_votes = 0
candidates = []
votes_received = {}

# Read the CSV file
with open('Resources/election_data.csv', 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes_received[candidate] = 1
        else:
            votes_received[candidate] += 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_received.items()}

# Determine the winner
winner = max(votes_received, key=votes_received.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes_received[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the analysis results to a text file
with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates:
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes_received[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")