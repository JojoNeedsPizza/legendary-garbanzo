#CIA

#input sum of all ur money

amount = int(input("Please enter the amount of money you have: "))

# formula


note_100 = (amount//100)
note_50 = (amount%100)//50
note_10 = (amount%100%50)//10

print("100 Euro notes: ", note_100)
print("50 Euro notes: ", note_50)
print("10 Euro notes: ", note_10)
