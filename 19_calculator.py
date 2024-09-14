# python calcultor using if elif else.

operator = input("Enter an operator ( + - * / ):")
num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))

if (operator== "+"):
    result=num1+num2
    print("result:",result)
elif(operator== "-"):
    result=num1-num2
    print("result:", result)
elif(operator== "*"):
    result=num1*num2
    print("result:",result)
elif(operator== "/"):
    result=num1/num2
    print("result:", result)
else:
    print(f"{operator} is not a valid operator:")