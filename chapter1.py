def ch1_1():
    print("Some Built-In Python Functions for Numbers:")
    print("""
abs(x) Converts negative numbers to positive.
bin(x) converted to binary (String).
float(x) Converts to float data type.
format(x,y) Returns x formatted as directed by format string y. In modern Python you’re more
likely to use f-strings, as described later in this chapter
hex(x) Returns a string containing x converted to hexadecimal, prefixed with 0x.
int(x) Converts x to the integer data type by truncating (not rounding) the decimal point and
any digits after it.
max(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the largest.
min(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the smallest.
oct(x) Converts x to an octal number, prefixed with 0o to indicate octal.
round(x,y) Rounds the number x to y number of decimal places.
str(x) Converts number x to the string data type.
type(x) Returns a string indicating the data type of x.""")

def ch1_2():
    print("""math.acos(x) Returns the arc cosine of x in radians.
math.atan(x) Returns the arc tangent of x, in radians.
math.atan2(y, x) Returns atan(y / x), in radians.
math.ceil(x) Returns the ceiling of x, the smallest integer greater than or equal to x.
math.cos(x) Returns the cosine of x radians.
math.degrees(x) Converts angle x from radians to degrees.
math.e Returns the mathematical constant e (2.718281 . . .).""")