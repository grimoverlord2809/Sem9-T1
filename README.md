<div align="center">

# 📘 Semana 9 — Tarefa 1 (Sem9-T1)

### Condicionais — Fundamentos

| Informação | Detalhe |
|:---:|:---:|
| **Turma** | 166/186 |
| **Período** | 2026-1 |
| **Professor** | Ritomar Torquato |
| **Instituição** | IFPI |
| **Linguagem** | Python 3 |

</div>

---

## 📂 Estrutura do Projeto

```
t1/
├── q1.py   → Comparação de três números
├── q2.py   → Calculadora simples
├── q3.py   → Retângulo ou Quadrado
├── q4.py   → Menor diferença
├── q5.py   → Resto da divisão por 5
└── README.md
```

---

## 🔹 Questão 1 — Comparação de três números (`q1.py`)

**Enunciado:** Leia 3 números inteiros e informe se todos são iguais, todos são diferentes ou se existem dois iguais e um diferente.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_numeros():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    return num1, num2, num3

def verificar_valores(num1, num2, num3):
    if num1 == num2 == num3:
        return "Todos os valores são iguais"
    elif num1 != num2 and num1 != num3 and num2 != num3:
        return "Todos os valores são diferentes"
    else:
        return "Existem dois valores iguais e um diferente"

def main():
    num1, num2, num3 = entrada_numeros()
    resultado = verificar_valores(num1, num2, num3)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê 3 números inteiros via `input()` |
| **Processamento** | Compara os valores usando `==` e `!=` par a par |
| **Saída** | Exibe uma das 3 mensagens possíveis |

**Lógica das comparações:**

```
num1 == num2 == num3              → "Todos os valores são iguais"
num1 != num2 AND num1 != num3
           AND num2 != num3       → "Todos os valores são diferentes"
senão                             → "Existem dois valores iguais e um diferente"
```

**▶️ Exemplo de execução:**
```
Digite o primeiro número: 5
Digite o segundo número: 5
Digite o terceiro número: 3
Resultado: Existem dois valores iguais e um diferente
```

---

## 🔹 Questão 2 — Calculadora simples (`q2.py`)

