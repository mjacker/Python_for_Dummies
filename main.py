from mjresources import choose, clear, choosen
import menu as mn
from Book2 import BK2chapter1 as CH1
from Book2 import Bk2chapter2 as CH2
from Book2 import BK2chapter3 as CH3

running = True

while running:
    # root menu
    mn.chapters()
    op = choosen(0,3)

    # termination program condition.
    if op == 0:
        running = False

    # refer to chapter numbers
    elif op == 1:
        mn.menu_CH1()
        op1 = mn.choosen(0,1)
        while op1 != 0:
            if op1 == 1:
                CH1._1()
                mn.menu_CH1()
                op1 = choosen(0,10)
            elif op1 == 0:
                pass
    elif op == 2:
        mn.menu_CH2()     
        op2 = choosen(0,10)
        while op2 != 0:
            if op2 == 0:
                pass
            elif op2 == 1:
                CH2._1()
            elif op2 == 2:
                CH2._2()
            elif op2 == 3:
                CH2._3()
            elif op2 == 4:
                CH2._4()
            elif op2 == 5:
                CH2._5()
            elif op2 == 6:
                CH2._6()
            elif op2 == 7:
                CH2._7()
            elif op2 == 8:
                CH2._8()
            elif op2 == 9:
                CH2._9()
            input("Presiona una tecla para continuar...")
            mn.menu_CH2()
            op2 = choosen(0,10)
    elif op == 3:
        mn.menu_CH3()
        op3 = choosen(0,2)
        while op3 != 0: 
            if op3 == 0:
                pass
            elif op3 == 1:
                CH3._1()
            elif op3 == 2:
                CH3._2()
            input("Presiona una tecla para continuar...")
            mn.menu_CH3()
            op3 = choosen(0,2)