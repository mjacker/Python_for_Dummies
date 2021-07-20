import chapter1
from mjresources import choose, clear

class Menu():
    def __init__(self) -> None:
        self.running = True

    # Menu principal
    def menu0(self):
        print("""
Welcome to Python for Dummies...
--------------------------------------
    1) Chapter 1 - Working with Numbers, Text, and Dates.
    0) Exit.""")


    # Menu 1
    def menu1(self):
        print("""
    1) Some Built-In Python Functions for Numbers
    2) Math Module.
    3) Formatting Numbers
    4) Formatting perfecnt numbers
    5) Making multiline format strings
    6) Formatting width and alignment
    9) Concatenating strings
    0) Back.""")


    def choose1(self, op1):
        try:
            # op1 = self.menu1()
            clear()
            if op1 == 1:
                chapter1.ch1_1()
            elif op1 == 2:
                chapter1.ch1_2()
            elif op1 == 3:
                chapter1.ch1_3()
            elif op1 == 4:
                chapter1.ch1_4()
            elif op1 == 5:
                chapter1.ch1_5()
            elif op1 == 6:
                chapter1.ch1_6()
            elif op1 == 9:
                chapter1.ch1_9()
            elif op1 == 0:
                return 0

            input("\n\n\tpress any key to go back...")

            self.choose1(self.menu1())
        except:
            print("error1_1")

    def choose_reset(self):
        pass

    def start(self):
        self.menu0()
        op = choose(1)

        if op == 1 :
            self.menu1()
            op2 = choose(6)
            if op2 == 1:
                chapter1.ch1_1()
            elif op2 == 2:
                chapter1.ch1_2()
            elif op2 == 3:
                chapter1.ch1_3()
            elif op2 == 4:
                chapter1.ch1_4()
            elif op2 == 5:
                chapter1.ch1_5()
            elif op2 == 6:
                chapter1.ch1_6()
            elif op2 == 9:
                chapter1.ch1_9()
        elif op == 0:
            print("Saliendo del programa")
            self.running = False
            
