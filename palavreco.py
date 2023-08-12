import random

from random import shuffle

def embara(elemento) :
  a = list(elemento)
  shuffle(a)
  a = "".join(a)
  print(a.upper())

def verifi(elemento, res):
  if res != elemento:
      print("A resposta está incorreta!!")
  elif res == elemento:
      print("A resposta está correta!!")
  else:
      print('Essa opção não existe')


temas = int(input('Selecione um tema: \n 1-Carro \n 2-Cor \n 3-Time \n'))
difi = int(input('Selecione uma dificuldade: \n 1-Fácil \n 2-Médio \n 3-Difícil \n'))

timef = ['santos', 'flamengo', 'palmeiras', 'fluminense', 'vasco']
timem = ['valencia', 'liverpool', 'napoli', 'monaco', 'sampdoria']
timed = ['galatasaray', 'fenerbahce', 'besiktas', 'tottenham', 'feyenoord']

corf = ['rosa', 'azul', 'verde', 'amarelo', 'vermelho']
corm = ['lilas', 'ciano', 'dourado', 'bordo', 'bege']
cord = ['gingerline', 'incarnadine', 'labrador', 'nattier', 'pervenche']

carrof = ['fusca', 'celta', 'onix', 'palio', 'corsa']
carrom = ['agile', 'cobalt', 'evoque', 'pajero', 'picasso']
carrod = ['cayman', 'hoggar', 'gallardo', 'veloster', 'aircross']

if temas == 1 :

  if difi == 1 :
    
    elemento = random.choice(carrof)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi == 2 :

    elemento = random.choice(carrom)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi == 3 :

    elemento = random.choice(carrod)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi > 3 :
    print('Essa opção não existe')


elif temas == 2 :

  if difi == 1 :

    elemento = random.choice(corf)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi == 2 :

    elemento = random.choice(corm)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi == 3 :

    elemento = random.choice(cord)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi > 3 :
    print('Essa opção não existe')


elif temas == 3 :

  if difi == 1 :

    elemento = random.choice(timef)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi == 2 :

    elemento = random.choice(timem)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi == 3 :

    elemento = random.choice(timed)
    embara(elemento)

    res = input('Qual é a palavra: ')

    verifi(elemento, res)

  elif difi > 3 :
    print('Essa opção não existe')

else :
  print('Essa opção não existe')