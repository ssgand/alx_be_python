number = int(input("Enter a number to see its multiplication table: "))

for num in range(1, 11):
	print(str(number) + " * " + str(num) + " = " + str(number * num))
