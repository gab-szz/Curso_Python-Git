# Uma coleção de itens não ordenada e não indexada
# Não permitem valores duplicados, ignorando um segundo valor igual e os elementos não podem ser alterados

# Criando Sets
set1 = {"um", "dois", "três"}
set2 = {"abc", 2024, True}
set3 = set(("cindo", "seis"))

# Acessando item

for i in set1:
    print(i)

# Adicionando elementos
    
set1.add("quatro")
set1.update(set3)
print(set1)