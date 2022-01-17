
import os
import csv


date_list = []
profit_list = []
change_list = []
greatest_increase_amount = 0
greatest_decrease_amount = 0
net_amount = 0
change_amount = 0


csvpath = os.path.join("Resources","budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:
        date_list.append(row[0])
        profit_list.append(row[1])
        net_amount = net_amount + int(row[1])
        
    total_months = len(date_list)
    
        
    for i, value in enumerate(profit_list):
        if i >0:
            previous_amount = int(profit_list[i-1])
            current_amount = int(value)

            change = current_amount - previous_amount
            change_list.append(change)
        
    for amount in change_list:
        change_amount = change_amount + int(amount)
        
    avg_change = round((change_amount/len(change_list)),2)
    
    for amount in change_list:
        if amount > greatest_increase_amount:
            greatest_increase_amount = amount
            increase_pos = change_list.index(amount) + 1
        elif amount < greatest_decrease_amount:
            greatest_decrease_amount = amount
            decrease_pos = change_list.index(amount) + 1
            
    greatest_increase_date = date_list[increase_pos]
    greatest_decrease_date = date_list[decrease_pos]
    


analysis = str((f"Financial Analysis"+"\n"+"----------------------------"+"\n"+f"Total Months: {total_months}"+"\n"+f"Total: ${net_amount}"+"\n"+f"Average Change: ${avg_change}"+"\n"+f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})"+"\n"+f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})"))


print(analysis)
with open('PyBank_Output.txt','w') as analysisOutput:
    analysisOutput.write(analysis)


