import os
import csv

pybank_csv = os.path.join("Resources", "03-Python_Homework_PyBank_Resources_budget_data.csv")

#read in the csv file
with open(pybank_csv, "r") as csvfile:

    #split the data on the commas
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header row
    header = next(csvreader)

    #creating lists to hold specific columns/calculations
    months = []
    profits_loss = []
    differences = []

    #loop through the given csv
    for row in csvreader:
        #put all the months in one list
        months.append(row[0])
        #puts all the profits or losses in one list
        profits_loss.append(int(row[1]))     

    #counts the number of entries in months list
    month_counter = len(months)

    #sum the entries in profits/loss list
    total = sum(profits_loss)

    #set values
    great_profit = 0
    great_loss = 0
    profit_index = 0
    loss_index = 0

    #loop though the profits_loss list using i as an index number
    for i in range(len(profits_loss)-1): #len(list)-1 because at the end we don't want to use a row outside the number of entries
        cur = profits_loss[i] 
        nxt = profits_loss[i+1]
        #determines the difference from one month to the next
        difference = (nxt - cur)
        #if difference is the greatest profit 
        if difference > great_profit:
            great_profit = difference
            profit_index = (i+1) #saves the index 
        #if difference is greatest loss
        if difference < great_loss:
            great_loss = difference
            loss_index = (i+1) #saves the index
        #creates new list of the differences from month to month
        differences.append(difference)
        
    #average change in profits/losses from one month to the next
    avg_differences = sum(differences)/len(differences)
    
    
    #Analysis to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_counter}")
    print(f'Total ${total}') #total profit/loss
    print(f"Average Change: ${avg_differences:.2f}") #average change in profits/loss
    print(f'Greatest Increase in Profits: {months[profit_index]} (${great_profit})')
    print(f'Greatest Decrease in Profits: {months[loss_index]} (${great_loss})')


    #Analysis to analysis.txt in Analysis directory
    analysis_file = open(r"Analysis/analysis.txt", "w")

    analysis_file.write("Financial Analysis")
    analysis_file.write("\n") #new line
    analysis_file.write("----------------------------")
    analysis_file.write("\n")
    analysis_file.write(f'Total Months: {month_counter}')
    analysis_file.write("\n")
    analysis_file.write(f'Total ${total}')
    analysis_file.write("\n")
    analysis_file.write(f"Average Change: ${avg_differences:.2f}")
    analysis_file.write("\n")
    analysis_file.write(f'Greatest Increase in Profits: {months[profit_index]} (${great_profit})')
    analysis_file.write("\n")
    analysis_file.write(f'Greatest Decrease in Profits: {months[loss_index]} (${great_loss})')    
    