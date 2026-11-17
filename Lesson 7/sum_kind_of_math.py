askusr = int(input("How much units do you have used: "))


if askusr < 50:
    print("Youre a good, healthy person, that touches grass")
    surcharge = 25
    amount = askusr * 2.60
elif askusr < 100:
    surcharge = 35
    amount = 130 + (askusr - 50) * 3.25
else:
    amount = 130 + 162.50 + (askusr - 100) * 5.26
    surcharge = 45


total = amount + surcharge


print(f"Ur total is {total}")
