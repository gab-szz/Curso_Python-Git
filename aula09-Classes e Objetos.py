# O INIT
###################################
# PROGRAMAÇÃO ORIENTADA A OBJETOS #
###################################

# Classe pessoa
class Pessoa:
    def __init__(objeto, nome, idade) -> None: # objeto = self
        objeto.nome = nome
        objeto.idade = idade

    def cumprimento(objeto):
        print("Olá, meu nome é: " + objeto.nome)

# Trabalhando com as classes
p1 = Pessoa("Gabriel", 36)
p1.nome = "Gab" # Alterando dado objeto
del p1.idade # Deleta dado de objeto
p1.cumprimento()
del p1 # Deleta o objeto

p2 = Pessoa("Danny", 35)
print("P2 " + p2.nome)
print("P2 ", p2.idade)

# Herança
class Estudante(Pessoa):
    def __init__(objeto, nome, idade, curso) -> None: 
        # Há duas formas de herdar propriedade da classe Pai:
        # Pessoa.__init__(objeto, nome, sobrenome)
        super().__init__(nome, idade)
        objeto.curso = curso
    
    def eCumprimento(objeto):
        print("Olá, meu nome é " + objeto.nome + "tenho " + objeto.idade + "anos e estou cursando " + objeto.curso)

p1 = Estudante("Gabriel", 22, "Banco de Dados")
print(p1.cumprimento())

