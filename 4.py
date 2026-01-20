# 🟢 Ejercicio 4: Palabra invertida (sin usar reverse)

# 📌 Descripción
# Dada una palabra, imprime la palabra invertida, sin usar funciones de inversión ([::-1], reverse, etc.).

# 🧪 Pruebas
# Entrada = python  | Salida = nohtyp
# Entrada = hola    | Salida = aloh
# Entrada = a       | Salida = a

def invertirPalabra(palabra):
    palabraInvertida = ""
    for i in range(len(palabra),0,-1):
        palabraInvertida += palabra[i-1]
    return palabraInvertida

print(invertirPalabra("python"))
print(invertirPalabra("hola"))
print(invertirPalabra("a"))