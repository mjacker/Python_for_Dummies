from mjresources import choose, clear, choosen

# Menu principal
def chapters():
    print("""
Welcome to Python for Dummies...
--------------------------------------
1) Chapter 1 - Getting Started with Python.
2) Chapter 2 - Understanding Python Building Blocks.
3) Chapter 3 - Working with Python Libraries
0) Exit.""")


def menu_CH1():
    print("""
1) Python Data Types.
0) Back.""")


def menu_CH2():
    print("""
1) Some Built-In Python Functions for Numbers
2) Math Module.
3) Formatting Numbers
4) Formatting perfecnt numbers
5) Making multiline format strings
6) Formatting width and alignment
9) Concatenating strings
0) Back.""")


def menu_CH3():
    print("""
1) Working with External Files
2) Juggling JSON Data.
0) Back.""")

def square(string):
    print("╒"+"═"*20+"╕")
    print("│"+f"       {string}       " +"│")
    print("╘"+"═"*20+"╛")

def line():
    print("═"*60)