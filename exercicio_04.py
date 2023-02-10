''' Desenvolva um código em python  que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
'''

# Variáveis para armazenar as informações do veículo
quantidade_rodas = int(input("Quantidade de rodas do veículo: "))
peso_bruto = float(input("Peso bruto do veículo (em kg): "))
quantidade_pessoas = int(input("Quantidade de pessoas no veículo: "))

# Verificação das condições para definir a categoria de habilitação
if quantidade_rodas >= 2 and quantidade_rodas <= 3:
  categoria = "A"
elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
  categoria = "B"
elif quantidade_rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000:
  categoria = "C"
elif quantidade_rodas >= 4 and quantidade_pessoas > 8:
  categoria = "D"
elif quantidade_rodas >= 4 and peso_bruto > 6000:
  categoria = "E"
else:
  categoria = "Inválida"

# Exibição da categoria de habilitação
print("A categoria de habilitação para o veículo é:", categoria)
