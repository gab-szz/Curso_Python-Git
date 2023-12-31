# Anotações importantes acerca dos operadores

# Operadores Aritiméticos

x = 10
y = 2

print(x + y) # Soma
print(x - y) # Subtração
print(x * y) # Multiplicação
print(x / y) # Divisão

x = 5
y = 2
print(x % y) # Resto da divisão

x = 2
y = 5
print(x ** y)# O mesmo que 2*2*2*2*2

x = 15
y = 2

print(x / y)
print(x // y) # Floor division

a = 5 + 2 * 4
print(a)

b = (5 + 2) * 4
print(b)

# Operadores de Atribuição

x = 5
print(x)

x = 5
x += 3 # x = x + 3
print(x)

x = 5
x -= 3 # x = x - 3
print(x)

x = 5
x *= 3 # x = x * 3
print(x)

x = 5
x /= 3 # x = x / 3
print(x)

x = 5
x %= 3 # x = x % 3
print(x)

x = 5
x //= 3 # x = x // 3
print(x)

x = 5
x **= 3 # x = x ** 3
print(x)

# Operações de Comparação

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Operadores Lógicos

x = 5
print(x > 3 and x < 10) # Retorna true se ambos forem verdadeiros

print(x > 3 or x < 4) # Retorna true se um for verdadeiro

print(not(x > 3 and x < 10)) # Inverte o retorno

# Operadores de Identidade

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)

# Operadores de Associação

x = ["maça", "banana"]
print("banana" in x)
print("abacaxi" not in x)

x = [150, 348, 25]
print(348 in x)