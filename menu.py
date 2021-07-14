import chapter1
import resourses as rsc
import pygame

class Menu():
    def __init__(self) -> None:
        self.running = True

    """ Codigo del menu principal"""
    def menu(self) -> int:
        try:
            print("""
Welcome to Python for Dummies...
--------------------------------------
            """)
            op = int(input("""
    1) Chapter 1 - Working with Numbers, Text, and Dates.
    0) Exit.
                \n\t>> """))
        except:
            print("ERROR0")

        return op


    def choose0(self):
        # rsc.clear()
        op = self.menu()
        if op == 1:
            self.choose1(self.menu1())
        elif op == 0:
            self.running = False


    """ Codigo del sub-menu uno"""
    def menu1(self) -> int:
        try:
            op = int(input("""
    1) Some Built-In Python Functions for Numbers
    2) Math Module.
    3) Formatting Numbers
    4) Formatting perfecnt numbers
    5) Making multiline format strings
    6) Formatting width and alignment
    9) Concatenating strings
    0) Back.
                \n\t>> """))
        except:
            print("ERROR1")
        return op

    def choose1(self, op1):
        try:
            # op1 = self.menu1()
            rsc.clear()
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
