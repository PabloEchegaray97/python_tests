## Functions ##
#todo lo definido despues de la tabulacion esta en la funcion
def my_function ():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

#podemos decirle el tipo del parametro pero le va a dar igual
#como guia si puede servir
def sum_two_values(first_number: int, second_number: int):
    print (first_number + second_number)

sum_two_values(1, 2)

def sum_two_values_with_return(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

sum_two_values_with_return(1, 2)
print(sum_two_values_with_return(2,15))

my_result = sum_two_values_with_return(10,10)
print(my_result)

def print_name(name, last_name):
    print(f"{name} {last_name}") #interpolar y formatear

print_name(last_name = "Pablo", name = "Echegaray") #podemos cambiarle el orden asignandole el nombre del parametro

#podemos definir el valor por defecto de un parametro si este no lo recibe
def print_name_with_default(name, last_name, alias = "Sin alias"):
    print(f"{name} {last_name} {alias}")

print_name_with_default("Pablo", "Echegaray")
print_name_with_default("Pablo", "Echegaray", "Pablovsky")

def print_texts(*text): #al poner el asterisco podemos pasarle varios textos
    #solo del tipo de dato podemos pasarle
    print(text)

print_texts("Hola", "Python", 4)

def print_texts_upper(*texts): #no es lo mismo que una lista sino que son parametros por separado
    for text in texts:
        print(text.upper())
print_texts_upper("Hola", "Python")

def print_texts_lower(texts): #recibe una lista
    for text in texts:
        print(text.lower())

print_texts_lower(("Hola", "PYTHON")) #es una lista no son solo parametros