## Dictionaries ##

my_dict = dict()
my_other_dict = {}
#hashmap ? diccionario 
#no existen hashmaps en python

print(type(my_dict))
print(type(my_other_dict))

#relacion clave: valor
my_other_dict = {
    "Nombre" : "Pablo",
    "Apellido": "Echegaray",
    "Edad": 25,
    1: "Python",
    }

my_dict = {
    "Nombre" : "Pablo",
    "Apellido": "Echegaray",
    "Edad": 25,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77,
    }

print (my_dict)
print (my_other_dict)

print(len(my_other_dict))
print (len(my_dict))
print(my_dict["Nombre"])

#actualizamos la clave con otro valor
my_dict["Nombre"] = "Agustin"
print (my_dict)

print(my_dict[1]) #la clave es un entero en este caso, si ponemos una cadena, da error

#agregamos un nuevo campo al diccionario
my_dict["Calle"] = "Calle Pablovsky"
print (my_dict)

#eliminar un elemento del diccionario
del my_dict["Calle"]
print (my_dict)

print("Agustin" in my_dict) #FALSE
print("Nombre" in my_dict) #TRUE analiza por clave

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

#creamos un diccionario nuevo sin valores
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) #la lista la pasamos en parentesis sino da error
print(my_new_dict)
#aca tiene sentido usar fromkeys 
#creamos un nuevo diccionario que aprovecha todas las claves del que le estamos pasando
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Pablo", "Echegaray")) #le metemos pablo echegaray a todas las claves
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ["Pablo", "Echegaray"])
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Empty")
print(my_new_dict)

print(list(my_new_dict)) #si lo transformamos en lista todas las claves se usan pero los valores no
print(tuple(my_new_dict.values())) #diferente si usamos valores y una tupla por ej
print(set(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values)) #tipo de dato dict_values
#DEBEMOS TRANSFORMARLO EN LISTA
my_values = list(my_values)
print(type(my_values)) 

print(dict.fromkeys(list(my_new_dict.values())))