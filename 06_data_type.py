# Python has the following data types built-in by default, in these categories:

# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool


a = "Hello World"  #string
print(a,type(a))

b = 10  #int
print(b,type(b))

c = 1j  #complex
print(c,type(c))

d = ["apple","bannan","cherry"]  #list
print(d,type(d))

e = ("apple","bannan","cherry")   #tuple
print(e,type(e))

f = range(6)  #range
print(f,type(f))

g = {"name":"bob","age":1}   #dict
print(g,type(g))

h = {"apple","bannan","cherry"}
print(h,type(h))

i = True #bool
print(i,type(i))
