import random

print("Bem-vindo ao Jogo de Adivinhação! 😎")

numero_secreto = random.randint(1, 50)
tentativa = 0
acertou = False

while not acertou:
    chute = int(input("Digite um número de 1 a 50: "))
    tentativa += 1
    if chute < numero_secreto:
        print("Muito baixo! ⬇️")
    elif chute > numero_secreto:
        print("Muito alto! ⬆️")
    else:
        print(f"Parabéns! Você acertou em {tentativa} tentativas 🎉")
        acertou = True
