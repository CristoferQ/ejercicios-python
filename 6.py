# 🟢 Ejercicio 6: Suma de los primeros N números usando recursión

# 📌 Descripción
# Dado un entero N, calcula la suma de los números desde 1 hasta N usando recursión.

# 🧪 Pruebas
# Entrada = 5   | Salida = 15
# Entrada = 1   | Salida = 1
# Entrada = 10  | Salida = 55


def sumaPrimerosNumeros(n):
    if(n == 1):
        return 1
    else:
        return n + sumaPrimerosNumeros(n-1)

print(sumaPrimerosNumeros(5))
print(sumaPrimerosNumeros(1))
print(sumaPrimerosNumeros(10))