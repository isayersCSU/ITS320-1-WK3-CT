tax_brackets = {
"a" : 10,
"b" : 15,
"c" : 20,
"d" : 30
}
income = int(input("Enter Weekly Earnings: "))
if income < 500:
    print((tax_brackets["a"] * income)/100)
elif income >= 500 and income < 1500:
    print((tax_brackets["b"] * income)/100)
elif income >= 1500 and income < 2500:
    print((tax_brackets["c"] * income)/100)
elif income >= 2500:
    print((tax_brackets["d"] * income)/100)
else : print("Invalid Option.")
	
