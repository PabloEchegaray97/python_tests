## Classes ##
class MyEmptyPerson: #por convencion las clases se definen con camelcase
    pass

#print(MyEmptyPerson)
#print(MyEmptyPerson())

class Person:
    def __init__(self, name, lastname, alias="Sin alias"): #sirve para crear un constructor de clase
        #self.name = name #con self creamos las propieades con el argumento para luego despues usarlos
        #self.lastname = lastname
        self.full_name = f"{name} {lastname} {alias}"
        self.__name = name
        self.__lastname = lastname
    def get_name (self):
        return self.__name
    def walk(self):
        print(f"{self.full_name} Esta caminando") #instanciamos la clase

my_person = Person("Pablo","Echegaray", "Pablovsky")
print(my_person.full_name)
my_person.walk()
my_other_person = Person("Matias", "Muller","Mati")
print(my_other_person.full_name)
my_other_person.full_name = "Mati el loco de los cartitas" #no hace falta usar el constructor nuevamente podemos reemplazar el valor con solo una cadena
print(my_other_person.full_name)
#print(my_person.name) #no puede acceder directamente al nombre
print(my_person.get_name()) #usando el metodo get podemos acceder al nombre
