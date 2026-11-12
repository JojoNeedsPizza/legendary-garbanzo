height = (int(input("Enter the height of the pizza: ")))
weight = (int(input("Enter the weight of the pizza: ")))

print("Calculate ur BMI")

bmi = weight / (height) ** 2

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are normal weight")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight")
else:
    print("You are obese Pizza boiiiii")