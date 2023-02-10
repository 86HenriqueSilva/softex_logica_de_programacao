'''Faça um algoritmo de ordenação utilizando o método insertion sort.
Crie um método que execute as seguintes operações:

- Tamanho do vetor: 30;
- Utilize números ímpares;
- Opere em ordem crescente.'''

def insertion_sort(vetor):
    n = len(vetor)
    for i in range(1, n):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and chave < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    return vetor

vetor = [35, 21, 7, 3, 1, 19, 27, 11, 9, 5, 15, 17, 13, 25, 29, 23, 31, 33, 37, 39, 43, 41, 45, 47, 49, 51, 53, 55, 57, 59]
print("Vetor desordenado:", vetor)
vetor = insertion_sort(vetor)
print("Vetor ordenado:", vetor)
