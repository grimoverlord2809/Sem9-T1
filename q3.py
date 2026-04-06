# Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. Separe esses valores com um hífen.

#entrada de dados
def entrada_dados():
    base   = int(input("Digite a base: "))  # lê o valor da base
    altura = int(input("Digite a altura: "))  # lê o valor da altura
    return base, altura

#processamento de dados
def verificar_forma(base, altura):
    if base == altura:                    # se base == altura, é um quadrado
        return "QUADRADO"
    else:
        perimetro = 2 * (base + altura)   # perímetro = soma de todos os lados
        area = base * altura              # área = base × altura
        return f"{perimetro} - {area}"   # exibe perímetro e área separados por hífen

#função principal
def main():
    base, altura = entrada_dados()            # obtém base e altura
    resultado = verificar_forma(base, altura) # verifica a forma e calcula
    print(f"Resultado: {resultado}")           # exibe o resultado
if __name__ == "__main__":    main()