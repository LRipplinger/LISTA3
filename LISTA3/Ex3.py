def calcular_dobro_ou_triplo(numero):
    if numero > 0:
        resultado = numero * 2
        print("O dobro de", numero, "é:", resultado)
    elif numero < 0:
        resultado = numero * 3
        print("O triplo de", numero, "é:", resultado)
    else:
        print("O número é zero.")

# Solicita ao usuário um número
numero = float(input("Digite um número: "))

# Chama a função para calcular o dobro ou o triplo
calcular_dobro_ou_triplo(numero)