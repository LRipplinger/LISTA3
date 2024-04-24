def calcular_valor_venda(valor_compra):
    if valor_compra < 20:
        lucro_percentual = 0.45  # 45%
    elif valor_compra <= 50:
        lucro_percentual = 0.35  # 35%
    else:
        lucro_percentual = 0.25  # 25%

    # Calcula o valor de venda com base no lucro percentual
    valor_venda = valor_compra * (1 + lucro_percentual)
    return valor_venda

# Solicita ao usuário o valor da compra
valor_compra = float(input("Digite o valor da compra: "))

# Calcula o valor de venda
valor_venda = calcular_valor_venda(valor_compra)

# Exibe o valor de venda
print("O valor de venda é R$", valor_venda)
