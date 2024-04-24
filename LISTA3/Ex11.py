def contar_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 1]
    resultado = {}

    for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            resultado[cedula] = quantidade
            valor -= quantidade * cedula

    return resultado

# Solicita ao usuário o valor
valor = int(input("Digite o valor desejado: "))

# Calcula e exibe as notas necessárias
notas_utilizadas = contar_cedulas(valor)
print("Notas utilizadas:")
for cedula, quantidade in notas_utilizadas.items():
    print(quantidade, "nota(s) de R$", cedula)
