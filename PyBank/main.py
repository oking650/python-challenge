import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

Months = 0
net_total = 0
delta = 0
total_delta = 0
previous_total = 0

sum_profit = 0
#current row minus previous row

greatest_increase = 0
greatest_decrease = 0

with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        Months = Months + 1
        net_total = net_total + int(row[1])

        #running total
        if previous_total != 0:
            delta = int(row[1]) - previous_total
        previous_total = int(row[1])
        total_delta = total_delta + delta

        



print(Months)
print(net_total)
print(total_delta)
print(total_delta/(Months-1))