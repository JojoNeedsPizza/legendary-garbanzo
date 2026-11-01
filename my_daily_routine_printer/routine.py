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
def wanna_return_to_the_main_menu():
    print("\n")
    returnmainmenuyesno = input("Wanna return to the main menu? \n Enter y for yes or n for no: ")
    if returnmainmenuyesno == "y":
        main_menu()
    else:
        print("\nExited Code")
        print("Thanks for using my Tool:)")
# --> print routine function
# "Has to be under all the funcs on the bottom, so it gets all the edited values'
def print_routine_func():
    print("\n---- Routine ----")
    print(f" - I wake up at {wake_up_time} AM")
    print(f" - I go to school at {go_to_school_time} AM")
    print(f" - I play Minecraft with my friends at {play_after_school_with_friends_time} PM")
    print(f" - I study at {study_clock_time} PM for {study_per_day_time} hours.")
    print("-----------------\n")
    yesno_studytime_per_week = input("Wanna calculate the studytime per week? \n Enter y for yes or n for no: ")

    if yesno_studytime_per_week == "y":
        print(f"\nMy weekly total studytime is a total of {study_time_for_whole_week} hours.")
        wanna_return_to_the_main_menu()

    elif yesno_studytime_per_week == "n":
        print("\n Ok, maybe next time :)")
        wanna_return_to_the_main_menu()

    else:
        print("\n no response = auto no\n")
        main_menu()
# --> main_menu to return to after running other funcs
def main_menu():
    print("\n ----------------- \n My Daily Routine: \n -----------------")

    start_end = input("(Enter 1 to Print \n Enter 2 to Exit): ")

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

# Core Code
main_menu()




