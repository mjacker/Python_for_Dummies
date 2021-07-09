import chapter1

class Chapter():
    def __init__(self) -> None:
        self.running = True

    """ Codigo del menu principal"""
    def menu(self) -> int:
        try:
            op = int(input("""
                1) Chapter 1 - Working with Numbers, Text, and Dates.
                0) Exit.
                \n"""))
        except:
            print("ERROR0")

        return op


    def choose0(self):
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
                0) Back.
                \n"""))
        except:
            print("ERROR1")
        return op

    def choose1(self, op1):
        try:
            # op1 = self.menu1()
            if op1 == 1:
                chapter1.ch1_1()
                input("enter something to go back.")
            elif op1 == 2:
                chapter1.ch1_2()
                input("enter something to go back.")
            elif op1 == 0:
                return 0

            self.choose1(self.menu1())
        except:
            print("error1_1")

    def choose_reset(self):
        pass


