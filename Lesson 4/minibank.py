# Var Grades

maths = int(input("Please enter your Maths grade: "))
english = int(input("Please enter your English grade: "))
german = int(input("Please enter your German grade: "))
geography = int(input("Please enter your Geography grade: "))

# Calculate Average
sum = maths + english + german + geography
average = sum / 400
percentage = average * 100

print("percentage: ", percentage)