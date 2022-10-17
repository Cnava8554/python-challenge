import os
import csv


    
budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)
    
    for row in csvreader:
        
    def date_totals(budget_data):
        date_total = int(budget_data[0]).count()
    
        print(date_total)