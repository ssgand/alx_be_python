income = input('Enter your monthly income: ')
expenses = input('Enter your total monthly expenses: ')

savings = int(income) - int(expenses)

projectedSavings = savings * 12 + (savings * 12 * 0.05)

print('Your monthly savings are $' + str(savings) + '.')
print('Projected savings after one year, with interest, is: $' + str(projectedSavings) + '.')
