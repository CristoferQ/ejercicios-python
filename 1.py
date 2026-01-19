# 🟢 Ejercicio 1: Suma de pares

# 📌 Descripción
# Dado un número entero N, imprime la suma de todos los números pares desde 1 hasta N (inclusive).

# 🧪 Pruebas
# Entrada = 10  | Salida = 30
# Entrada = 1   | Salida = 0
# Entrada = 8   | Salida = 20

def sumaPares(n):
    sumaTotal = 0
    for i in range(1,n+1):
        if(i%2==0):
            sumaTotal += i
    return sumaTotal

print(sumaPares(10))
print(sumaPares(1))
print(sumaPares(8))