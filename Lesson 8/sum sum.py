# vars
des_usr_sum = int(input("Enter the sum you desire to get: "))

sum = 0

# i stores value of the current number in the range, sum stores the total sum of all numbers from 1 to des_usr_sum

for i in range(1,des_usr_sum+1):
	sum = sum + i
	print(f"{sum}")