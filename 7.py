# 🟢 Ejercicio 7: Factorial usando recursión

# 📌 Descripción
# Dado un número N, calcula su factorial usando recursión.

# 🧪 Pruebas
# Entrada = 5   | Salida = 120
# Entrada = 0   | Salida = 1
# Entrada = 7   | Salida = 5040

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(0))
print(factorial(7))
