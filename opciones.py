class Opciones():
    indexA = []

    def op_0(self):
        print("""
        1) ENGLISH.
        2) ESPAÑOL.
        3) 中文.
        4) EXIT.""")


    def op_1(self):
        print("""
        1) esto es uno
        2) esto es dos
        3) esto es tres""")

        self.indexA.append(1)
        self.indexA.append(3)
        self.indexA.append(5)

    def lista(self):
        print(self.indexA)

