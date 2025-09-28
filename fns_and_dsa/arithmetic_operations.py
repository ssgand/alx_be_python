
def perform_operation(num1, num2, operation):
	match(operation):
		case "add":
			return num1 + num2
		case "substract":
			return num1 - num2
		case "multiply":
			return num1 * num2
		case "divide":
			if (num2 == 0):
				print("num2 must be different from 0")
				return
			else:
				return num1 / num2
