# receive input
med_con_yn = input("Do you have an medical condition (Y/N): ")
med_con_yn = med_con_yn.upper()
med_con_yn = med_con_yn.strip()

# declare if input is correct and decide function

if med_con_yn == "Y" :
 print("Is Allowed")
elif med_con_yn == "N":
 print("You're not Allowed")
 attendance = int(input("Enter your attendance quota: "))
 if attendance >= 75:
    print("You are allowed")
 else:
    print("You are not allowed")
else:
 print(f"Please write y or n not sum gibberish like {med_con_yn}")
