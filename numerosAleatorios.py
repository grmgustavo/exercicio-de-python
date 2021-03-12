from random import *
print ("Hello World")

nAl = randint(0,100)
n = input("Informe um número de 0 a 100: ")

if nAl == n:
    print("Você acertou, o seu numero era {}, o mesmo que o seu".format(nAl))
else: 
    print("Você errou, o numero aleatorio era {} o seu foi {}".format(nAl, n))
