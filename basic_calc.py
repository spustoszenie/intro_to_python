# Build a calculator using a Python if statement, that performs addition, subtraction,  multiplication, and division. 
# 1 Receive from the user three inputs. Two are for two numbers (integer data type), and another one is for the desired mathematical operation. 
# 2 Create an if statement that checks the operation input by the user, and performs the specified mathematical calculation. 
# In addition, create an else błock that prevents options outside the scope of the calculation. 

def basic_calc():
    num1 = int(input("Podaj numerek 1: "))
    num2 = int(input("Podaj numerek 2: "))
    co_robimy = input("Jakie działanie wykonujemy? addition, subtraction,  multiplication, and division ? + , - , *, /")
    if co_robimy == "+":
        return num1+num2
    elif co_robimy == "-":
        return num1-num2
    elif co_robimy == "*":
        return num1*num2
    else:
        return num1/num2
    
print(basic_calc())
