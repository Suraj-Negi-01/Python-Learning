num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operator = input("Choose an operation (1-4): ")

match operator:
	case "1":
		result = num1 + num2
	case "2":
		result = num1 - num2
	case "3":
		result = num1 * num2
	case "4":
		if num2 == 0:
			print("Error: cannot divide by zero.")
		else:
			result = num1 / num2
	case _:
		print("Error: choose a number from 1 to 4.")

if operator in ["1", "2", "3"] or (operator == "4" and num2 != 0):
	print("Result:", result)
