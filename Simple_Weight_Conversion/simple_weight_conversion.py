weight = float(input("Enter weight: "))

unit = input("Enter unit (L for Lbs or K for Kg): ")

if unit == "K":
	converted = weight * 2.205
	unit = "Lbs"
	print(f"Weight in {unit} is {converted}")
	
elif unit == "L":
	converted = weight / 2.205
	unit = "Kg"
	print(f"Weight in {unit} is {converted}")
	
else:
	print("Invalid unit")