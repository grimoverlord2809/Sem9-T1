# Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os valores lidos:

# Todos os valores são diferentes;

# Existem dois valores iguais e um diferente;

# Todos os valores são iguais.

#entrada de dados  

def entrada_numeros():
    num1 = int(input("Digite o primeiro número: "))  # lê o primeiro número inteiro
    num2 = int(input("Digite o segundo número: "))  # lê o segundo número inteiro
    num3 = int(input("Digite o terceiro número: "))  # lê o terceiro número inteiro
    return num1, num2, num3

#processamento de dados
def verificar_valores(num1, num2, num3):
    if num1 == num2 == num3:                               # verifica se os três são iguais
        return "Todos os valores são iguais"
    elif num1 != num2 and num1 != num3 and num2 != num3:   # verifica se todos são diferentes
        return "Todos os valores são diferentes"
    else:                                                  # caso contrário, dois são iguais
        return "Existem dois valores iguais e um diferente"
#função principal
def main():
    num1, num2, num3 = entrada_numeros()             # obtém os três valores
    resultado = verificar_valores(num1, num2, num3)  # determina a relação entre eles
    print(f"Resultado: {resultado}")                  # exibe o resultado
if __name__ == "__main__":    main()