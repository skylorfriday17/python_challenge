# import modules to access csv
import os
import csv

# print heading for output
print('Financial Analyis')

print('--------------------------')

#find csv file
pybank_csv = os.path.join('Resources/budget_data.csv')

#access csv file
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip header
    csv_header = next(csv_reader)
    
    # set variables and lists to use later
    total_months = 0
    total = 0

    changes = []

    previous_profit = None
    
    greatest_increase = 0
    greatest_decrease = 0
    
    # start looping to rerturn initial values
    for row in csv_reader:
        total_months += 1
        total += int(row[1])
    
        current_profit = int(row[1])
        
        # create conditionals to find average change in profit/losses and max/min changes
        if previous_profit is not None:
            change = current_profit - previous_profit
            
            if change > greatest_increase:
                greatest_increase = change
                date_increase = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                date_decrease = row[0]
            
            changes += [change]
            
            previous_profit = current_profit

        previous_profit = current_profit

    average_change = sum(changes)/len(changes)
   
# print out all results from looping
print('Total Months: ' + str(total_months))
print('Total: $' + str(total))
print('Average change: $' + str(round(average_change,2)))
print(f'Greatest Increase in Profits: {date_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})')


# export results to .txt file
output_path = os.path.join('Analysis/pybank_ouput.txt')

with open(output_path, 'w') as txt_file:
    txt_file.write('Financial Analyis')
    txt_file.write('\n' + '--------------------------' + '\n')
    txt_file.write('Total Months: ' + str(total_months) + '\n')
    txt_file.write('Total: $' + str(total) + '\n')
    txt_file.write('Average change: $' + str(round(average_change,2)) + '\n')
    txt_file.write(f'Greatest Increase in Profits: {date_increase} (${greatest_increase})' + '\n')
    txt_file.write(f'Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})')
    
print('\n' + 'Results have been exported to the pybank_output.txt file')