''' Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:

- use a função realloc;
- use a função sizeof;
- que tenha tamanho 22 de vetor;
- depois libere o bloco utilizando a função free.'''


# include <stdio.h>
# include <stdlib.h>

int
main()
{
    int
tamanho = 22;
int * vetor = (int *)
malloc(tamanho * sizeof(int));

if (vetor == NULL)
{
    printf("Erro ao alocar memória\n");
return 1;
}

printf("Tamanho do vetor: %lu bytes\n", tamanho * sizeof(int));

int
novo_tamanho = 33;
vetor = (int *)
realloc(vetor, novo_tamanho * sizeof(int));

if (vetor == NULL)
{
printf("Erro ao redimensionar memória\n");
return 1;
}

printf("Novo tamanho do vetor: %lu bytes\n", novo_tamanho * sizeof(int));

free(vetor);

return 0;
}
