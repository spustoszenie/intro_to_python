# Lab Task 
# Receive input that asks the user's age. Then cast the age to the integer data type and  check if the age is 18 or less. 
# 1 Create a variable that stores input that asks the user's age. 
# 2 Create an if statement that checks the age provided. If the age is greater than 18, display the message ”Access Granted” . 
# If the age is less than 18, display the message ”Access Denied". 
# Cast the data type of the variable to integer. 

age = int(input("What is your age? "))

def sprawdzenie_wieku(wiek: int):
    if age >= 18:
        print("Access granted!")
    else:
        print("Access Denied! Musisz dorosnąć małolat! :D")

sprawdzenie_wieku(age)
