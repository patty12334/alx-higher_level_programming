mport random
number = random.randint(-10000, 10000)
LastDigit =0

if number >= 0:
	LastDigit = number % 10
else:
	LastDigit = (-number % 10) *-1
message = f"Last digit of {number} is {LastDigit}"

if LastDigit ==0:
	print(f"{message} and is 0")
elif LastDigit >5 and LastDigit % 10 != 0:
	print (f"{message} and is greater than 5")
else:
	print(f"{message} and is less than 6 and not 0")
