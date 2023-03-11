#en python camelCase no esta aceptado por convencion
#se usa SNAKE_CASE (ejemplos abajo)
# + python no compila, interpreta
#en python el tipado es dinamico

my_variable = "My string variable"
my_int_variable = 3
my_bool_variable = False
my_int_to_str_variable = str(my_int_variable) # convertimos a string una variable entera

#concatenacion en prints + se separan por comas
print("Hello", "World!")
print(my_variable, my_int_variable,my_bool_variable)
print("Este es el valor de:", my_int_variable)
print(type(my_int_to_str_variable))

# funciones del sistema 
print(len(my_variable)) #len() -- es la longitud de la variable en caracteres 

# variables en una sola linea -- no se recomienda
name, surname, alias, age = "Pablo", "Echegaray", "Pablovsky", 35
print(name, surname, alias, age)

#inputs 
input_random = input("ingresa algo") 

#cambiamos el tipo de la variable
my_int_variable = "hola"
print(my_int_variable)

# forzamos el tipo pero vuelve a sobreescribirse
address : str = "Direccion"
address = 32
print (type(address))