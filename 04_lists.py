### Listas ###

# ¡NO SE PUEDEN CREAR CONSTANTES EN PYTHON!

my_list = list()
my_other_list = []

print (len(my_list)) #operacion comun del sistema

my_list = [12,43,23,43]
print(my_list)
print(len(my_list))

my_other_list = [25, "1.82", "Pablo", "Echegaray"]
print(my_other_list)

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4]) # es lo max que podemos hacer debido al limite de indices
print(my_other_list.count("1.82"))

#desempaquetado
age, height, name, lastname = my_other_list #necesita todos los elementos para poder desempaquetar
print(age)

#concatenar dos listas
print(my_list + my_other_list)

#metodos para listas
my_other_list.append("Empresa de pablo")
print(my_other_list)
my_other_list.insert(0, "Azul")
print(my_other_list)
my_other_list.remove("Azul")
print(my_other_list)

my_other_list.pop() #remueve el ultimo elemento
print(my_other_list)
print(my_other_list.pop()) #devuelve el ultimo elemento y lo remueve
print(my_other_list)
print(my_other_list[-1])
my_pop_element = my_other_list.pop(1) #remueve la primera posicion y lo guarda en una variable
print(my_other_list)
print(my_pop_element)
del my_other_list[1] #se elimina el elemento en la posicion seleccionada
print(my_other_list)
my_other_list[0] = 26
my_new_list = my_other_list.copy() #copiamos la lista antes de eliminarla
print(my_other_list)
my_other_list.clear() #limpia completamente la lista
print(my_other_list)
print(my_new_list)

my_new_list.append("hola")
my_new_list.reverse() #invertir la lista
print(my_new_list)

my_list.sort() #ordena de menor a mayor
print(my_list)
print(my_list[1:3]) #sublista usando los indices