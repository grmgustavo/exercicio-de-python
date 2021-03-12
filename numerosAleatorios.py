from random import *


nAl = randint(0,100)


n = int (input("Informe um número de 0 a 100: "))



if n == nAl:
    print("Você acertou, o numero aleatório era {}, o mesmo que o seu".format(nAl))
else: 
    print("Você errou, o numero aleatorio era {}".format(nAl))
