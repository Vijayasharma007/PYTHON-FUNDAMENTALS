#  The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
  
# syntax --- round(number, ndigits)  //  Number - Required. The number to be rounded. // ndigits - Optional. The number of decimals to use when rounding the number. Default is 0

# rounding integer values
a = 10
print(round(a))

# rounding floating point numbers
b = 77.33
print(round(b))

# rounding even choice
print(round(5.5))

# rounding negative number
c = -4.7
d = -35.2
print(round(c))
print(round(d))

# rounding using optional digit
e = 12.768645
print(round(e,3))