# import modules
import os
import csv

print('Election Results')
print('---------------------------------')

# determine where the csv file is
election_csv = os.path.join('Resources/election_data.csv')

# open and read election_data.csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    # set variables to determine results
    vote_count = 0
    charles_count = 0
    diana_count = 0
    raymon_count = 0

    # start looping through data
    for row in csv_reader:
        
        # count all votes
        vote_count += 1

        # count nominee votes
        if row[2] == 'Charles Casper Stockham':
            charles_count += 1
        elif row[2] == 'Diana DeGette':
            diana_count += 1
        elif row[2] == 'Raymon Anthony Doane':
            raymon_count += 1

        # determine percentage of votes
        charles_percent = round((charles_count/vote_count)*100,3)
        diana_percent = round((diana_count/vote_count)*100,3)
        raymon_percent = round((raymon_count/vote_count)*100,3)

        # code to determine the winner based on individual vote count
        if charles_count > diana_count | raymon_count:
            winner = 'Charles Casper Stockham'
        elif diana_count > charles_count | raymon_count:
            winner = 'Diana DeGette'
        else:
            winner = 'Raymon Anthony Doane'

# print results in terminal
print('Total Votes: ' + str(vote_count))
print('---------------------------------')
print(f'Charles Casper Stockham: {charles_percent}% ({charles_count})')
print(f'Diana DeGette: {diana_percent}% ({diana_count})')
print(f'Raymon Anthony Doane: {raymon_percent}% ({raymon_count})')
print('---------------------------------')
print(f'Winner: {winner}')
print('---------------------------------')

# export results to .txt file
output_path = os.path.join('Analysis/pypoll_output.txt')

with open(output_path, 'w') as txt_file:
    txt_file.write('Election Results' + '\n')
    txt_file.write('---------------------------------' + '\n')
    txt_file.write('Total Votes: ' + str(vote_count) + '\n')
    txt_file.write('---------------------------------' + '\n')
    txt_file.write(f'Charles Casper Stockham: {charles_percent}% ({charles_count})' + '\n')
    txt_file.write(f'Diana DeGette: {diana_percent}% ({diana_count})' + '\n')
    txt_file.write(f'Raymon Anthony Doane: {raymon_percent}% ({raymon_count})' + '\n')
    txt_file.write('---------------------------------' + '\n')
    txt_file.write(f'Winner: {winner}' + '\n')
    txt_file.write('---------------------------------')

print('\n' + 'Results have been exported to the pypoll_output.txt file')
