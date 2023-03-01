### Tuples ### son inmutables !
# una tupla es un conjunto de valores, como una lista pero estos son constantes una vez se agregan
# las tuplas no soportan reemplazos ni agregaciones pero si asignaciones a una nueva tupla
my_tuple = tuple() #constructor de clase
my_other_tuple = () 

my_tuple = (25, 1.82, "Pablo", "Echegaray", "Pablo")
my_other_tuple = ("Direccion","Casa")


print(my_tuple)
print(type(my_tuple))

print (my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("Pablo")) # la cantidad de veces que aparece
print(my_tuple.index("Echegaray")) #devuelve el primer indice que coincide

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:5]) #subtupla (podriamos asignarla a otra variable)

#de lista a tupla y al reves 
my_sum_tuple = list(my_sum_tuple) #si que podemos hacerla lista
print(type(my_sum_tuple))
#4:25:13
my_sum_tuple[3] = "Azul"
my_sum_tuple[4] = "Hola"
print(my_sum_tuple)
my_sum_tuple = tuple (my_sum_tuple)
print(type(my_sum_tuple))
print(my_sum_tuple)

#eliminar tupla (no se pueden eliminar elementos de una tupla tampoco)
del my_sum_tuple
print(my_sum_tuple) # va a tirar error 

