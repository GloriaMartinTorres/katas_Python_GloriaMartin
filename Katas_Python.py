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

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.    

while True:
    try:
        entrada = input("Introduce tu edad: ")
        edad = int(entrada)

        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango")

        print(f"Tu edad es: {edad}")
        break

    except ValueError as e:
        print("Error: Debes introducir un número entero válido entre 0 y 120.")

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
        
def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

texto = "Buenos dias"
longitud = longitudes_palabras(texto)
print(longitud)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minus(caracteres):
    letras = map(str.lower, filter(str.isalpha, caracteres))

    unicos = set(letras)
       
    resultado = list(map(lambda c: (c.upper(), c.lower()), unicos))
    
    return resultado

letras1 = "AabBCcDe"
print(letras_mayus_minus(letras1))

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrar_por_letra(palabras, letra):
    
    letra = letra.lower()
    
    return list(filter(lambda palabra: palabra.lower().startswith(letra), palabras))

animales = ["perro", "Gato", "oso", "periquito", "pez"]
letra_p = filtrar_por_letra(animales, "p")
print(letra_p)

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

def sumar_tres(lista):
    return list(map(lambda x: x + 3, lista))

numeros = [2, 3, 5, 8]
suma1 = sumar_tres(numeros)
print(suma1)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

ejemplo1 = "Todos los días salgo con mi perra"
palabras1 = palabras_mas_largas(ejemplo1, 4)
print(palabras1)

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda acc, d: acc * 10 + d, digitos, 0)

print(lista_a_numero([5, 7, 2]))

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter()

def estudiantes_destacados(estudiantes):
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

estudiantes = [
    {"nombre": "Ana", "edad": 30, "calificacion": 98},
    {"nombre": "Luis", "edad": 22, "calificacion": 80},
    {"nombre": "Marta", "edad": 40, "calificacion": 90},
    {"nombre": "Carlos", "edad": 51, "calificacion": 78},
    {"nombre": "Elena", "edad": 20, "calificacion": 92}]

destacados = estudiantes_destacados(estudiantes)

for e in destacados:
    print(e)

# 19. Crea una función lambda que filtre los números impares de una lista dada.
 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

datos = [2, "hola", 3, "perro", 6, 9.5, "casa", 30]

solo_enteros = list(filter(lambda x: isinstance(x, int), datos))

print(solo_enteros)

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

def cubo(numero):
    f = lambda x: x ** 3
    return f(numero)
    
print(cubo(6))

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce() .

from functools import reduce

def producto_total(lista):
    return reduce(lambda acc, x: acc * x, lista, 1)

numeros = [2, 5, 8, 6]
resultado = producto_total(numeros)
print(resultado)    

# 23. Concatena una lista de palabras. Usa la función reduce() .

from functools import reduce

palabras = ["Hola", "mundo", "desde", "Python"]

resultado = reduce(lambda x, y: x + " " + y, palabras)

print(resultado)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

valores = [80, 30, 10, 7]

resultado = reduce(lambda x, y: x - y, valores)

print(resultado)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto):
    return len(texto)


cadena = "Hoy sale el sol"
resultado = contar_caracteres(cadena)

print(resultado)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda a, b: a % b

resultado = resto(100, 6)
print(resultado)

# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(numeros):
    if not numeros:  
        return 0
    return sum(numeros) / len(numeros)

lista = [5, 13, 30, 21]
resultado = calcular_promedio(lista)

print(resultado)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # si no hay duplicados

# Ejemplo de uso
datos = [3, 1, 4, 2, 5, 3, 6]
resultado = primer_duplicado(datos)

print(resultado)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.

