# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(string):
    """Esta función recibe una cadena de texto y devuelve un diccionario con las frecuencias de cada letra de la cadena.
    Args:
        string (str): cadena de texto
    """
    frecuencias = {}

    for caracter in string:
        if caracter != " ":  
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
    
    return frecuencias

cadena = "hola, mundo"
resultado = frecuencia_letras(cadena)
print(resultado)

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doble(num):
    """
    Calcula el doble de una lista de números

    Args:
        num (int): número que desea multiplicar por dos.
    """
    return list(map(lambda x: x * 2, num))


numeros = [1,2,3,4,5]
print(doble(numeros))

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    resultado = []
    
    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            resultado.append(palabra)
    
    return resultado


palabras = ["persona", "carpeta", "personal", "personalizar", "mesa"]
objetivo = "persona"

print(filtrar_palabras(palabras, objetivo))

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

a = [48, 50, 5]
b = [20, 32, 3]

print(diferencia_listas(a, b))

# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluar_notas(numeros, nota_aprobado=5):
    if not numeros:
        raise ValueError("La lista de números no puede estar vacía")
    
    media = sum(numeros) / len(numeros)
    
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    return media, estado

notas1 = [5, 7, 4, 8]
resultado1 = evaluar_notas(notas1)
print(resultado)

notas2 = [3, 5, 2, 4]
resultado2 = evaluar_notas(notas2)
print(resultado2)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(6))

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: str(t), lista_tuplas))

datos = [("hola", "adiós"), ("perros", "gatos"), (1, 2, 3)]
resultado = tuplas_a_strings(datos)
print(resultado)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        resultado = num1 / num2
        print(f"División exitosa. Resultado: {resultado}")
    
    except ValueError:
        print("Error: Debes introducir valores numéricos válidos.")
    
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Ejecutar la función
dividir_numeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

mascotas = ["Perro", "Gato", "Tigre", "Tortuga", "Oso"]
resultado = filtrar_mascotas(mascotas)

print(resultado)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""
    pass

def calcular_promedio(numeros):
    if not numeros:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    
    return sum(numeros) / len(numeros)

try:
    lista = [2, 5, 8, 6]  
    promedio = calcular_promedio(lista)
    print(f"El promedio es: {promedio}")

except ListaVaciaError as e:
    print(f"Error: {e}")

    