**Enunciado:** Leia dois valores e um código de operação (1=Adição, 2=Subtração, 3=Multiplicação, 4=Divisão) e exiba o resultado.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    valor1   = float(input("Digite o primeiro valor: "))
    valor2   = float(input("Digite o segundo valor: "))
    operacao = int(input("Digite a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))
    return valor1, valor2, operacao

def calcular(valor1, valor2, operacao):
    if operacao == 1:
        return valor1 + valor2
    elif operacao == 2:
        return valor1 - valor2
    elif operacao == 3:
        return valor1 * valor2
    elif operacao == 4:
        return valor1 / valor2

def main():
    valor1, valor2, operacao = entrada_dados()
    resultado = calcular(valor1, valor2, operacao)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê dois valores (`float`) e o código da operação (`int`) |
| **Processamento** | Usa `if/elif` para escolher a operação matemática |
| **Saída** | Exibe o resultado do cálculo |

**Mapeamento das operações:**

| Código | Operação | Símbolo |
|:---:|:---:|:---:|
| 1 | Adição | `+` |
| 2 | Subtração | `-` |
| 3 | Multiplicação | `*` |
| 4 | Divisão | `/` |

**▶️ Exemplo de execução:**
```
Digite o primeiro valor: 10
Digite o segundo valor: 3
Digite a operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): 3
Resultado: 30.0
```

---

## 🔹 Questão 3 — Retângulo ou Quadrado (`q3.py`)

**Enunciado:** Leia base e altura. Se forem iguais, imprima "QUADRADO". Se forem diferentes, mostre o perímetro e a área do retângulo separados por hífen.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    base   = int(input("Digite a base: "))
    altura = int(input("Digite a altura: "))
    return base, altura

def verificar_forma(base, altura):
    if base == altura:
        return "QUADRADO"
    else:
        perimetro = 2 * (base + altura)
        area = base * altura
        return f"{perimetro} - {area}"

def main():
    base, altura = entrada_dados()
    resultado = verificar_forma(base, altura)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê base e altura (inteiros) |
| **Processamento** | Verifica se `base == altura` (quadrado) ou calcula perímetro e área |
| **Saída** | `"QUADRADO"` ou `"perímetro - área"` |

**Fórmulas utilizadas:**

```
Perímetro = 2 × (base + altura)
Área      = base × altura
```

**▶️ Exemplo de execução:**
```
Digite a base: 5
Digite a altura: 8
Resultado: 26 - 40
```
```
Digite a base: 4
Digite a altura: 4
Resultado: QUADRADO
```

---

## 🔹 Questão 4 — Menor diferença (`q4.py`)

**Enunciado:** Leia 3 valores inteiros. Determine se o segundo ou o terceiro valor tem menor diferença em relação ao primeiro, imprimindo o valor dessa diferença.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    return num1, num2, num3

def menor_diferenca(num1, num2, num3):
    dif2 = abs(num1 - num2)
    dif3 = abs(num1 - num3)
    if dif2 <= dif3:
        return dif2
    else:
        return dif3

def main():
    num1, num2, num3 = entrada_dados()
    resultado = menor_diferenca(num1, num2, num3)
    print(f"Menor diferença: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê 3 números inteiros |
| **Processamento** | Calcula `abs(num1 - num2)` e `abs(num1 - num3)`, compara as diferenças |
| **Saída** | Exibe a menor diferença absoluta |

**Lógica do cálculo:**

```
dif2 = |num1 - num2|    ← diferença entre 1º e 2º
dif3 = |num1 - num3|    ← diferença entre 1º e 3º

Se dif2 ≤ dif3 → retorna dif2
Senão          → retorna dif3
```

**▶️ Exemplo de execução:**
```
Digite o primeiro número: 10
Digite o segundo número: 7
Digite o terceiro número: 15
Menor diferença: 3
```

> `|10 - 7| = 3` e `|10 - 15| = 5` → menor é **3**

---

## 🔹 Questão 5 — Resto da divisão por 5 (`q5.py`)

**Enunciado:** Leia um número inteiro, calcule o resto da divisão por 5 e, conforme o resultado, execute uma operação específica.

<details>
<summary>📄 Ver código completo</summary>

```python
def entrada_dados():
    n = int(input("Digite um número inteiro: "))
    return n

def processar(n):
    resto = n % 5
    if resto == 0:
        return 9 * n + 7
    elif resto == 1:
        if n % 2 == 0:
            return "par"
        else:
            return "ímpar"
    elif resto == 2:
        return 5 * n ** 2 - 3 * n + 42
    elif resto == 3:
        return n // 10
    elif resto == 4:
        return n ** 2

def main():
    n = entrada_dados()
    resultado = processar(n)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":    main()
```

</details>

**🔍 Como funciona:**

| Etapa | Descrição |
|:---:|---|
| **Entrada** | Lê um número inteiro |
| **Processamento** | Calcula `n % 5` e executa a operação correspondente ao resto |
| **Saída** | Exibe o resultado da operação |

**Tabela de operações por resto:**

| Resto (`n % 5`) | Operação | Fórmula |
|:---:|---|:---:|
| 0 | Equação | `9n + 7` |
| 1 | Paridade | par / ímpar |
| 2 | Equação | `5n² - 3n + 42` |
| 3 | Divisão inteira | `n // 10` |
| 4 | Quadrado | `n²` |

**▶️ Exemplo de execução:**
```
Digite um número inteiro: 7
Resultado: 266
```

> `7 % 5 = 2` → `5×(7²) - 3×7 + 42 = 245 - 21 + 42 = 266`

---

<div align="center">

**IFPI — Instituto Federal do Piauí** • Período 2026-1 • Prof. Ritomar Torquato

</div>
