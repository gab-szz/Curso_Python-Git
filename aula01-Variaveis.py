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

# Dicas (Caracteres de escape)
txt = "Somos os chamados \"vikings\" do norte." #Assim conseguimos imprimir as ""
print(txt)

txt = "Ola\nMundo!" # Quebra de linha
print(txt) 

txt = "Ola\rMundo!" # Retorna
print(txt) 

txt = "Ola\tMundo!" # Tabulação
print(txt)
txt = "Isso irá inserir um \\ (barra invertida)." 
print(txt) 

txt = 'It\'s alright.' # Substitui por uma aspas simples
print(txt) 

txt = "Ola \bMundo!" #Este exemplo apaga um caractere (backspace):
print(txt)

txt = "\x48\x65\x6c\x6c\x6f" #Uma barra invertida seguida por um 'x' e um número hexadecimal representa um valor hexadecimal
print(txt) 

txt = "\110\145\154\154\157" #Uma barra invertida seguida por três inteiros resultará em um valor octal
print(txt) 


# Confirmar se é uma instância
print(isinstance(txt, str)) 