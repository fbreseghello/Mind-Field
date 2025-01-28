print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while tentativas < max_tentativas:
    try:
        palpite = int(input("Seu palpite: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue
    
    tentativas += 1
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
else:
    print(f"Você atingiu o número máximo de tentativas. O número secreto era {numero_secreto}.")