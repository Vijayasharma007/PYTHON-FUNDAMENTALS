print("Welcome to python pizza deliveriest!")
size=input("What size pizza do you want: S, M or L :")

bill=0
if(size=="S" or size=="s"):
    bill +=100
    print("Small pizza price is 100 Rs.")
elif(size=="M" or size=="m"):
    bill +=200
    print("Medium pizza price is 200 Rs.")
else:
    bill +=300
    print("Large pizza price is 300 Rs.")

add_pepporoni = input("Do you want pepperoni: Y or N:")
if(add_pepporoni=="Y" or add_pepporoni=="y"):
    if size=="S" or size=="s":
        bill +=30
    else:
        bill +=50

extra_cheese = input("Do you want extra cheese Y or N:")
if(extra_cheese=="Y" or extra_cheese=="y"):
    bill += 20

print(f"your final bill is {bill}")
        
