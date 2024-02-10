# 1. Decisions at the Crossroad
# Task 1: Code Correction
# You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

# Buggy Code:

# number = input("Enter a number: ")

# if int(number) > 0:
#     print("The number is positive.")
# elif int(number)== 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")


# 2. The Story Brancher
# Task 1: Code Correction
# You are provided with a Python script that uses if-else structures for a story branching mechanism. There are some errors in the code. Identify and correct them.

# Buggy Code:

# choice = input("Do you choose the path to the left or right? ")

# if choice == "left":
#     print("You find a treasure chest!")
# elif choice == "right":
#     print("You encounter a dragon!")
# else:
#     print("Invalid choice!")

# 3. The Greatest Showdown
# Objective:
# Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest
# Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
# def largest_number():
#     number1 = int(input('enter a number '))
#     number2 = int(input('enter another number '))
#     number3 = int(input('enter one last number '))
#     if ( number1 > number2) and (number1 > number3):
#         print(number1)
#     elif ( number2 > number1) and (number2 > number3):
#         print(number2)
#     else:
#         print(number3)
# largest_number()

# Task 2: Identify the Smallest
# Extend your program from Task 1 to also determine the smallest number among the three and print it out.
# def largest_and_smallest_number():
#     number1 = int(input('enter a number '))
#     number2 = int(input('enter another number '))
#     number3 = int(input('enter one last number '))
#     if ( number1 > number2) and (number1 > number3):
#         print('largest number: ',number1)
#         if ( number2 < number3):
#             print('smallest number: ',number2)
#         else:
#             print('smallest number: ',number3)
            
#     if ( number2 > number1) and (number2 > number3):
#         print('largest number: ',number2)
#         if (number1 < number3):
#             print('smallest number: ',number1)
#         else:
#             print('smallest number: ',number3)
    
#     if ( number3 > number1) and (number3 > number2):
#         print('largest number: ',number3)
#         if ( number1 < number2):
#             print('smallest number: ',number1)
#         else:
#             print('smallest number: ',number2)
# largest_and_smallest_number()


# Task 3: Equality Check
# Enhance your program to handle cases where two or all of the numbers are equal. The program should display appropriate messages like "Two numbers are equal and the largest" or "All numbers are equal".
# def equality_check():
#     number1 = int(input('enter a number '))
#     number2 = int(input('enter another number '))
#     number3 = int(input('enter one last number '))

#     if ( number1 == number2 == number3):
#         print("All numbers are equal")

#     elif (number1 == number2) and (number1 > number3):
#         print(f'Two numbers are equal and largest {number1} and {number2} while, {number3} is the smallest')

#     elif (number1 == number3) and (number1 > number2):
#         print(f'Two numbers are equal and largest {number1} and {number3} while, {number2} is the smallest')
        
#     elif (number2 == number3) and (number2 > number1):
#         print(f'Two numbers are equal and largest {number2} and {number3} while, {number1} is the smallest')

#     elif ( number1 > number2) and (number1 > number3):
#         print('largest number: ',number1)
#         if ( number2 < number3):
#             print('smallest number: ',number2)
#         else:
#             print('smallest number: ',number3)
            
#     elif ( number2 > number1) and (number2 > number3):
#         print('largest number: ',number2)
#         if (number1 < number3):
#             print('smallest number: ',number1)
#         else:
#             print('smallest number: ',number3)
    
#     elif ( number3 > number1) and (number3 > number2):
#         print('largest number: ',number3)
#         if ( number1 < number2):
#             print('smallest number: ',number1)
#         else:
#             print('smallest number: ',number2)
# equality_check()

# 4. Leap Year Explorer
# Objective:
# Dive deep into the intricacies of the calendar by exploring the concept of leap years.
# Task 1: Leap Year Checker
# Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message.
def leap_year(year):
    if (year % 400 == 0):
        print(year, ' is a Leap Year')
    elif (year % 100 == 0):
        print(year, ' is not a Leap Year')
    elif (year % 4 == 0):
        print(year, ' is a Leap Year')
    else:
        print(year, ' is not a Leap Year')
leap_year(2000)
leap_year(2016)
leap_year(1900)
leap_year(2015)

# Task 2: Century Verification
# Add functionality to your program from Task 1 to inform the user if the entered year is a century year (e.g., 1900, 2000) regardless of whether it's a leap year or not.
def century_verificaitonZ(year):
    if (year % 400 == 0):
        print(year, ' is a Leap Year and it is also a century year')
    elif (year % 100 == 0):
        print(year, ' is not a Leap Year and it is also a century year')
    elif (year % 4 == 0):
        print(year, ' is a Leap Year')
    else:
        print(year, ' is not a Leap Year')
century_verificaiton(2000)
century_verificaiton(2016)
century_verificaiton(1900)
century_verificaiton(2015)

# Task 3: Time Traveler
# Enhance your program to indicate if the provided year is in the future, past, or is the current year, compared to the system's current year. You might find Python's datetime module helpful for this task.