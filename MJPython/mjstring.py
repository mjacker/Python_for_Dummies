import string
import menu as mn

class MyString():
    def __init__(self):
        self.myString = "This is a string example." 
        self.output = ""

    def getString(self):
        return self.myString

    def setString(self, s):
        self.myString = s

    def setOuput(self, s):
        self.output = s
    
    def ToString(self): 
        mn.clear()
        print("###                My String                ###")
        print("-----------------------------------------------")
        print("")
        print(self.myString)
        print("")
        print("-----------------------------------------------")
        print(self.output)

ObjMyString = MyString()

def mjstrings():
    mjrunning = True
    while mjrunning:
        mn.clear()
        print("### Welcome to MJPython ###")
        print("Please choose the topic that you want to practice.")
        print("1) String.")
        print("0) Exit.")
        choise = input(">> ")

        if choise == "1":
            # String topic
            while True:
                # Print string interface
                ObjMyString.ToString()
                print("\n\nWhat do you want to do to this string?:")
                print("-----------------------------------------------")
                print("   1) Print len()")
                print("   2) Get a char from string. myArray[n].")
                print("   3) Reverse.")
                print("   4) upper()")
                print("   5) lower()")
                print("   0) Back.")
                stringchoise = input(">> ")

                # Len()
                if stringchoise == "1":
                    ObjMyString.setOuput("This string has " + str(len(ObjMyString.getString())) +" chars.")
                # "string"[n]
                elif stringchoise == "2":
                    ObjMyString.setOuput(f"Enter the n position to get from string. (0, {len(ObjMyString.getString()) - 1})")
                    ObjMyString.ToString()
                    nposition = int(input(">> "))
                    if nposition < len(ObjMyString.getString()):
                        ObjMyString.setOuput("The char in the position " + str(nposition) + " is \"" + ObjMyString.getString()[nposition] + "\"")
                    else:
                        ObjMyString.setOuput("The value of n you enter is ouf of range.")
                # reversed string
                elif stringchoise == "3":
                    ObjMyString.setString(ObjMyString.getString()[::-1])
                # upper()
                elif stringchoise == "4":
                    ObjMyString.setString(ObjMyString.getString().upper())
                # lower()
                elif stringchoise == "5":
                    ObjMyString.setString(ObjMyString.getString().lower())
                # exit from string
                elif stringchoise == "0":
                    break

        elif choise == "0":
            mjrunning = False
        else:
            print("Invalid option, please try it again.")
