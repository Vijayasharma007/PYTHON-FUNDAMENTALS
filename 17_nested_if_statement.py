print("Welcome to the rollercoaster:")
height = int(input(" What is your height in cm?"))

if(height >=120):
    print("You can ride the rollercoaster,")
    age = int(input("What is your age:"))
    if (age <=12):
        print("Please pay 50")
    elif (age <= 18):
        print("Please pay 150")
    else:
        print("Please pay 200")
else:
    print("sorry you have to grow taller before you can ride.")    