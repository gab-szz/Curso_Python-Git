# Igual a: a == b
# Diferente de: a != b
# Menor que: a < b
# Menor ou igual a: a <= b
# Maior que: a > b
# Maior ou igual a: a >= b

# IF ELIFE ELSE

a = 50
b = 200

if b < a:
    print("b é maior do que a")
    print("outra instrução no if.")
elif a == b:
    print("a é igual a b")
elif a + 150 != b:
    print("a é diferente de b") 
else:
    print("Todas as verificações retornam false")    

# Short Hand if
if b > a: print("a é maior do que b")

# Short Hand if else
print("A") if a > b else print("B")

print("Fim do programa.")

# Permite que de continuidade sem erro por não ter nada no IF
if b > a:
    pass

# AND
# OR