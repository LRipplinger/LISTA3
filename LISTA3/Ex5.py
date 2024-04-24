def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        print(numero, "é um número par.")
    else:
        print(numero, "é um número ímpar.")

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Chama a função para verificar se é par ou ímpar
verificar_par_ou_impar(numero)
