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
