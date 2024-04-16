# Task 1: Identify the Greatest
# Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
num3 = int(input("Please enter a final number: "))

def largest_number():
    if num1 >= num2 and num1 >= num3:
        print("The largest number is " + str(num1))
    elif num2 >= num1 and num2 >= num3:
        print("The largest number is " + str(num2))
    elif num3 >= num1 and num3 >= num2:
        print("The largest number is " + str(num3))
        

largest_number()


#Task 2: Identify the Smallest
def smallest_number():
    if num1 <= num2 and num1 <= num3:
        print("The smallest number is " + str(num1))
    elif num2 <= num1 and num2 <= num3:
        print("The smallest number is " + str(num2))
    elif num3 <= num1 and num3 <= num2:
        print("The smallest number is " + str(num3))


smallest_number()

#Task 3: Equality Check
def same_number():
    if num1 == num2 and num1 == num3:
        print("All numbers are equal")
    elif num2 == num1 or num2 == num3:
        print(str(num2) + " and " + str(num2) + " are the same number")
    elif num3 == num1 or num3 == num2:
        print(str(num3) + " and " + str(num3) + " are the same number")
    elif num1 == num2 and num1 == num3:
        print(str(num1) + " and " + str(num1) + " are the same number")

same_number()