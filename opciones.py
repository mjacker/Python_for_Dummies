from mjresources import choose
import menu as mn

class Opciones():
    indexA = []
    running = True

    def check(self):
        if len(self.indexA) == 0:
            mn.chapters(self)
        # elif self.indexA[0] == 0:
        #     self.running = False # condicion de salida
        elif self.indexA[-1] == 0:
            self.indexA.pop()
            self.indexA.pop()
        elif self.indexA[0] == 1:
            mn.menu_CH1(self)
        elif self.indexA[0] == 2:
            mn.menu_CH3(self)
        elif self.indexA[0] == 3:
            mn.menu_CH3(self)
        

        self.iprint()



    def read(self):
        self.indexA = input("HACIENDO NADA>>")

    def iprint(self):
        print(self.indexA)

