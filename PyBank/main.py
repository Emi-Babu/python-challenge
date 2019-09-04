import os
import csv

csvpath = os.path.join("budget_data.csv")

months = []
revenue = []
profit = []

with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)

        for row in csvreader:
                months.append(row[0])
                revenue.append(int(row[1]))

        total_months = len(months)
        total_revenue = sum(revenue)

        for i in range(1, len(revenue)):
                revenue_change = ((int(revenue[i]) - int(revenue[i-1])))
                profit.append(revenue_change)
  
        avg_change = sum(profit) / len(profit)
        Greatest_increase = max(profit)
        Greatest_date = (months[profit.index(Greatest_increase)+1])
        Greatest_decrease = min(profit)
        loss_date = (months[profit.index(Greatest_decrease)+1])

print("Financial Analysis")
print("----------------------")
print(f"Total months: {str(total_months)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {Greatest_date} (${str(Greatest_increase)})")
print(f"Greatest Decrease in Profits: {loss_date} (${str(Greatest_decrease)})")

output_file = open("output_data_file.txt", "w")
output_file.write("Financial Analysis \n")
output_file.write("----------------------\n")
output_file.write("Total months: "+str(total_months)+ "\n")
output_file.write("Total: $"+str(total_revenue)+ "\n")
output_file.write("Average Change: $"+str(round(avg_change,2))+ "\n")
output_file.write("Greatest Increase in Profits: "+Greatest_date+ "  ($"+str(Greatest_increase)+") \n")
output_file.write("Greatest Decrease in Profits: "+loss_date+ "  ($"+str(Greatest_decrease)+") \n")