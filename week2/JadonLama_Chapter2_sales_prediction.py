# Get the projected total sales.
# input function reads input from keyboard and float
# function converts it to a floating point number

totalSales = float(input("Enter total sales: "))

# Calculate the profit as 23 percent of total sales and display result
profit = totalSales * 0.23
print(f"The total profit is $", format(profit, ',.2f'))


def calculate_profit():
    totalSales = float(input("Enter total sales:"))
    profit = totalSales * 0.23
    
    print(f"The total profit is $", format(profit, ',.2f'))
calculate_profit()