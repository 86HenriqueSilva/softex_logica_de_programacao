''' ️
Faça uma função calculadora em python  de dois números com três parâmetros:
os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
 Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0. '''


def calculadora(n1, n2, operacao):
  if operacao == 1:
    return n1 + n2
  elif operacao == 2:
    return n1 - n2
  elif operacao == 3:
    return n1 * n2
  elif operacao == 4:
    if n2 != 0:
      return n1 / n2
    else:
      return "Divisão por 0 é inválida"
  else:
    return 0

print(calculadora(10, 5, 1)) # 15
print(calculadora(10, 5, 2)) # 5
print(calculadora(10, 5, 3)) # 50
print(calculadora(10, 5, 4)) # 2
print(calculadora(10, 0, 4)) # Divisão por 0 é inválida
print(calculadora(10, 5, 5)) # 0
