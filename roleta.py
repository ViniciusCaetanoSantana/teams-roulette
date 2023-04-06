from random import shuffle

pessoas_= int(input('Quantas pessoas vão jogar? ')) # how many people will play?
contador = 1
pessoas = []
print('-='*15)

while True:
    if contador > pessoas_:
        break
    nome = str(input(f'Nome {contador}: ').title())  # names
    pessoas.append(nome)
    contador += 1

shuffle(pessoas)
time1num = (len(pessoas)) // 2

print('-='*15)

print(f'Time1: ')
for nomes in range(time1num):
    print('-',pessoas[nomes])
    pessoas.remove(pessoas[nomes])

print('-='*15)

print(f'Time2: ')
for nomes in range(len(pessoas)):
    print('-',pessoas[nomes])