# Exibe uma mensagem de boas-vindas e instrui o jogador
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

# Inicializa o número secreto e as variáveis de tentativas
numero_secreto = 42  # Substitua pelo número secreto que deseja
max_tentativas = 10  # Define o número máximo de tentativas
tentativas = 0  # Inicializa o contador de tentativas

# Loop principal do jogo, que continua enquanto o jogador não atingir o número máximo de tentativas
while tentativas < max_tentativas:
    try:
        # Solicita o palpite do jogador
        palpite = int(input("Seu palpite: "))
    except ValueError:
        # Se o jogador não digitar um número, exibe uma mensagem de erro e continua o loop
        print("Por favor, digite um número válido!")
        continue
    
    # Incrementa o contador de tentativas
    tentativas += 1

    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        # Se o palpite estiver correto, exibe uma mensagem de sucesso e encerra o jogo
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
        break
    elif palpite < numero_secreto:
        # Se o palpite for menor que o número secreto, sugere um número maior
        print("Tente um número maior.")
    else:
        # Se o palpite for maior que o número secreto, sugere um número menor
        print("Tente um número menor.")
else:
    # Se o jogador atingir o número máximo de tentativas sem acertar, exibe o número secreto
    print(f"Você atingiu o número máximo de tentativas. O número secreto era {numero_secreto}.")
