''' Construa um algoritmo de ordenação, utilizando o método bubble sort estudado.
 (Lembre-se que se trata de uma série de instruções que devem ser seguidas passo a passo).
Para isso, você deve criar um método em que o tamanho do vetor seja dez e deve estar em ordem crescente.

O vetor deverá:
- comparar seus elementos dois a dois adjacentes;
- se os elementos não estiverem em ordem, então ordenar;
- senão, avançar para o próximo par;
- repetir a operação até que nenhuma troca possa ser feita no vetor inteiro.'''

def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor

vetor = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Vetor desordenado:", vetor)
vetor = bubble_sort(vetor)
print("Vetor ordenado:", vetor)
