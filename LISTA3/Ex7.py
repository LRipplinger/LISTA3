def calcular_desconto_previdenciario(salario):
    # Define a taxa de desconto como 11%
    taxa_desconto = 0.11
    
    # Calcula o desconto proporcional ao salário
    desconto = salario * taxa_desconto
    
    # Verifica se o desconto ultrapassa o limite máximo de 318,20
    if desconto > 318.20:
        desconto = 318.20
    
    return desconto

# Solicita ao usuário que digite o salário do funcionário
salario_funcionario = float(input("Digite o salário do funcionário: "))

# Chama a função para calcular o desconto previdenciário
desconto_previdenciario = calcular_desconto_previdenciario(salario_funcionario)

# Exibe o valor do desconto previdenciário
print("O desconto previdenciário é de R$", desconto_previdenciario)
