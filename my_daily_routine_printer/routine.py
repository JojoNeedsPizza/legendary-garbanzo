# Define Variables

# Routine Times
wake_up_time = 7
go_to_school_time = 8
play_after_school_with_friends_time = 5
study_per_day_time = 2
study_clock_time = 7

#special study per week timee calculating var
study_time_for_whole_week = study_per_day_time * 7

# Define functions and edit Variables

# --> print routine function
# "Has to be under all the funcs on the bottom, so it gets all the edited values'
def print_routine_func():
    print("\n---- Routine ----")
    print(f" - I wake up at {wake_up_time} AM")
    print(f" - I go to school at {go_to_school_time} AM")
    print(f" - I play Minecraft with my friends at {play_after_school_with_friends_time} PM")
    print(f" - I study at {study_clock_time} PM for {study_per_day_time} hours.\n")

    yesno_studytime_per_week = input("Wanna calculate how long you study per week? \n Enter y for yes or n for no: ")

    if yesno_studytime_per_week == "y":
        print("yes")

    elif yesno_studytime_per_week == "n":
        print("no")

    else:
        print("\n no response = auto no\n")
        main_menu()
# --> main_menu to return to after running other funcs
def main_menu():
    print(" ----------------- \n My Daily Routine: \n -----------------")

    start_end = input("(Enter 1 to Print \n Enter 2 to Exit: ")

    # Print my daily Routine
    if start_end == "1":
        print_routine_func()

    # Exit Code
    elif start_end == "2":
        print("Thanks for using my Tool:)")

    # Easter Egg
    elif start_end == "777":
        print("You hit the Jackpot :)")

    # End Code aswell
    else:
        print("Thanks for using my Tool:)")

# Start of Core Code
print(" ----------------- \n My Daily Routine: \n -----------------")

start_end = input("(Enter 1 to Print \n Enter 2 to Exit: ")


# Print my daily Routine
if start_end == "1":
    print_routine_func()

# Exit Code
elif start_end == "2":
 print("Thanks for using my Tool:)")

# Easter Egg
elif start_end == "777":
 print("You hit the Jackpot :)")

# End Code aswell
else:
 print("Thanks for using my Tool:)")


