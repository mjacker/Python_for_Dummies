import string
import menu as mn
import random

class MyList():
    def __init__(self):
        self.myString = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
        self.output = ""

    def getString(self):
        myString = ""
        for elem in self.myString:
            myString += elem
        return myString

    def setString(self, s):
        self.myString = s

    def setOuput(self, s):
        self.output = s
    
    def ToString(self): 
        mn.clear()
        print("###                My List                  ###")
        print("-----------------------------------------------")
        print("")
        print(self.myString)
        print("")
        print("-----------------------------------------------")
        print(self.output)

ObjMyList = MyList()

def mjlist():
        # String topic
        while True:
            # Print string interface
            ObjMyList.ToString()
            print("\n\nHow do you want to do to this list?:")
            print("-----------------------------------------------")
            print("   1) Add a item to the end of the list.")
            print("   2) Extend the list by appending all items from iterable.")
            print("   0) Back.")
            stringchoise = input(">> ")

            # Len()
            if stringchoise == "1":
                ObjMyList.setOuput(f"Enter new element: ")
                ObjMyList.ToString()
                newElemToAdd = input(">> ")
                ObjMyList.myString.append(newElemToAdd)
            # "string"[n]
            elif stringchoise == "2":
                ObjMyList.setOuput(f"How many items greater or equal to 2.")
                ObjMyList.ToString()
                var_number_items = int(input("Number or item to exten: "))
                var_array_extend = []
                for i in range(var_number_items):
                    var_array_extend.append(input(f"Add item {i}: "))
                print("VAR: ", str(var_array_extend))
                print(f"Input data is: {var_array_extend}")
                ObjMyList.myString.extend(var_array_extend)
            # float random
            elif stringchoise == "3":
                ObjMyList.setString(str(random.random()))
            
            # exit from string
            elif stringchoise == "0":
                break
