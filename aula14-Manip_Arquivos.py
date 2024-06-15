# Manipulação de arquivos

# open("NomeDoArquivo", "Modo")

# MODOS:
# "r"- Ler - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existe
# "a" - Anexar - abre um arquivo para anexar, cria o arquivo se ele não existir
# "w" - Gravar - abre um arquivo para gravação, cria o arquivo se ele não existir
# "x" - Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir

# TIPOS
# "t"- Texto - Valor padrão. Modo texto
# "b" - Binário - Modo binário (por exemplo, imagens)

texto = open("texto.txt", "r", encoding="UTF-8")
print(texto.read(6)) # apenas as 6 primeiras letras
#print(texto.readline()) # Lê linha por linha

for x in texto:
    if "txt" in x:print(x)

texto.close(

    
)