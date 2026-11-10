# --__--


act_pris = float(input("Act Pris: "))
sales_pris = float(input("Sell price: "))

# formula
profit = sales_pris - act_pris

#if stuff
if profit > 0:
    print("You made a prof of {0}€".format(profit))
elif profit < 0:
    print("You made a loss of {0}€".format(profit))
else:
    print("You made no profit or loss")
