#Definindo o tipo de variável
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