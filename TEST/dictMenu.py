#python 3.7.1
def PrintMenu():
    # Printing all options from menu
    for key in (sorted(menu.keys()))[1:]:
        print(key+") " + menu[key][0])
    
    # Printing the exit option.
    for key in (sorted(menu.keys()))[:1]:
        print(key+") " + menu[key][0])
    

def UserInput() -> str:
    print(">> " , end = '')
    varUserInput = input()
    # If options exist, then execute program.
    if varUserInput in menu.keys():
        menu[varUserInput][1]()
        return varUserInput
    else:
        print("Warning: Option not available.")
        return "-1"

def SayHello():
    print("I am saying Hello")

def SayBye():
    print("I am saying Bye bye.. ")

def NotImplemented():
    print("Sorry, but this is not implemented.")

def ExitProgram():
    quit()

menu = {
    "1": ("Say Hello.", SayHello), 
    "2": ("Say bye.", SayBye),
    "3": ("Not implemented.", NotImplemented),
    "0": ("Exit.", ExitProgram)}
exit = 0

while (True):
    PrintMenu()
    UserInput()




