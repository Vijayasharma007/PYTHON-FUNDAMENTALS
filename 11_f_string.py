# F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value.
# f-string is a literal string, prefixed with ‘f’, which contains expressions inside braces. The expressions are replaced with their values.
# When using f-Strings to display variables, you only need to specify the names of the variables inside a set of curly braces {}. And at runtime, all variable names will be replaced with their respective values. 

# f "This is an f-string {var_name} and {var_name}"  --- syntax

name = "bob"
age = 20
print(f"Hello My name is {name} and i'm {age} year old")