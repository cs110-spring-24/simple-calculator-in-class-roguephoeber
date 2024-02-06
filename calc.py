firstnum = float(input("Enter a number: "))
op = input("Enter an operation: ")
secondnum = float(input("Enter a second number: "))

if op == "+":
	total = firstnum+secondnum
	print(f"{firstnum} + {secondnum} = {total}")
	exit()
if op == "-":
	total = firstnum-secondnum
	print(f"{firstnum} - {secondnum} = {total}")
	exit()
if op == "*":
	total = firstnum*secondnum
	print(f"{firstnum} * {secondnum} = {total}")
	exit()
if op == "/":
	if secondnum == 0:
		print("cannot divide by zero.")
		exit()
	total = firstnum+secondnum
	print(f"{firstnum} + {secondnum} = {total}")
	exit()
if op == "**":
	total = firstnum**secondnum
	print(f"{firstnum} ** {secondnum} = {total}")
	exit()
if op == "%":
	total = firstnum%secondnum
	print(f"{firstnum} % {secondnum} = {total}")
	exit()
if op == "//":
	total = firstnum//secondnum
	print(f"{firstnum} // {secondnum} = {total}")
	exit()
if op != "+" and "-" and "*" and "/" and "**" and "%" and "//":
	print("not a valid operator, try again. ")
	exit()