def enmascarar(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

dato = 123456789
resultado = enmascarar(dato)

print(resultado)

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
        p1 = palabra1.replace(" ", "").lower()
        p2 = palabra2.replace(" ", "").lower()
    
        return sorted(p1) == sorted(p2)


print(son_anagramas("Roma", "amor"))   
print(son_anagramas("hola", "mundo"))

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

def buscar_nombre():
    try:
        
        entrada = input("Introduce una lista de nombres separados por comas: ")
        lista_nombres = [nombre.strip() for nombre in entrada.split(",")]
        
        
        nombre_buscar = input("Introduce el nombre a buscar: ").strip()
        
       
        if nombre_buscar in lista_nombres:
            print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no se encuentra en la lista.")
    
    except ValueError as e:
        print("Error:", e)

buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

def buscar_empleado(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    return "La persona no trabaja aquí."

lista_empleados = [
    {"nombre": "Ana Martín", "puesto": "Gerente"},
    {"nombre": "Sara Pérez", "puesto": "Desarrolladora"},
    {"nombre": "Marta Rodríguez", "puesto": "Diseñadora"}
]

print(buscar_empleado("Sara Pérez", lista_empleados))
print(buscar_empleado("Juan Torres", lista_empleados))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = sumar_listas(lista1, lista2)
print(resultado)

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
# Código a seguir:
# 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
# 6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.
#Caso de uso:
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.


class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    # 2. Crecer tronco
    def crecer_tronco(self):
        self.tronco += 1

    # 3. Nueva rama
    def nueva_rama(self):
        self.ramas.append(1)

    # 4. Crecer ramas
    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    # 5. Quitar rama por posición
    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida")

    # 6. Información del árbol
    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
    
# CASO DE USO

# 1. Crear un árbol
arbol = Arbol()

# 2. Crecer el tronco
arbol.crecer_tronco()

# 3. Añadir una nueva rama
arbol.nueva_rama()

# 4. Crecer todas las ramas
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama en la posición 2
arbol.quitar_rama(2)

# 7. Obtener información
info = arbol.info_arbol()
print(info)


# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
# poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
#Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".


class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # 4. Agregar dinero
    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        self.saldo += cantidad

    # 2. Retirar dinero
    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para realizar el retiro.")
        self.saldo -= cantidad

    # 3. Transferir dinero desde otro usuario
    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        if cantidad > otro_usuario.saldo:
            raise ValueError("El usuario emisor no tiene suficiente saldo.")
        
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

# CASO DE USO


# 1. Crear usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 a Bob
bob.agregar_dinero(20)

# 3. Transferir 80 de Bob a Alicia
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 de Alicia
alicia.retirar_dinero(50)

# Mostrar resultados finales
print("Saldo Alicia:", alicia.saldo)
print("Saldo Bob:", bob.saldo)     


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# Código a seguir:
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto

from collections import Counter

# 1. Contar palabras
def contar_palabras(texto):
    palabras = texto.lower().split()
    return dict(Counter(palabras))


# 2. Reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)


# 3. Eliminar palabra
def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return " ".join(palabras_filtradas)


# 4. Función principal
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)

    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se requieren palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])

    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se requiere una palabra para eliminar.")
        return eliminar_palabra(texto, args[0])

    else:
        raise ValueError("Opción no válida. Usa: contar, reemplazar, eliminar.")
    

# CASO DE USO

texto = "los perros se revuelcan en la hierba"

# Contar palabras
print(procesar_texto(texto, "contar"))

# Reemplazar palabra
print(procesar_texto(texto, "reemplazar", "perros", "gatos"))

# Eliminar palabra
print(procesar_texto(texto, "eliminar", "hierba"))


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento_dia(hora):
    if 0 <= hora < 6:
        return "Es de noche"
    elif 6 <= hora < 12:
        return "Es de día"
    elif 12 <= hora < 20:
        return "Es de tarde"
    elif 20 <= hora < 24:
        return "Es de noche"
    else:
        return "Hora no válida"
    
try:
    hora = int(input("Introduce la hora (0-23): "))
    resultado = determinar_momento_dia(hora)
    print(resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente        

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "calificación no válida"
    
try:
    nota = int(input("Introduce la calificación (0-100): "))
    resultado = calificacion_texto(nota)
    print("Calificación:", resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).        

import math

def calcular_area(figura, datos):
    figura = figura.lower()

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        return "Figura no válida"
    
print(calcular_area("rectangulo", (10, 5)))
print(calcular_area("circulo", (3,)))
print(calcular_area("triangulo", (8, 4)))

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.

# 1. Precio original
try:
    precio = float(input("Introduce el precio original del artículo: "))

    # 2. Cupón de descuento
    tiene_cupon = input("¿Tienes cupón de descuento? (sí/no): ").strip().lower()

    descuento = 0

    # 3 y 4. Si tiene cupón, pedir valor y validarlo
    if tiene_cupon == "sí" or tiene_cupon == "si":
        descuento = float(input("Introduce el valor del cupón de descuento: "))

        if descuento <= 0:
            print("Cupón no válido. No se aplicará descuento.")
            descuento = 0

    elif tiene_cupon != "no":
        print("Respuesta no válida. Se asumirá que no hay descuento.")

    # 5. Calcular precio final
    precio_final = precio - descuento

    if precio_final < 0:
        precio_final = 0

    print(f"El precio final de la compra es: {precio_final:.2f}€")

except ValueError:
    print("Error: introduce valores numéricos válidos.")