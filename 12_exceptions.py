## exception handling ## 
numberOne, numberTwo = 5,1

numberTwo = "1"

#try except

try:
    print(numberOne + numberTwo) # va a fallar
    print("No se ha producido error")
except:
    print("Se ha producido un error")

#try except else
numberTwo = 3
try:
    print(numberOne + numberTwo) # va a fallar
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")

#try except else finally
numberTwo = "4"
try:
    print(numberOne + numberTwo) # va a fallar
    print("No se ha producido error")
except: #cuando hay un error se ejecuta
    print("Se ha producido un error")
else: #si no hay excepciones ejecutar esto
    print("La ejecucion continua correctamente")
finally: # se ejecuta siempre
    print("La ejecucion continua")

#Excepciones por tipo

try:
    print(numberOne + numberTwo) # va a fallar
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as exception: #caso default para controlar el error
    print("Ha ocurrido algun otro error")
    print(exception)


