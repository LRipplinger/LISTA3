def calcular_valor_plano(idade, numero_dependentes):
    valor_plano = 300  # Valor base do plano
    
    # Calcula o adicional baseado na idade do conveniado
    if idade < 10:
        valor_plano += 100
    elif idade >= 10 and idade <= 30:
        valor_plano += 220
    elif idade >= 31 and idade <= 60:
        valor_plano += 395
    elif idade > 60:
        valor_plano += 480

    # Calcula o adicional baseado na idade dos dependentes
    if numero_dependentes > 0:
        for _ in range(numero_dependentes):
            idade_dependente = int(input("Digite a idade do dependente: "))
            if idade_dependente < 10:
                valor_plano += 100
            elif idade_dependente >= 10 and idade_dependente <= 30:
                valor_plano += 220
            elif idade_dependente >= 31 and idade_dependente <= 60:
                valor_plano += 395
            elif idade_dependente > 60:
                valor_plano += 480

    return valor_plano

# Solicita ao usuário a idade do conveniado
idade_conveniado = int(input("Digite a idade do conveniado: "))

# Solicita ao usuário o número de dependentes
numero_dependentes = int(input("Digite o número de dependentes: "))

# Calcula o valor total do plano
valor_total = calcular_valor_plano(idade_conveniado, numero_dependentes)

# Exibe o valor total a ser pago pelo plano de saúde
print("O valor total a ser pago pelo plano de saúde é R$", valor_total)
