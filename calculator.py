#basic calculator program
import math as m

def add(x, y):
	z = x+y
	
	return z

def sub(x,y):
	
	return x - y

def multiplication(x, y):

	return x*y

def div(x, y):

	if y == 0:
		print("Cannot divide by zero!")
		exit_program()

	return x/y

def exit_program():
	
	print("Exiting...")
	exit()

def main():
	
	total = int(input("Insert integer: "))

	run = True

	while(run):
		mode = input("Select mode ( +, -, *, /), or press q to quit: ")
		
		if mode == 'q':
			exit_program()
			run = False
		
		elif mode == '+':
			print("Addition is working")
			input2 = int(input("Insert 2nd integer: "))
			total = add(total, input2)
			print("Current total: ", total)
		elif mode == '-':
			print("Subtraction is working")
			input2 = int(input("Insert 2nd integer: "))
			total = sub(total, input2)
			print("Current total = ", total)
		elif mode == '*':
			print("Multiplication is working")
			input2 = int(input("Insert 2nd integer: "))
			total = multiplication(total, input2)
			print("Current total = ", total)
		elif mode == '/':
			print("Division is working")
			input2 = int(input("Insert 2nd integer: "))
			total = div(total, input2)
			print("Current total = ", total)
		else: 
			print("Invalid input! Try again.")
		
main()
