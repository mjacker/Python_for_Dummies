# Calculating Numbers with Functions
def _1():
    print("Some Built-In Python Functions for Numbers:")
    print("""
1)\t abs(x)\t\t Converts negative numbers to positive.
2)\t bin(x)\t\t converted to binary (String).
3)\t float(x)\t Converts to float data type.
4)\t format(x,y)\t Returns x formatted as directed by format string y. In modern Python you’re more
likely to use f-strings, as described later in this chapter
5)\t hex(x)\t\t Returns a string containing x converted to hexadecimal, prefixed with 0x.
6)\t int(x)\t\t Converts x to the integer data type by truncating (not rounding) the decimal point and
any digits after it.
7)\t max(x,y,z ...)\t Takes any number of numeric arguments and returns whichever one is the largest.
8)\t min(x,y,z ...)\t Takes any number of numeric arguments and returns whichever one is the smallest.
9)\t oct(x)\t\t Converts x to an octal number, prefixed with 0o to indicate octal.
10)\t round(x,y)\t Rounds the number x to y number of decimal places.
11)\t str(x)\t\t Converts number x to the string data type.
12)\t type(x)\t Returns a string indicating the data type of x.\n\n\n""")

    # number = 0.0
    # try: 
    #     number = int(input("\n\nPlease input a negative number: "))
    #     print(f"\nusing abs({number}). \n\t The result of this function is: ", abs(number))
    # except:
    #     print("Please, try it again.")

# Still More Math Functions
def _2():
    print("""
1) math.acos(x) Returns the arc cosine of x in radians.
2) math.atan(x) Returns the arc tangent of x, in radians.
3) math.atan2(y, x) Returns atan(y / x), in radians.
4) math.ceil(x) Returns the ceiling of x, the smallest integer greater than or equal to x.
5) math.cos(x) Returns the cosine of x radians.
6) math.degrees(x) Converts angle x from radians to degrees.
7) math.e Returns the mathematical constant e (2.718281 . . .).""")

# Formatting Numbers
def _3():
    print("""
1) Formatting with f-strings
""")
    username = "Alan"
    print(f"Hellos {username}")

    """Second example"""
    print("""
    EXAMPLE 2"
    ----------------------------------------------
    unit_price= 49.99
    quantity = 10
    print(f"Subtotal: ${quantity * unit_price}")
    """)
    unit_price= 49.99
    quantity = 30
    print(f"Subtotal: ${quantity * unit_price}")

    print("\n If you add :, like this")
    print("""    print(f"Subtotal: ${quantity * unit_price:,}")
    it will change form comma to dots.""")
    print(f"Subtotal: ${quantity * unit_price:,}")

    print("\n If you need only two decimal places, you can use .2f")
    print(f"Subtotal: ${quantity * unit_price:,.2f}")


# Formatting perfecnt numbers
def _4():
    sales_tax_rate = 0.065
    print(f"Sales Tax Rate {sales_tax_rate:.2%}")


# Making multiline format strings
def _5():
    unit_price = 49.95
    quantity = 32
    sales_tax_rate = 0.065
    subtotal = quantity * unit_price
    sales_tax = sales_tax_rate * subtotal
    total = subtotal + sales_tax
    output = f"""
    Subtotal:  ${subtotal:,.2f}
    Sales Tax: ${sales_tax:,.2f}
    Total:     ${total:,.2f}
    """
    print(output)

# Formatting width and alignment
# """ es cuando se usa por ejemplo :>20 """
def _6():
    unit_price = 49.95
    quantity = 32
    sales_tax_rate = 0.065
    subtotal = quantity * unit_price
    sales_tax = sales_tax_rate * subtotal
    total = subtotal + sales_tax
    output = f"""
    Subtotal:  ${subtotal:>9,.2f}
    Sales Tax: ${sales_tax:>9,.2f}
    Total:     ${total:,.2f}
    """

    print(output)

    print("Para corregir de que el signo de dolar")


    # Forat amounts to whos as string with Leading dollar sign

    # Output the string with dollar sign already attached


# Binary, octal, and hexadecimal numbers
def _7():
    x = 255
    print(bin(x))
    print(oct(x))
    print(hex(x))

    print(0b11111111)
    print(0o337)
    print(0xff)


# Complex number
def _8():
    print("""complex(real, imaginary)""")
    z = complex(2, -3)
    print(z)

# Complex number
def _9():
    print("Manipulating Strings:")
    print("Concatenating strings")
    first_namem = "Alan"
    middle_init = "C"
    last_name = "Simpson"
    full_name = first_namem + middle_init + last_name
    print(full_name)
