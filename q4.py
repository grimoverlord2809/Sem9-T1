# Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.

#entrada de dados
def entrada_dados():
    num1 = int(input("Digite o primeiro número: "))  # lê o primeiro número inteiro
    num2 = int(input("Digite o segundo número: "))  # lê o segundo número inteiro
    num3 = int(input("Digite o terceiro número: "))  # lê o terceiro número inteiro
    return num1, num2, num3

#processamento de dados
def menor_diferenca(num1, num2, num3):
    dif2 = abs(num1 - num2)  # calcula a diferença absoluta entre o 1º e o 2º
    dif3 = abs(num1 - num3)  # calcula a diferença absoluta entre o 1º e o 3º
    if dif2 <= dif3:          # verifica qual diferença é menor
        return dif2           # retorna a diferença do 2º valor
    else:
        return dif3           # retorna a diferença do 3º valor

#função principal
def main():
    num1, num2, num3 = entrada_dados()            # obtém os três valores
    resultado = menor_diferenca(num1, num2, num3) # determina a menor diferença
    print(f"Menor diferença: {resultado}")            # exibe o resultado
if __name__ == "__main__":    main()