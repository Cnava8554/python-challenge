import os
import csv


    
budget_csv = os.path.join('Resources', 'budget_data.csv')

total_months=[]
total_profits=[]
profit_change=[]
profit = 0
ele=0

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    
    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(int(row[1]))
        while(ele < len(total_profits)):
            profit = profit + total_profits[ele]
            ele += 1
            
for row in range(len(total_profits) - 1):
    profit_change.append(total_profits[row+1] - total_profits[row])
    
    maxincrease = profit_change.index(max(profit_change)) + 1
    maxdecrease = profit_change.index(min(profit_change)) + 1
    
    avgpc = round(sum(profit_change) / len(profit_change),2)
#    avgpc = sum(profit_change)/len(profit_change)
#        profits = sum(int(total_profits))
#        for ele in range(1, len(total_profits)):
 #           profit = profit + total_profits[ele]
 
print("Financial Analysis:")
print("----------------------------")
print(f"Total Months:  {len(total_months)}")
print(f"Net Profit: ${profit}")
print(f"Average Change: ${avgpc}")
print(f'Greatest Decrease: {total_months[maxdecrease]} (${min(profit_change)})')
print(f'Greatest Increase: {total_months[maxincrease]} (${max(profit_change)})')

createFile = os.path.join("Analysis","Financial_Analysis_Summary.txt")
with open(createFile,"w") as file:
    
    file.write("Financial Analysis:")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months:  {len(total_months)}")
    file.write("\n")
    file.write(f"Net Profit: ${profit}")
    file.write("\n")
    file.write(f"Average Change: ${avgpc}")
    file.write("\n")
    file.write(f'Greatest Decrease: {total_months[maxdecrease]} (${min(profit_change)})')
    file.write("\n")
    file.write(f'Greatest Increase: {total_months[maxincrease]} (${max(profit_change)})')