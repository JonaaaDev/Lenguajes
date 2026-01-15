# antes de empezar aclarar que None no es lo mismo que cero


# el 0 es un número entero (un valor matemático)
# el None es la ausencia total de valor (el vacío)

# puntos = 0 el usuario tiene cero puntos (ya empezó a jugar)

puntos = 0 # el jugador si tiene un puntaje 
puntos = None # el usuario ni siquiera tiene puntaje (no ha jugado)

# 2. para resultados que aún no existen
ganador_de_la_partida = None # el juego sigue en curso, no hay ganador todavía

# si guardas None, python entiende que la variable está «esperando» un dato

# ***diferencias clave***
#    0 es un valor de tipo «int» (entero)
#    None es un valor de tipo «nonetype» (vacío)
#    en un examen, un 0 es una nota, un None es no haberse presentado


# None y False no son lo mismo aunque ambos se usen para condiciones

# ejemplo de interruptor
luz_encendida = False # la luz existe, pero está apagada
luz_encendida = None  # no sabemos si hay luz o la lámpara ni está conectada

# ejemplo de respuesta en un formulario
acepta_terminos = False # el usuario marcó «no» (tomó una decisión)
acepta_terminos = None  # el usuario ni siquiera ha respondido (no hay dato)


# ***comparativa rápida***
#    False es un dato lógico (está en la categoría de True/False)
#    None es un dato de estado (está en su propia categoría)
#    si una variable es False, el programa sabe que es un «no»
#    si una variable es None, el programa sabe que «falta información»
