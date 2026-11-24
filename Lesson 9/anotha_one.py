# Armstrong Numbers
# In german: Narzisstische Zahlen

# enter the number to check it
number_to_check = int(input("Enter a number, to check, if it's an Armstrong Number: "))

number_to_check = str(number_to_check)
number_to_check = number_to_check.strip()
#number_to_check = int(number_to_check)

# len() counts the characters
# var[], [] is to select specific a specific character

chars = len(str(number_to_check))
chars = int(chars)

print(chars)
temp = number_to_check
temp_num = 0
num = number_to_check
final_num = 0

for times_repeated in range(chars):
    temp_num = num[times_repeated]

    # formula
    temporary_num2 = int(temp_num)
    temp_num = temporary_num2 ** chars

    # save it
    final_num = final_num + temp_num
    temp_num = 0
    #final_num = final_num + temp_num

print(final_num)

if final_num == number_to_check:
    print(f"Your number {final_num} is an Armstrong Number!")
else:
    print(f"Your number {final_num} is not an Armstrong Number!")
