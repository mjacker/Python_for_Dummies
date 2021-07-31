import chapter1
from mjresources import choose, clear, choosen

def __init__(self) -> None:
    self.running = True
    menu_index = []


# Menu principal
def chapters(self):
    print("""
Welcome to Python for Dummies...
--------------------------------------
1) Chapter 1 - Getting Started with Python.
2) Chapter 2 - Understanding Python Building Blocks.
3) Chapter 3 - Working with Python Libraries
0) Exit.""")
    self.indexA.append(choosen(0, 3))

def menu_CH1(self):
    print("""
1) Tipos de datos.
2) Cualquier batata.
0) Back.""")
    self.indexA.append(choosen(0, 2))


def menu_CH2(self):
    print("""
1) Some Built-In Python Functions for Numbers
2) Math Module.
3) Formatting Numbers
4) Formatting perfecnt numbers
5) Making multiline format strings
6) Formatting width and alignment
9) Concatenating strings
0) Back.""")
    self.indexA.append(choosen(0, 9))


def menu_CH3(self):
    print("""
1) Working with External Files
2) Juggling JSON Data.
0) Back.""")
    self.indexA.append(choosen(0, 2))