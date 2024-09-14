#   () 	Parentheses 	
#   ** 	Exponentiation 	
#   +x  -x  ~x 	Unary plus, unary minus, and bitwise NOT 	
#   *  /  //  % 	Multiplication, division, floor division, and modulus 	
#   +  - 	Addition and subtraction 	
#   <<  >> 	Bitwise left and right shifts 	
#   & 	Bitwise AND 	
#   ^ 	Bitwise XOR 	
#   | 	Bitwise OR 	
#   ==  !=  >  >=  <  <=  is  is not  in  not in  	Comparisons, identity, and membership operators 	
#    not 	Logical NOT 	
#   and 	AND 	
#   or 	OR

a = 10
b = 20

print((a+b))
print(a**b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print(a==b) 
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

# PEMDAS - parentheses, exponents, multiplication, division, addition, subtraction. --- operation perfomance based on PAMDAS
# ()
# **
# *
# /
# +
# -

# left to right operation performace left to right

print(3 * 3 + 3 / 3 - 3)