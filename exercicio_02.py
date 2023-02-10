'''Após uma prova de vestibular, uma escola quer identificar quantos dos seus alunos foram aprovados em cada turma de formandos.
Ela quer saber qual aluno teve a maior nota e de qual turma ele é. Nessa escola, há quatro turmas (A, B, C e D) com vinte e cinco alunos cada.
crie um código em python  que solicite o nome e a nota do vestibular aos alunos.
Depois, informe quantos deles foram aprovados, de que turma são, qual a maior nota em cada turma e qual aluno teve a maior nota de todas.
Para que o aluno seja aprovado no vestibular, ele deverá obter nota maior ou igual a 7.
ATENÇÃO: As notas por turma não podem se repetir.'''

# Define a quantidade de alunos por turma e a nota mínima para aprovação
qtd_alunos = 25
nota_minima = 7

# Inicializa as variáveis de contagem
aprovados = 0
turma_a = 0
turma_b = 0
turma_c = 0
turma_d = 0

# Inicializa as variáveis para armazenar a maior nota de cada turma
maior_nota_turma_a = 0
maior_nota_turma_b = 0
maior_nota_turma_c = 0
maior_nota_turma_d = 0

# Inicializa a variável para armazenar a maior nota de todas as turmas
maior_nota = 0

# Inicializa a variável para armazenar o nome do aluno com a maior nota
nome_maior_nota = ""

# Loop para ler os dados de todos os alunos
for i in range(qtd_alunos * 4):
    # Solicita o nome do aluno
    nome = input("Digite o nome do aluno: ")

    # Solicita a nota do vestibular
    nota = float(input("Digite a nota do vestibular: "))

    # Verifica se o aluno foi aprovado
    if nota >= nota_minima:
        aprovados += 1

        # Verifica qual turma o aluno pertence
        turma = input("Digite a turma do aluno (A, B, C ou D): ")

        # Verifica se a nota do aluno é maior que a maior nota da turma
        if turma == "A" and nota > maior_nota_turma_a:
            maior_nota_turma_a = nota
            nome_maior_nota_turma_a = nome
            turma_a += 1
        elif turma == "B" and nota > maior_nota_turma_b:
            maior_nota_turma_b = nota
            nome_maior_nota_turma_b = nome
            turma_b += 1
        elif turma == "C" and nota > maior_nota_turma_c:
            maior_nota_turma_c = nota
            nome_maior_nota_turma_c = nome
            turma_c += 1
        elif turma == "D" and nota > maior_nota_turma_d:
            maior_nota_turma_d = nota
            nome_maior_nota_turma_d = nome
            turma_d += 1

        # Verifica se a nota do aluno é a maior de todas
 '''O código em Python começa pedindo for que itera 100 vezes,
  solicitando essas informações do usuário e armazenando-as em uma lista de dicionários,
   onde cada dicionário representa um aluno e seus respectivos dados.'''