# 🟢 Ejercicio 8: Potencia usando recursión

# 📌 Descripción
# Dados dos enteros a y b, calcula a^b usando recursión (no se puede usar ** ni pow).

# 🧪 Pruebas
# Entrada = 2, 5   | Salida = 32
# Entrada = 3, 0   | Salida = 1
# Entrada = 5, 3   | Salida = 125

def potencia(n1, n2):
    if (n2 == 0):
        return 1
    else:
        return n1 * potencia(n1, n2-1)
    
print(potencia(2, 5))
print(potencia(3, 0))
print(potencia(5, 3))