# 🟢 Ejercicio 3: Número más frecuente

# 📌 Descripción
# Dada una lista de números enteros, imprime el número que aparece más veces.
# Si hay empate, imprime el menor número.

# 🧪 Pruebas
# Entrada = [1,3,3,2,2]   | Salida = 2
# Entrada = [4,4,4,2,2,1] | Salida = 4
# Entrada = [7,8,9,10]    | Salida = 7

def numeroMasFrecuente(lista):
    contador = {}
    for i in lista:
        if (contador.get(i) != None):
            contador[i] = contador.get(i) + 1
        else:
            contador[i] = 1
    vecesQueAparece = max(contador.values())
    resultado = []
    for i in contador:
        if(contador[i] == vecesQueAparece):
            resultado.append(i)
    return min(resultado)
    
        
    
print(numeroMasFrecuente([1,3,3,2,2]))
print(numeroMasFrecuente([4,4,4,2,2,1]))
print(numeroMasFrecuente([8,7,9,10]))

