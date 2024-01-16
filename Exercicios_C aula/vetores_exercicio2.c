#include <stdio.h>

int main()
{
    int tamanho = 8;
    int num[tamanho];

    printf("Adicione 8 numeros à sua lista:\n"); // adiciona ao array os valors do input
    for (int i = 0; i < tamanho; i++)
        {
        printf("%i: ", i + 1);
        scanf("%i", &num[i]);
        }

    printf("Os números introduzidos são:\n");
    for (int i = 0; i < tamanho; i++)
    {
    printf("%i ", num[i]);
    }

     int cont_maior30 = 0; // contador dos numeros maiores que 30

    for (int i = 0; i < tamanho; i++)
    {
        if (num[i] > 30)
        {cont_maior30++;}
    }

    if (cont_maior30 > 0)
    {
    printf("\nExistem %i numeros maiores que 30\n", cont_maior30);
    }
    else
    {
    printf("\nNão existem numeros maiores que 30.\n");
    }
return 0;
}