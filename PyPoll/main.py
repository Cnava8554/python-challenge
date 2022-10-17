import os
import csv


    
election_csv = os.path.join('Resources', 'election_data.csv')

total_votes=[]
#all_votes=0
Raymond=[]
Diana=[]
Charles=[]
candidate_options=[]
#votes={}

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        total_votes.append(row[0])
        candidate_name = row[2]
#        all_votes +=1
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
        if 'Ray' in candidate_name:
            Raymond.append(candidate_name)
        if 'Diana' in candidate_name:
            Diana.append(candidate_name)
        if 'Charles' in candidate_name:
            Charles.append(candidate_name)
#            votes[candidate_name] = 0
#            votes[candidate_name] += 1
        RPercent = len(Raymond)/len(total_votes) * 100
        DPercent = len(Diana)/len(total_votes) * 100
        CPercent = len(Charles)/len(total_votes) * 100
    
#    for candidate in votes:
#        vote_count = votes[candidate]
#        vote_percent = float(vote_count) /  float(all_votes) * 100
#        candidates.append(row[1])
#        candidates_count = candidates.count(row[1])
        
        
        
        
        
print("Election Results:")
print("------------------------")
print(f"Total Votes: {len(total_votes)}")
print("------------------------")
print(f'{(list(set(candidate_options))[0])}: {RPercent}% {len(Raymond)}')
print(f'{(list(set(candidate_options))[1])}: {DPercent}% {len(Diana)}')
print(f'{(list(set(candidate_options))[2])}: {CPercent}% {len(Charles)}')
print("------------------------")
print(f'Winner: {}')