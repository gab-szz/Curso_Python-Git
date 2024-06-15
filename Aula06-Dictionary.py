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

# Adicionar items em um dicionario 

dict1["Pai"] = "Manoel"
#ou
dict1.update({"Mae": "Flavia"})
print("\n{}".format(dict1))

# Removendo items de um dicionario

dict1.pop("Pai")
del dict1["Altura"]
dict1.popitem() #Remove o último item
print("\n{}\n".format(dict1))

dict2 = dict1 # Os dois são o mesmo dicionário, ligados pela referência
#dict2.clear() # Apaga todos os itens do dicionario
print(dict2,"\n")
#del dict2 # remove o dicionario

# Percorrendo chave e valor do dicionario

for key,value in dict1.items():
    print(key,value)

# Copiando dicionários

dict2 = dict1.copy()
print(f"copia do dicionario 1 {dict2}")

# Dicionários Alinhandos (dicionarios dentro de dicionario)

myFamily = {
    "filho1" : {
        "Nome" : "Lucas",
        "Idade" : 10
    },
    "filho2" : {
        "Nome" : "Igor",
        "Idade" : 10
    }
}