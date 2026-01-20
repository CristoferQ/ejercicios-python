# 🟢 Ejercicio 2: Contar vocales

# 📌 Descripción
# Dada una cadena de texto, cuenta cuántas vocales (a, e, i, o, u) contiene.
# No distingue entre mayúsculas y minúsculas.

# 🧪 Pruebas
# Entrada = Hola Mundo  | Salida = 4
# Entrada = PYTHON      | Salida = 1
# Entrada = bcdfg       | Salida = 0

def contarVocales(palabra):
    contador = 0
    vocales = ['a','e','i','o','u']
    for i in palabra.lower():
        if (i in vocales):
            contador += 1
    return contador

print(contarVocales("Hola Mundo"))
print(contarVocales("PYTHON"))
print(contarVocales("bcdfg"))