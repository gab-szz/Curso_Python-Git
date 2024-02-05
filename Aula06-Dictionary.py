#Criando um dicionário:
dict1 = {
    "Nome":"Gabriel",
    "Nome":"Gab", # Substitui a chave anterior
    "Sobrenome":"Silvio",
    "Idade":21,
    "Ano":2002,
    "Altura":1.68,
    "Filhos":["Rynna", "Emma"]
}

# Acessando um item do dicionaro:
print(dict1["Nome"])
x = dict1.get("Nome")
print(x)

x = dict1.keys()
print(x)
dict1["Idade"] = 36
print(x)

x = dict1.values()
print(x)
dict1["Altur "] = 1.65
print(x)

x = dict1.items()
print(x)
dict1["Altura"] = 1.75
print(x)

if "Idade" in dict1:
    print("Sim, 'Idade' é uma das chaves deste dictionary")
    
