## list comprehension ##
#crear listas de forma comprimida
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i+1 for i in range(8)] #a c/u de los elementos que guarda les suma 1

print(my_list)

#crear una lista con un rango
my_range = range(8)
print(my_range)
print(list(my_range))

my_list = [i*i for i in my_original_list] #potencias
print(my_list) 

#usando una funcion para meterla en la lista
def sum_five(num):
    return num +5
my_other_list = [sum_five(i) for i in range(8)]
print(my_other_list)