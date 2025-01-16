import csv
import os

# File paths
file_to_load = os.path.join("/users/samibsata/desktop/STARTER_CODE/pybank/resources/budget_data.csv")  # Replace with the correct path
file_to_output = os.path.join("/users/samibsata/desktop/STARTER_CODE/pybank/analysis/budget_final.txt")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []
greatest_increase = {"date": "", "amount": float('-inf')} #dictionary to hold greatest increase
greatest_decrease = {"date": "", "amount": float('inf')}

# Read the CSV file
with open(file_to_load, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        date = row[0]
        profit = int(row[1])
        
        # Count total months
        total_months += 1
        
        # Add to net total
        net_total += profit
        
        # Calculate change and track greatest increase/decrease
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)

            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        # Update previous profit
        previous_profit = profit

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the results
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

print(output)

with open(file_to_output, mode='w') as txt_file:
    txt_file.write(output)