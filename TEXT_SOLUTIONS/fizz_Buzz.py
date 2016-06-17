for x in range(101):
	noNum = False
	if x % 3 == 0:
		fizz_Buzz = "Fizz"
		noNum = True
	if x % 5 == 0:
		fizz_Buzz = "Buzz"
		noNum = True
	if x % 5 == 0 and x % 3 == 0:
		fizz_Buzz ="FizzBuzz"
		noNum = True
	if noNum == True:
		print(fizz_Buzz)
	else:
		print(x)