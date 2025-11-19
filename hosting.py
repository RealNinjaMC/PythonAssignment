rate_per_hour = 0.51

cost_per_day = rate_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

print("Cost per day:", cost_per_day)
print("Cost per week:", cost_per_week)
print("Cost per month:", cost_per_month)

money = 918
hours_possible = money / rate_per_hour
days_possible = hours_possible / 24

print("Days the server can run with $918:", days_possible)
