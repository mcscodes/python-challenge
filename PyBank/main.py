import os
import csv

# Path to the budget data file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the budget data file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the dataset
    for row in csvreader:
        # Calculate total months
        total_months += 1

        # Calculate total profit/losses
        total_profit_losses += int(row[1])

        # Calculate profit/loss changes
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_loss_changes.append(profit_loss_change)
        previous_profit_loss = int(row[1])

        # Store the month
        months.append(row[0])

# Calculate average change
average_change = round(sum(profit_loss_changes[1:]) / (total_months - 1), 2)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the results to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print("Results have been exported to financial_analysis.txt")