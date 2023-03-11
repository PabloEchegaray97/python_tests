## Loops ##

# While (hay que pasarle una condicion)
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1 # my_condition = my_condition + 1
else: #es algo propio de python poder usar un else al final del bucle
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
    elif my_condition == 16:
        print("Mi condicion es 16")
        print("La ejecucion se detiene")
        break #detiene la ejecucion

    print("Mi condicion es menor que 20")

#For se va a ejecutar cuantos elementos tenga el listado
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_set = {"Pablo","Echegaray",25}
my_dict = {
    "Nombre" : "Pablo",
    "Apellido": "Echegaray",
    "Edad": 25,
    1: "Python",
    }

for element in my_set:
    print(element)

for element in my_dict: #imprime solo las claves y NO los valores
    print(element)
    if element == "Edad":
        continue #sale del bucle for
        print("Sale del bucle en ese punto") #no se va a imprimir
    print("Se ejecuta")

for element in list(my_dict.values()):
    print(element)
else: 
    print("El bucle for ha finalizado")

#7:24:00 funciones