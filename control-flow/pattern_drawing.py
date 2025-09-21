pattern = int(input("Enter the size of the pattern: "))

i = 0

while i < pattern:
	for item in range(0, 4):
		print("*", end="")
	print("\n")
	i += 1
