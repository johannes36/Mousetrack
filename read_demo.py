import pickle
 
class MyClass():
    def __init__(self, param):
        self.param = param
 
    def load_object(filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)
 
obj = MyClass.load_object("demo.pickle")
 
# print(obj)
# print(isinstance(obj, MyClass))


with open("demo.txt","r") as datei:
    # für jede Zeile in der Datei...
    for name in datei:
        # erster Eintrag (Index 0) aus der Liste repräsentiert den Namen
        move_x = name[0,:]
        # zweiter Eintrag (Index 1) aus der Liste repräsentiert das Alter
        move_y = name[1,:]
        # dritter Eintrag (Index 2) aus der Liste repräsentiert das Geschlecht
        click_x = name[2,:]

        click_y = name[3,:]


print(type(move_x))
        # Ausgabe der Werte in einem Satz. 
# print('x-Pos:', move_x[0])
# print('y-Pos:', move_y[0])
# print('x-Klick:', click_x[0])
# print('y-Klick:', click_y[0])
# print(move_x)