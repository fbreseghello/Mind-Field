import random
import sys

print ("idade?")
idd = int(input())

print ("nome?")
nm = str(input())

print ("alt?")
alt = float(input())

print ("estuda?")
estd = bool(input())

print(f"idade {idd} nome {nm} alt {alt} estuda {estd}")

sys.exit()

"""
print("Qual sua idade?")
idade = int(input())

if idade >= 18:
    print("voce é maior de idade teste concluido")
else:
    print("voce é menor de idade teste concluido")
    sys.exit()

print("Qual seu nome?")
nome = str(input())

print(f"Ola {nome} voce tem: {idade}")
print("adivinhe um numero de 1 a 10")
numero = random.randint(1, 10)
tentativas = 0

while True:
    tentativa = int(input())
    tentativas += 1
    if tentativa == numero:
        print(f"Parabens voce acertou o numero era {numero} e voce tentou {tentativas} vezes")
        break
    else:
        print("Tente novamente")
"""