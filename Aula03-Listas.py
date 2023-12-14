# Listas em Python

lista = ["um", "dois", "tres", "um"]

print(lista)
print(len(lista)) # Imprime a quantidade de itens na lista

print(lista[0]) # Acessar um item da lista
print(lista[1:]) # Mesma regra dos strings

if "dois" in lista:
    print("\"Dois\" está na lista")

lista[3] = "cinco"
lista.insert(3, "quatro") # Substitui o item 3, empurrando-o pra frente na lista
lista.append("seis") # Acrescenta um item ao fim da lista
tupla = ('sete', 'oito', 'nove')
lista.extend(tupla) # Acrescentamos mais objetos

# Removendo itens
lista.remove("nove") # Remove item pelo conteúdo
lista.pop(7) # Remove item pelo índice (sem argumento remove o último)
del lista[6] # Remove pelo índice também
# del lista     - Apaga a lista inteira

print(lista)

# Imprime os itens da lista
for item in lista:
    print(item)

# Imprime os índices da lista
for indice in range(len(lista)):
    print("{} {}".format(indice, lista[indice]))

# Compreensão de lista
#  - Código sem compreensão 
novaLista = []
for x in lista:
    if "a" in x:
        novaLista.append(x)
print("Nova lista criada com os elementos: {}".format(novaLista))

# Faz uma lista com os elementos da lista que tem a
outraLista = [x for x in lista if "a" in x] 

numeros = [2,5,3,10,1,7,4,15]
numeros.sort() # Organiza em ordem crescente (numeral e alfabética)
numeros.sort(reverse = True) # Ordem decrescente 
lista.sort(key = str.lower) # Não diferencia maiusculas e minusculas na ordem

def muFunction(n):
    return abs(n - 10)
numeros.sort(key = muFunction) #Organiza de acordo com os números mais próximos de 10

# Formas de copiar elementos de uma lista para outras
copiaLista = lista.copy()
copia = list(lista)

# Juntanto listas
listaTres = lista + copiaLista
# for x in listaTres: lista.append(x)
# listaTres.extend(lista) 

lista.clear() # Limpa a lista
print(lista)