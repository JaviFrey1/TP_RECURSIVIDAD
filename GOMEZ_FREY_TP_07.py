# 1) Factorial recursivo y aplicación
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factoriales_hasta_n(n):
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")

# 2) Serie de Fibonacci hasta n
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_fibonacci_hasta(pos):
    for i in range(pos + 1):
        print(f"F({i}) = {fibonacci(i)}")

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4) Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_y_mostrar_binario(n):
    if n == 0:
        print("0")
    else:
        print(f"Binario: {decimal_a_binario(n)}")

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# 7) Pirámide de bloques
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Contar ocurrencias de un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)

# =============================
# Programa principal de prueba
# =============================
if __name__ == "__main__":
    print("\n1) Factoriales hasta N")
    n = int(input("Ingrese un número para calcular los factoriales: "))
    factoriales_hasta_n(n)

    print("\n2) Serie de Fibonacci")
    n = int(input("Ingrese la posición hasta la que quiere ver la serie de Fibonacci: "))
    mostrar_fibonacci_hasta(n)

    print("\n3) Potencia base^exponente")
    base = int(input("Base: "))
    exponente = int(input("Exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

    print("\n4) Conversión Decimal a Binario")
    decimal = int(input("Ingrese un número decimal: "))
    convertir_y_mostrar_binario(decimal)

    print
