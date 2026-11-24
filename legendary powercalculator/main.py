# powercalculator
number = int(input("Enter the number, of that you wanna calculate its power: " ))
power = int(input("Enter the power: "))
calc = 0
res = ""

for i in (0, power):
    print(f"{i}")
    number = number * number

print(f"{number}")
