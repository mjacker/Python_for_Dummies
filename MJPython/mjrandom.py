import string
import menu as mn
import random

class MyRandom():
    def __init__(self):
        self.myString = "Here will be generated the random number:" +  str(random.randint(1, 100))
        self.output = ""

    def getString(self):
        return self.myString

    def setString(self, s):
        self.myString = s

    def setOuput(self, s):
        self.output = s
    
    def ToString(self): 
        mn.clear()
        print("###                My Random                ###")
        print("-----------------------------------------------")
        print("")
        print(self.myString)
        print("")
        print("-----------------------------------------------")
        print(self.output)

ObjMyRandom = MyRandom()

def mjrandom():
        # String topic
        while True:
            # Print string interface
            ObjMyRandom.ToString()
            print("\n\nHow do you want to generate a random namber?:")
            print("-----------------------------------------------")
            print("   1) Between [0, 100].")
            print("   2) Between [a, b].")
            print("   3) Float random [0, 1).")
            print("   0) Back.")
            stringchoise = input(">> ")

            # Len()
            if stringchoise == "1":
                ObjMyRandom.setString(str(random.randint(0, 100)))
            # "string"[n]
            elif stringchoise == "2":
                ObjMyRandom.setOuput(f"Enter interval values for a and b.")
                ObjMyRandom.ToString()
                var_a = int(input("Value for a: "))
                var_b = int(input("Value for b: "))
                ObjMyRandom.setString(random.randint(var_a, var_b))
            # float random
            elif stringchoise == "3":
                ObjMyRandom.setString(str(random.random()))
            
            # exit from string
            elif stringchoise == "0":
                break
