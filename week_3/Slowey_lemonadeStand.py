'''
Author: Nate Slowey
Date: 1/26
File Name: Slowey_lemonadeStand.py
Description: calculates cost and profit of lemonade stand
'''

def calculate_cost(lemons_cost, sugar_cost):
  total_cost = lemons_cost + sugar_cost
  return total_cost

def calculate_profit(lemons_cost, sugar_cost, selling_price):
  total_profit = selling_price - lemons_cost - sugar_cost
  return total_profit


# Test variables
lemons_price = 2.50
sugar_price = 1.50
selling_price = 6.00

# Calculate cost
cost_output = calculate_cost(lemons_price, sugar_price)

# Calculate profit
profit_output = calculate_profit(lemons_price, sugar_price, selling_price)

# Print results
print("Cost: $" + str(cost_output))
print("Profit: $" + str(profit_output))