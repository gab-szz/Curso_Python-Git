##############
# ITERADORES #
##############

Tupla = ["mercado", "farmacia", "açougue"]
Iterador = iter(Tupla)

print(next(Iterador))
print(next(Iterador))
print(next(Iterador))

class MeusNumeros:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self): # Para ser usado em for
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # Parar interação

myClass = MeusNumeros()
myIter = iter(myClass)

for x in myIter:
    print(x)


