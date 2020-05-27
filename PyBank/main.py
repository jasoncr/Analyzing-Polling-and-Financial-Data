import os
import csv

pybank_csv = os.path.join("Resources", "03-Python_Homework_PyBank_Resources_budget_data.csv")

#read in the csv file
with open(pybank_csv, "r") as csvfile:

    #split the data on the commas
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header row
    header = next(csvreader)

    months = []
    profits_loss = []
    for row in csvreader:
        #put all the months in one list
        months.append(row[0])
        #puts all the profits or losses in one list
        profits_loss.append(int(row[1]))

    #counts the number of entries in months list
    month_counter = len(months)

    #sum the entries in profits/loss list
    total = sum(profits_loss)
  

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_counter}")
    print(f"Total: {total}")

    


        

