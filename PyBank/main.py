# Financial Analysis - PyBank - Emily Boulware

import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# setting initial values to variables or creating blank lists to store data
total_months = 0
total_profit_loss = 0

new_profit_loss = 0
profit_loss_average_change = []

dates = []

with open(budget_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    for row in csv_reader:

        # finding the total number of months
        total_months = total_months + 1
        
        # finding the total profit/loss 
        total_profit_loss = total_profit_loss + int(row[1])

        # calculating each change in profit/loss and updating the list
        profit_loss_changes = int(row[1]) - new_profit_loss
        new_profit_loss = int(row[1])
        profit_loss_average_change.append(profit_loss_changes)

        # build out the dates list for each row
        dates.append(row[0])
        
    # removing first change stored in list since it skews the results
    profit_loss_average_change.pop(0)

    # calculating the average change in profit/loss and rounding to two decimals
    average_change = round(sum(profit_loss_average_change) / (total_months - 1), 2)
    
    # find the greatest change in profit/loss and mark the associated month
    greatest_change = max(profit_loss_average_change)
    greatest_date_index = profit_loss_average_change.index(greatest_change)
    greatest_date = dates[greatest_date_index+1]

    # find the worst change in profit/loss and mark the associated month
    worst_change = min(profit_loss_average_change)
    worst_date_index = profit_loss_average_change.index(worst_change)
    worst_date = dates[worst_date_index+1]

# printing the average change list helped me see that I needed to take out the first
# value of the list for the average to calculate correctly
#print(profit_loss_average_change) 

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_change})")
print(f"Greatest Decrease in Profits: {worst_date} (${worst_change})")

#-------------------------------------

# now to write the results to a .txt file in the "Analysis" folder
analysis_txt = os.path.join("Analysis", "FinancialAnalysis.txt")

with open(analysis_txt, 'w') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total_profit_loss}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_change})\n")
    text_file.write(f"Greatest Decrease in Profits: {worst_date} (${worst_change})\n")