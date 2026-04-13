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