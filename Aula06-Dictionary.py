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

# Acessando um item do dicionario:
print(dict1["Nome"])
x = dict1.get("Nome")
print(x)

x = dict1.keys()
print(x)

x = dict1.values()
print(x)

x = dict1.items()
print(x)

if "Idade" in dict1:
    print("Sim, 'Idade' é uma das chaves deste dictionary\n")

# Alterando valores de items em um dicionario:
    
dict1["Ano"] = "2000"
#ou
dict1.update({"Ano": 2000})
print(dict1)

# 