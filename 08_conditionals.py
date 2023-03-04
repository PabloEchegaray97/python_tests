## Conditionals ##
#en python se usa ":"
my_condition = False

if my_condition : #el true esta implicito no es necesario hacer == True
    print("Se ejecuta la condicion del if")

my_condition = 1

if my_condition: #no estamos limitando nada por eso si entra en la ejecucion y toma como si fuera true porque tiene algo con valor
    print("Se ejecuta la condicion del segundo if")

if my_condition == 10:
    print("Es igual a 10")

if my_condition >= 10 and my_condition < 20:
    print("Es mayor o igual que 10 y menor que 20")
elif my_condition == 1 :
    print("Es igual a 1")

if my_condition > 11 :
    print("Es mayor que 11")
else:
    print("Es menor o igual que 10")

print("La ejecucion continua")

my_string = "" #False

if my_string: 
        print("Mi cadena de texto esta vacia")

my_string = "Mi cadena de texto" #True cuando tiene algo dentro

if my_string:
    print("Mi cadena de texto no esta vacia")

if my_string == "Mi cadena de TEXTO":
    print("La cadena coincide")

my_string = ""
if not my_string:
    print("La cadena de texto es vacia")