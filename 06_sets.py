## Sets ##

my_set = set() #palabra reservada constructora, creacion de un set (tipo de dato)
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un dict

my_other_set = {"Pablo","Echegaray",25}
print(type(my_other_set)) #ahora si es set, ¿que pasa?
print(len(my_other_set))

# print(my_other_set[0])  tira error
