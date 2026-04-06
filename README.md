# Semana 9 — Tarefa 1 (Sem9-T1)

**Turma:** 166/186  
**Período:** 2026-1  
**Professor:** Ritomar Torquato  
**Instituição:** IFPI  
**Tema:** Condicionais — Fundamentos

---

## Questão 1 — Comparação de três números (`q1.py`)

**Enunciado:** Leia 3 números inteiros e informe se todos são iguais, todos são diferentes ou se existem dois iguais e um diferente.

**Como funciona:**

1. A função `entrada_numeros()` lê três valores inteiros via `input()`.
2. A função `verificar_valores(num1, num2, num3)` compara os três valores:
   - Se `num1 == num2 == num3` → todos são iguais.
   - Se todos forem diferentes entre si (usando `!=` par a par) → todos são diferentes.
   - Caso contrário → existem dois iguais e um diferente.
3. O resultado é exibido com `print()`.

**Exemplo:**
```
Entrada: 5, 5, 3
Saída: Existem dois valores iguais e um diferente
```

---

## Questão 2 — Calculadora simples (`q2.py`)

**Enunciado:** Leia dois valores e um código de operação (1=Adição, 2=Subtração, 3=Multiplicação, 4=Divisão) e exiba o resultado.

**Como funciona:**

1. A função `entrada_dados()` lê dois valores (`float`) e o código da operação (`int`).
2. A função `calcular(valor1, valor2, operacao)` usa condicionais `if/elif` para executar a operação correspondente:
   - `1` → soma (`+`)
   - `2` → subtração (`-`)
   - `3` → multiplicação (`*`)
   - `4` → divisão (`/`)
3. O resultado do cálculo é exibido.

**Exemplo:**
```
Entrada: 10, 3, 3
Saída: Resultado: 30.0
```

---

## Questão 3 — Retângulo ou Quadrado (`q3.py`)

**Enunciado:** Leia base e altura. Se forem iguais, imprima "QUADRADO". Se forem diferentes, mostre o perímetro e a área do retângulo separados por hífen.

**Como funciona:**

1. A função `entrada_dados()` lê a base e a altura (inteiros).
2. A função `verificar_forma(base, altura)` verifica:
   - Se `base == altura` → retorna `"QUADRADO"`.
   - Caso contrário → calcula o perímetro (`2 * (base + altura)`) e a área (`base * altura`), retornando no formato `"perímetro - área"`.
3. O resultado é exibido.

**Exemplo:**
```
Entrada: 5, 8
Saída: Resultado: 26 - 40
```

---

## Questão 4 — Menor diferença (`q4.py`)

**Enunciado:** Leia 3 valores inteiros. Determine se o segundo ou o terceiro valor tem menor diferença em relação ao primeiro, imprimindo o valor dessa diferença.

**Como funciona:**

1. A função `entrada_dados()` lê os três números inteiros.
2. A função `menor_diferenca(num1, num2, num3)` calcula:
   - `dif2 = abs(num1 - num2)` → diferença absoluta entre o 1º e o 2º.
   - `dif3 = abs(num1 - num3)` → diferença absoluta entre o 1º e o 3º.
   - Compara `dif2` e `dif3` e retorna a menor.
3. O valor da menor diferença é exibido.

**Exemplo:**
```
Entrada: 10, 7, 15
Saída: Menor diferença: 3
```

---

## Questão 5 — Resto da divisão por 5 (`q5.py`)

**Enunciado:** Leia um número inteiro, calcule o resto da divisão por 5 e, conforme o resultado, execute uma operação específica.

**Como funciona:**

1. A função `entrada_dados()` lê um número inteiro.
2. A função `processar(n)` calcula `resto = n % 5` e decide:
   - **Resto 0:** retorna `9n + 7`.
   - **Resto 1:** verifica se `n` é par ou ímpar.
   - **Resto 2:** retorna `5n² - 3n + 42`.
   - **Resto 3:** retorna a divisão inteira de `n` por 10 (`n // 10`).
   - **Resto 4:** retorna o quadrado de `n` (`n²`).
3. O resultado é exibido.

**Exemplo:**
```
Entrada: 7
7 % 5 = 2 → 5*(7²) - 3*7 + 42 = 245 - 21 + 42 = 266
Saída: Resultado: 266
```
