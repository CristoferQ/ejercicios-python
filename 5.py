# 🟢 Ejercicio 5: Detector de palíndromos

# 📌 Descripción
# Dada una palabra, determina si es un palíndromo.
# Imprime SI o NO.

# 🧪 Pruebas
# Entrada = radar   | Salida = SI
# Entrada = python  | Salida = NO
# Entrada = oso     | Salida = SI

def detectorPalindromos(palabra):
    palindromo = ""
    for i in range(len(palabra),0,-1):
        palindromo += palabra[i-1]
    if(palabra == palindromo):
        return "SI"
    else:
        return "NO"


print(detectorPalindromos("radar"))
print(detectorPalindromos("python"))
print(detectorPalindromos("oso"))

