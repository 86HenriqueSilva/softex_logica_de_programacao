#Levando em consideração os aprendizados sobre as estruturas condicionais, elabore um algoritmo que possa descobrir, através de perguntas e respostas, qual meio de transporte o usuário está considerando. O usuário deverá escolher uma das seguintes opções:

#- trator;
#- moto;
#- bicicleta.

#Para chegar ao resultado, as perguntas precisam ser respondidas apenas com "Sim" ou "Não".

#Exemplo:
#É terrestre? Sim.
#Cabe apenas uma pessoa? Sim.
#É pesado? Não.
#Tem pedal? Sim.
#Então, o transporte escolhido foi a bicicleta.


def determine_transportation():
    terrestrial = input("É terrestre? (Sim/Não): ")
    if terrestrial == "Não":
        print("O transporte escolhido não pode ser trator, moto ou bicicleta.")
        return

    single_person = input("Cabe apenas uma pessoa? (Sim/Não): ")
    heavy = input("É pesado? (Sim/Não): ")
    pedal = input("Tem pedal? (Sim/Não): ")

    if single_person == "Sim" and heavy == "Não" and pedal == "Sim":
        print("O transporte escolhido foi a bicicleta.")
    elif heavy == "Sim":
        print("O transporte escolhido foi o trator.")
    else:
        print("O transporte escolhido foi a moto.")


determine_transportation()

# 1.Inicialmente, definimos as variável
# 2.A função "pergunta()" é definida para fazer uma pergunta ao usuário
# e armazenar sua resposta na variável "resposta".
# 3.Em seguida, usamos a estrutura condicional "if" para verificar se a resposta do usuário é "Sim".
# Se for, a variável "escolha" é atualizada para "Sim" e a função é chamada novamente para fazer a próxima pergunta.
# Se não for, a variável "escolha" é atualizada para "Não" e o transporte é definido como "Nenhum".
# 4. O programa faz 3 perguntas ao usuário, cada uma relacionada a uma das opções de transporte (trator, moto ou bicicleta).
# Se a resposta do usuário for "Sim" para a primeira pergunta, o transporte é definido como "trator".
# Se a resposta for "Não" para a primeira pergunta, mas "Sim" para a segunda, o transporte é definido como "moto".
# Se as respostas forem "Não" para ambas as primeiras perguntas, mas "Sim" para a terceira, o transporte é definido como "bicicleta".
# 5.Finalmente, o programa imprime o resultado para o usuário, mostrando qual transporte ele escolheu.