# Calculating Numbers with Functions
def _1():

    #localmenu = """
    #1) Asign values to Lists.
    #2) Print Lists.
    #3) Looping through a List."""

    menu = {
        "1":("1) Asign values to Lists.", my_add_fn()),
        "2":("2) Looping through a List.", asign_values_to_Lists()),
        "3":("3) Quit", my_quit_fn),
    }

    students = []
    score = []

   # print(localmenu)
   # op = int(input(">> "))
   #  while (op != 0):
   #    {
   #       print("hola")
   #    }

    for key in sorted(menu.keys()):
      print(key+":" + menu[key][0])

    #ans = input("Make A Choice")
    #menu.get(ans,[None,invalid])[1]()   

    # This chapter is about Definin and Using Lists and tuples.
    #print("Defining and Using Lists.\n-------------------------- ")

def asign_values_to_Lists():
    # asign to values to Lists
    print("""#Let's asign values to'scores' and 'students' both are lists
    scores = [88, 92, 78, 90, 98, 85]
    students = ["Alex", "Fabio", "Kira", "Alejandro", "Ariel", "Mercho"]""")
    #self.scores = [88, 92, 78, 90, 98, 85]
    #self.students = ["Alex", "Fabio", "Kira", "Alejandro", "Ariel", "Mercho"]

    # print Lists
    print("\n#Then let's print it out in the console:")
    #print("\t"); print(self.scores)
    #print("\t"); print(self.students)

def loop_throgh_list(self):
    # Looping through a list
    print("\n"+"""#Looping through a list:
    for x in list""")
    for x in self.scores:
        print(x)

def my_add_fn():
   print ("SUM:%s"%sum(map(int, input("Enter 2 numbers seperated by a space").split())))

def my_quit_fn():
   raise SystemExit

def invalid():
   print ("INVALID CHOICE!")

def _2():
    print("esto es chapter 3 ejercicio 2")
