# Write a program that receives two numbers from the user, compares them, and returns the highest number. 
# 1 Receive two numbers from the user as integers. 
# 2 Create an if statement to compare the two numbers, and find out which number is higher. 

def max_number():
    num1 = int(input("Podaj pierwszy numer: "))
    num2 = int(input("Podaj drugi numer: "))
    if num1 > num2:
        return num1
    else:
        return num2

print(max_number())
