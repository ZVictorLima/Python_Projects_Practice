unit = input("Enter unit (C for Celsius or F for Fahrenheit): ")

temp = float(input("Enter temperature: "))

  

if unit == "C":

    converted = (temp * 9/5) + 32

    unit = "Fahrenheit"

elif unit == "F":

    converted = (temp - 32) * 5/9

    unit = "Celsius"

else:

    print(f"Invalid unit")

  

print(f"Temperature in {unit} is {converted}")