# TUPLAS
# Tuplas são imutáveis

tupla = ("um", "dois", "tres", "quatro")
tupla2 = ("é uma tupla",)
tupla3 = ("não é uma tupla")
print(tupla)
print(type(tupla3))
tupla4 = ("zero", 1, 2.0, True)
print(tupla4)
tupla5 = tuple(("cinco", 6))

# Acessando dados de uma tupla
#   Mesma coisa das listas

# Atualizando elementos de uma tupla
#  Temos que converter para uma lista para atualizar elementos de uma tupla

x = ("Gabriel", "Danny", "Arthur")
print(x)

y = list(x)
y[1] = "Danielle"
x = tuple(y)
print(x)

# y = list(x)
# y.append("Lucas")
# x = tuple(y)

y = ("Lucas",)
x += y
print(x)

y = list(x)
y.remove("Arthur")
x = tuple(y)
print(x)

del x

# Descompactando tuplas

(um, dois, *tres_e_quatro) = tupla
print(type(um))

# Percorrendo valores de uma tupla

tupla1 = ("Gabriel", "Danny", "Arthur")
print(tupla1)

# for x in tupla1:
#     print(x)

# for i in range(len(tupla1)):
#     print(tupla1[i])

i = 0
while i < len(tupla1):
    print(tupla1[i])
    i += 1

# Juntando tuplas
# tupla 3 = tupla1 + tupla2

