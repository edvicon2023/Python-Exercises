# Exercise 1: Greet the User and Check If the User Was Born in a Leap Year

def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    greet_user()
    year = int(input("Enter your birth year: "))
    if is_leap_year(year):
        print("You were born in a leap year!")
    else:
        print("You were not born in a leap year.")

main()
