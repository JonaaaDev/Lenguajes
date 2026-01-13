mi_nombre = "Jonathan"
mi_apellido = "Gimenez"
edad = 19

#--------------------------------------
# formas de imprimir variablas mi recomendada la forma 3

# la principal usando el nombre de la variable

print(mi_nombre) 
print(mi_apellido)
print(edad) 

# todo junto
print(mi_nombre, mi_apellido, edad)


print() # salto de linea (no lo tengas en cuenta)

#--------------------------------------
# forma 1

print("Te llamas", mi_nombre)
print("Te apellidas", mi_apellido)
print("Tienes", edad, "años")

# todo junto
print("Te llamas", mi_nombre, "te apellidas", mi_apellido, "tienes", edad, "años")

print() # salto de linea (no lo tengas en cuenta)

#--------------------------------------
# forma 2 usando concatenación

print("Te llamas " + mi_nombre)
print("Te apellidas " + mi_apellido)
# esto provoca un error ya que suma un texto con un número.
#print("Tienes " + edad + " Años") 

print() # salto de linea (no lo tengas en cuenta)

#--------------------------------------
# forma 3
# mi recomendada usando f-string

print(f"Te llamas {mi_nombre}")
print(f"Te apellidas {mi_apellido}")
print(f"Tienes {edad} años")

# todo junto 
print(f"Te llamas {mi_nombre} te apellidas {mi_apellido} tienes {edad} años")

print() # salto de linea (no lo tengas en cuenta)

#--------------------------------------
# forma 4 usando format

print("Te llamas {}".format(mi_nombre))
print("Te apellidas {}".format(mi_apellido))
print("Tienes {} años".format(edad))

# todo junto
print("Te llamas {} te apellidas {} tienes {} años".format(mi_nombre, mi_apellido, edad))

print() # salto de linea (no lo tengas en cuenta)

#--------------------------------------
# forma 6

print("Te llamas %s" % (mi_nombre))
print("Te apellidas %s" % (mi_apellido))
print("tienes %d años" % (edad))

# todo junto
print("Te llamas %s te apellidas %s tienes %d años" % (mi_nombre, mi_apellido, edad))
