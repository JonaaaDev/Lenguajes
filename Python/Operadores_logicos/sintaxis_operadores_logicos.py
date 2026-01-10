# operadores lógicos devuelven un True o un False

# operador «and» significa «y»
# el and solo devuelve el True si todas las condiciones son verdaderas
print(True and True) # las dos condiciones son verdaderas
# salida: True 

# si solo una condición se cumple la condición es falsa
print(True and False) # la condición es verdadera y falsa
# salida: False

# si las dos condiciones son falsas la condición es Falsa
print(False and False) # la condición es falso y falso
# salida: False


# operador «or» significa «o»
# devuelve True si solo una condición es verdadera
print(True or True) # la condición es verdadero o verdadero
# salida True

# si uno es verdadero la condición es verdadero
print(True or False) # la condición es verdadero o falso
# salida: True

# si las dos condiciones son falsas la condición es falsa
print(False or False) # la condición es falso o falso
# salida: False


# el operador «not» devuelve True al False y False al True
# not significa no
# si la condicion es not False la condición es verdadera
print(not False) # la condición es no falso
# salida: True

# si la condicion es not True la condición es falsa
print(not True) # la condición es no verdadero
# salida: False


# operador not y el operador and

print(not False and True) # la condición es verdadero y verdadero
# salida: True

print(not False and not True) # la condición es verdadera y falso
# salida: False

# operador not y el operador or

print(not False or True) # la condición es verdadero o falso
# salida: True

print(not True or False) # la condición es falso y falso
# salida: False
