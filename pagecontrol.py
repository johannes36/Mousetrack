#funktionen, die Wechsel zwischen den unterschiedlichen Seiten des GUI ermöglichen
class PageControl:
    def __init__(self, number):
        self.number = number
        print("initialisiert" + str(self.number))

    def showNextPage(self, test, swecond):
        print("nachste seite ist: " + str(test))
        print("\n")
        print(swecond)

    def showPreviousPage(self):
        pass
