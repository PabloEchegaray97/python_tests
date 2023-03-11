## Sets ##
#no es una estructura ordenada y no admite repetidos
#ordena sus elementos por un hash interno
#al no ser una estructura ordenada no sabremos donde estan los elementos por lo tanto no sabriamos si es correcto cuando estamos accediendo a alguno 

my_set = set() #palabra reservada constructora, creacion de un set (tipo de dato)
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un dict

my_other_set = {"Pablo","Echegaray",25}
print(type(my_other_set)) #ahora si es set, ¿que pasa?
print(len(my_other_set))

#Añadir y eliminar datos
# print(my_other_set[0])  tira error
my_other_set.add("Azul")
print(my_other_set) # un set no es una estructura ordenada

my_other_set.add("Azul")
print(my_other_set) # solo me deja agregar una vez si el valor es igual no cambia

my_other_set.remove("Pablo")
print(my_other_set)

#Busquedas
print("Azul" in my_other_set) #devuelve un booleano
print("azul" in my_other_set) #es key sensitive

#Otras operaciones
my_other_set.clear() #limpia su contenido
print(my_other_set)
print(len(my_other_set))

del my_other_set #elimina la variable / elemento

my_set = {"Pablo", "Echegaray", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # no es recomendable porque es casi aleatorio el ordenamiento del set

my_other_set = {"Kotlin", "Swift", "Python"}
#unir sets
my_new_set = my_set.union(my_other_set)
print(my_new_set)
my_new_set = my_new_set.union(my_other_set)
print(my_new_set) #sigue siendo lo mismo
my_new_set = my_new_set.union({"Javascript", "C#"})
print(my_new_set)

print(my_new_set.difference(my_set)) #elimina lo que esta en my_set del set

#5:08:36