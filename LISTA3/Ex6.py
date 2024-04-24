import random

def jogo_par_ou_impar():
    # Pergunta ao usuário se ele aposta em PAR ou ÍMPAR
    aposta = input("Você aposta em PAR ou ÍMPAR? ").upper()
    while aposta not in ['PAR', 'ÍMPAR']:
        print("Por favor, escolha entre PAR ou ÍMPAR.")
        aposta = input("Você aposta em PAR ou ÍMPAR? ").upper()

    # Solicita ao usuário que escolha um número de 0 a 5
    numero_usuario = int(input("Escolha um número de 0 a 5: "))
    while numero_usuario < 0 or numero_usuario > 5:
        print("Por favor, escolha um número entre 0 e 5.")
        numero_usuario = int(input("Escolha um número de 0 a 5: "))

    # Gera um número aleatório de 0 a 5 para o computador
    numero_computador = random.randint(0, 5)
    print("O número escolhido pelo computador é:", numero_computador)

    # Calcula a soma dos números escolhidos pelo usuário e pelo computador
    soma = numero_usuario + numero_computador
    print("A soma dos números é:", soma)

    # Verifica se a soma é par ou ímpar e se corresponde à aposta do usuário
    if (soma % 2 == 0 and aposta == 'PAR') or (soma % 2 != 0 and aposta == 'ÍMPAR'):
        print("Parabéns! Você venceu!")
    else:
        print("Você perdeu! O programa venceu.")

# Chama a função para jogar PAR ou ÍMPAR
jogo_par_ou_impar()
