from MJPython import mjstring as MJP1
from MJPython import mjrandom as MJR1
from MJPython import mjlist as MJL1
import menu as mn

def mjMain():
    mjrunning = True
    while mjrunning:
        mn.clear()
        print("### Welcome to MJPython ###")
        print("Please choose the topic that you want to practice.")
        print("1) String.")
        print("2) Random.")
        print("3) List.")
        print("0) Exit.")
        choise = input(">> ")

        if choise == "1":
             MJP1.mjstrings()
        elif choise == "2":
            MJR1.mjrandom()
        elif choise == "3":
            MJL1.mjlist()
        elif choise == "0":
            mjrunning = False
        else:
            print("Invalid option, please try it again.")