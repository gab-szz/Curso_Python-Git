import random

#Definindo o tipo de variável
# - Pode ser utilizado para converter um tipo para outro (casting)
varString = str(5)
varInt = int(5)
varFloat = float(5)

print("Tipos das variáveis: {} {} {}".format(type(varString), type(varInt), type(varFloat)))

#Definindo valores simultaneamente

a, b, c = "A", "B", "C"

a = b = c = "Mesmo valor"

tupla = ["A", "B", "C"]

#Imprimindo string + inteiro
texto = "O valor é: "
numero = 20

print(texto + str(numero))

#Definindo variável global dentro de função
def myFunc():
    global z
    z = "letra z"
myFunc()
print(z)

#Numero aleatorio
alea = random.randrange(1,10)
print(alea)

# Strings
# - Strings são arrays

txt = "um dois tres"

if "um" in txt:
    print("Tem 'um' no texto.")
if "quatro" not in txt:
    print("Nao tem 'quatro' no texto")

# Pegando do um ao dois
print(txt[0:7])

# Pegando o tres de traz pra frente
print(txt[-4:12])

# Caixa alta e baixa
print(txt.upper())
print(txt.lower())

# Remover espaceamento do início e do final
print(txt.strip)

# Substituindo letras
print(txt.replace("tres", "quatro"))

# Separando por caractere
print(txt.split(" "))

# Inserindo dado depois
idade = 21
txt2 = "Minha idade é {}"
print(txt2.format(idade))
