## strings ##
my_string = "My string"
my_other_string = "My other string"

#hallar la longitud
print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)
my_tab_string = "Este es un string \t con tabulacion"
print(my_tab_string)
my_scape_string = "Este es un string \\n con escapado" #se usa doble barra
print(my_scape_string)

#formateo strings (la manera correcta de formatearlos sin "+")
name, surname, age = "Pablo", "Echegaray", 25
print("Mi nombre es: {} {} y tengo {} años".format(name, surname, age))
print("Mi nombre es: %s %s y tengo %d años" % (name, surname,age))
#f por delante abajo 
#interpolacion
print (f"Mi nombre es {name} {surname} y tengo {age} años") #esta es la mejor y mas rapida

#desempaquetado de caracteres [1:2:4 y asi]
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(f)

#division
language_slice = language[1:3] #cuenta las letras de la 1 a la 3 sin incluir
print(language_slice)

language_slice = language[1:] #todas excepto la 1ra
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

#reverse (dar vuelta todo)
reversed_language = language[::-1]
print(reversed_language)

#metodos o funciones del sistema
print(language.upper().isupper())
print(language.capitalize())
print(language.lower())
print(language.count("t")) #cuantas letras hay
print(len(language))
print(language.isnumeric())
print(language.startswith("Py")) #empieza con ? 