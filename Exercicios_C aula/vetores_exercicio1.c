#include <stdio.h>

int main()
{
    int tamanho = 10;
    int num_pares[tamanho];
    
    for (int i = 0, valor = 2; i < tamanho; i++, valor += 2) //soma de 2 em 2 ate ocupar os 10 lugares do vetor
    {
        num_pares[i] = valor;
    }
    printf("Numeros pares de 2 até ao 20:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", num_pares[i]);
    }
return 0;
}
