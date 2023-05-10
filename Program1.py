#project 1

TempNum = int(input("please input temperture: "))
temp = input("please input either C for Celsius or F for Fahrenheit: ")
TemCon = 0 
#this would conver the temperture to another temperture 
#this would convert celsius to Fahrenheit
if temp == "C" or temp == "c":
	Temcon = (TempNum*(9/5))+32
	print("the converted temperture is ", '{0:.1f}'.format(Temcon), " Fahrenheit")
#this would convert Fahrenheit to celsius
elif temp == "F" or temp == "f":
	Temcon = (TempNum-32)*(5/9)
	print("the converted temperture is ", '{0:.1f}'.format(Temcon), " Celsius")
#this would end the program if an incorrect 
else:
	print("please input an real temperture")

