# Calculating Numbers with Functions
def ch1_1():
    print("Some Built-In Python Functions for Numbers:")
    print("""
1) abs(x) Converts negative numbers to positive.
2) bin(x) converted to binary (String).
3) float(x) Converts to float data type.
4) format(x,y) Returns x formatted as directed by format string y. In modern Python you’re more
likely to use f-strings, as described later in this chapter
5) hex(x) Returns a string containing x converted to hexadecimal, prefixed with 0x.
6) int(x) Converts x to the integer data type by truncating (not rounding) the decimal point and
any digits after it.
7) max(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the largest.
8) min(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the smallest.
9) oct(x) Converts x to an octal number, prefixed with 0o to indicate octal.
10) round(x,y) Rounds the number x to y number of decimal places.
11) str(x) Converts number x to the string data type.
12) type(x) Returns a string indicating the data type of x.\n\n\n""")

    # number = 0.0
    # try: 
    #     number = int(input("\n\nPlease input a negative number: "))
    #     print(f"\nusing abs({number}). \n\t The result of this function is: ", abs(number))
    # except:
    #     print("Please, try it again.")

# Still More Math Functions
def ch1_2():
    print("""
1) math.acos(x) Returns the arc cosine of x in radians.
2) math.atan(x) Returns the arc tangent of x, in radians.
3) math.atan2(y, x) Returns atan(y / x), in radians.
4) math.ceil(x) Returns the ceiling of x, the smallest integer greater than or equal to x.
5) math.cos(x) Returns the cosine of x radians.
6) math.degrees(x) Converts angle x from radians to degrees.
7) math.e Returns the mathematical constant e (2.718281 . . .).""")

# Formatting Numbers
def ch1_3():
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
def ch1_4():
    sales_tax_rate = 0.065
    print(f"Sales Tax Rate {sales_tax_rate:.2%}")


# Making multiline format strings
def ch1_5():
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
def ch1_6():
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
    s_subtotal = "$" + f"{subtotal:.,2f}"
    s_sales_tax = "$" + f"{sales_tax:.,2f}"
    s_total = "$" + f"{total:.,2f}"

    # Output the string with dollar sign already attached
    output = f"""\n\n Output the string with dollar sign already attached
    Subtotal:  ${s_subtotal:>9}
    Sales Tax: ${s_sales_tax:>9}
    Total:     ${s_total:}
    """
    x = int(input("press any key to continue..."))


# Binary, octal, and hexadecimal numbers
def ch1_7():
    x = 255
    print(bin(x))
    print(oct(x))
    print(hex(x))

    print(0b11111111)
    print(0o337)
    print(0xff)


# Complex number
def ch1_8():
    print("""complex(real, imaginary)""")
    z = complex(2, -3)
    print(z)

# Complex number
def ch1_9():
    print("Manipulating Strings:")
    print("Concatenating strings")
    first_namem = "Alan"
    middle_init = "C"
    last_name = "Simpson"
    full_name = first_namem + middle_init + last_name
    print(full_name)
