# Escreva um programa que leia dois valores e uma das seguintes operações, codificadas dessa forma, será executada:

# 1 – Adição

# 2 – Subtração

# 3 – Multiplicação

# 4 – Divisão

# Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

#entrada de dados
def entrada_dados():
    valor1   = float(input("Digite o primeiro valor: "))  # lê o primeiro valor
    valor2   = float(input("Digite o segundo valor: "))  # lê o segundo valor
    operacao = int(input("Digite a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))    # lê o código da operação
    return valor1, valor2, operacao

#processamento de dados
def calcular(valor1, valor2, operacao):
    if operacao == 1:
        return valor1 + valor2   # adição
    elif operacao == 2:
        return valor1 - valor2   # subtração
    elif operacao == 3:
        return valor1 * valor2   # multiplicação
    elif operacao == 4:
        return valor1 / valor2   # divisão

#função principal
def main():
    valor1, valor2, operacao = entrada_dados()       # obtém valores e operação
    resultado = calcular(valor1, valor2, operacao)   # executa o cálculo
    print(f"Resultado: {resultado}")                  # exibe o resultado
if __name__ == "__main__":    main()