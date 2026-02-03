import random

# Personagem
nome = input("Qual é o nome do seu herói? ")
nivel = 1
xp = 0
vida = 100
mochila = []

print(f"\nBem-vindo, {nome}, ao RPG Ninja de Terminal! 😎\n")

# Função batalha simples
def batalhar():
    global xp, vida
    inimigo = random.choice(["Goblin", "Esqueleto", "Slime"])
    vida_inimigo = random.randint(20, 50)
    print(f"Um {inimigo} apareceu com {vida_inimigo} de vida!")

    while vida_inimigo > 0 and vida > 0:
        acao = input("Escolha: [A]tacar ou [C]urar: ").lower()
        if acao == "a":
            dano = random.randint(5, 20)
            vida_inimigo -= dano
            print(f"Você causou {dano} de dano! Vida do inimigo: {vida_inimigo}")
        elif acao == "c":
            cura = random.randint(10, 25)
            vida += cura
            print(f"Você curou {cura} de vida! Sua vida: {vida}")
        else:
            print("Ação inválida!")

        if vida_inimigo > 0:
            dano_inimigo = random.randint(5, 15)
            vida -= dano_inimigo
            print(f"O {inimigo} atacou e causou {dano_inimigo} de dano! Sua vida: {vida}")

    if vida > 0:
        ganho_xp = random.randint(10, 30)
        xp += ganho_xp
        print(f"Você venceu! Ganhou {ganho_xp} XP. Total de XP: {xp}\n")
        mochila.append(random.choice(["Poção", "Espada", "Escudo"]))
        print(f"Você encontrou um item: {mochila[-1]}\n")
    else:
        print("Você foi derrotado! Game Over 😢")
        exit()

# Loop principal
while True:
    print(f"\n{nome} - Nível {nivel} - XP: {xp} - Vida: {vida} - Mochila: {mochila}")
    comando = input("Escolha sua ação: [B]atalhar, [S]air: ").lower()
    if comando == "b":
        batalhar()
        if xp >= 50 * nivel:  # sobe de nível
            nivel += 1
            vida += 20
            print(f"Parabéns! {nome} subiu para o nível {nivel}! Vida aumentou para {vida}")
    elif comando == "s":
        print("Saindo do jogo... Até a próxima! 😎")
        break
    else:
        print("Comando inválido!")
