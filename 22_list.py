a = ["apple","banana","cherry"]


print(a[1])
print(a[-1])
print(a[1:3])
print(len(a))
a[1]="blackcurrent"
a.append("orange")

b=["mango","papaya","pineapple"]
a.extend(b)
a.remove("mango")

a.insert(2,"watermelon") # insert() method a new list item, without replacing any of the existing values.
print(a)

if "apple" in a:
    print("yes, 'apple' is in the fruits lisr")