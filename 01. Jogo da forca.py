import random

print("\033[47m\033[1m "*31)
print("\033[47m\033[1m" + " "*5 + "\U0001F635  JOGO DA FORCA  \U0001F635" + " "*5 + "\033[1m")
print("\033[47m\033[1m" + " "*31 + "\033[0m")
print(" "*12 + "By DMax\n"+ " " * 12)

def escolher_palavra(categorias):
    print(" \033[47m\033[1m🎲  Escolha uma categoria: \033[0m")
    for idx, categoria in enumerate(categorias.keys(), 1):
        print(f"{idx}. {categoria}")
    
    while True:
        try:
            escolha = int(input("\U0001F4AC \033[4mDigite 1, 2 ou 3:\033[0m ")) -1
            if 0 <= escolha < len(categorias):
                break
            else:
                print("\u2757 \033[31mEscolha inválida! Tente novamente.\033[0m \u2757")
        except ValueError:
            print("\u2757 \033[31mPor favor, digite um número válido.\033[0m \u2757")
    
    categoria_selecionada = list(categorias.keys())[escolha]
    palavra = random.choice(categorias[categoria_selecionada]).upper()
    return palavra, categoria_selecionada

def mostrar_forca(tentativas):
    estagios = [
        """
        \033[1m\033[31mGAME OVER\033[0m
           _____
          |     |
          |    💀
          |    /|\\
          |    / \\
          |
        __|__
        """,
        """
        SE TU ERRAR MAIS UMA EU MORRO! 
        AI MEU DEUS!
           _____
          |     |
          |    😵
          |    /|\\
          |    /
          |
        __|__
        """,
        """
           _____
          |     |
          |    😡
          |    /|\\
          |
          |
        __|__
        """,
        """
           _____
          |     |
          |    😰
          |    /|
          |
          |
        __|__
        """,
        """
           _____
          |     |
          |    😢
          |     |
          |
          |
        __|__
        """,
        """
           _____
          |     |
          |    🤔
          |
          |
          |
        __|__
        """,
        """
           _____
          |     |
          |
          |
          |
          |
        __|__
        """
    ]
    return estagios[tentativas]


def jogar():
    categorias = {
        "\033[43m Frutas  \033[0m": ["banana", "abacaxi", "manga", "uva", "morango", "jambo", "melancia", "kiwi", "ata", "cacau", "laranja", "acerola", "melao", "cupuacu", "carambola", "goiaba", "siriguela", "pitomba", "caja", "limao"],
        "\033[42m Animais \033[0m": ["elefante", "cachorro", "gato", "tigre", "pinguim","passaro", "tigre", "peixe", "golfinho", "macaco", "vaca", "boi", "dinosauro", "tamandua", "tatu", "galinha", "rinoceronte", "girafa", "bode", "jegue"],
        "\033[46m Países  \033[0m": ["brasil", "canada", "alemanha", "japao", "australia", "chile", "argentina", "estados unidos", "china", "peru", "grecia", "egito", "coreia", "afeganistao", "israel", "arabia saudita", "italia", "franca", "portugal"]
    }

    palavra, categoria = escolher_palavra(categorias)
    letras_adivinhadas = []
    tentativas_restantes = 6
    palavra_oculta = [" " if char == " " else "_" for char in palavra]

    print(f"\nCategoria escolhida: \033[33m{categoria}\033[0m")

    while tentativas_restantes > 0 and "_" in palavra_oculta:
        print(mostrar_forca(tentativas_restantes))
        print("\U0001F914 \033[1mPalavra:\033[0m ", " ".join(palavra_oculta))
        print(f"\u23F3 Tentativas restantes: {tentativas_restantes}")
        print(f"\U0001F4DD Letras escolhidas: \033[34m{', '.join(sorted(letras_adivinhadas))}\033[0m")
        letra = input("\u2753 Adivinhe uma letra: ").strip().upper()

        if len(letra) != 1 or not letra.isalpha():
            print("\033[31mPor favor, digite apenas UMA letra válida.\033[0m")
            continue

        if letra in letras_adivinhadas:
            if letra in palavra:
                print(f"\033[32mA letra {letra} já está na palavra! Continue!\033[0m")
            else:
                print(f"\033[31mVocê já tentou a letra {letra} e ela NÃO está na palavra. Tente outra.\033[0m")
            continue

        letras_adivinhadas.append(letra)

        if letra in palavra:
            print(f"\u2705\033[32m Boa!\nA letra \033[42m\033[39m {letra} \033[0m \033[32mestá na palavra.\033[0m")
            for idx, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[idx] = letra
        else:
            print(f"\u274C\033[31m Não!\nA letra \033[41m\033[39m {letra} \033[0m \033[31mnão está na palavra.\033[0m")
            tentativas_restantes -= 1

    if "_" not in palavra_oculta:
        print("""
\033[43m       Você Escapou      \033[0m
\033[43m        da FORCA         \033[0m
\033[43m           \U0001F604 \U0001F3C6         \033[0m
           _____
          |     |
          |
          |
          |
          |
        __|__          
        """
        )
        print("\u2B50"*17)
        print(f" " *5 + "\033[34m Parabéns, Você Acertou! \033[0m"+ " " *5)
        print(f" "*3+f"\U0001F913\033[32m A palavra é:\033[47m {palavra} \033[0m \U0001F3C6"+" "*3)
        print("\u2B50"*17)
        print()

    else:
        print(mostrar_forca(tentativas_restantes))
        print("\U0001F480"*14)
        print(f" " *4 +f"\U0001F480\033[31m Fim de jogo! \U0001F480" + " " *4)
        print(f" " *2 +f"\033[31m A palavra era:\033[47m {palavra} \033[0m " + " " *2)
        print("\U0001F480"*14)        

if __name__ == "__main__":
    while True:
        jogar()
        replay = input("Deseja jogar novamente? \033[33m(s/n):\033[0m ").strip().lower()
        if replay == 's':
            print("\033[32mOk, Vamos lá novamente!\033[0m\n")
            continue
        elif replay == 'n':
            print("\033[33mObrigado por jogar! Até a próxima!\n\033[0m")
            break
        else:
            jogar()


'''
Jogo da Forca:
o Desenvolver um jogo clássico da forca onde o jogador
tenta adivinhar uma palavra oculta letra por letra.
o Pode incluir funcionalidades como seleção de categorias de palavras,
gráficos simples para representar o progresso do jogo e contagem de tentativas.
o É um projeto que permite explorar estruturas de dados
como listas e strings, além de laços de repetição e condicionais.
'''