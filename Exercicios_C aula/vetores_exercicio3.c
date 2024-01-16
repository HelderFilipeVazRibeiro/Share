#include <stdio.h>
#include <string.h>

int main()
{
    int tamanho = 100;
    char nome_1[tamanho];
    char nome_2[tamanho];
    char nome_3[tamanho];

    printf("Digite o primeiro nome: ");
    fgets(nome_1, tamanho, stdin);
    nome_1[strcspn(nome_1, "\n")] = '\0'; // removequebra de linha inserida pelo fgets

    printf("Digite o segundo nome: ");
    fgets(nome_2, tamanho, stdin);
    nome_2[strcspn(nome_2, "\n")] = '\0';

    printf("Digite o terceiro nome: ");
    fgets(nome_3, tamanho, stdin);
    nome_3[strcspn(nome_3, "\n")] = '\0';

    // contador letras
    int cont_A = 0;
    int cont_E = 0;

    for (int i = 0; nome_3[i] != '\0'; i++)
    {
    if (nome_3[i] =='A' || nome_3[i] =='a')
        {cont_A++;}
    if (nome_3[i]=='E' || nome_3[i]=='e') 
    {cont_E++;}
    }

    // Exibindo os resultados
    printf("Existem  %i letras 'A' no terceiro nome\n", cont_A);
    printf("Exitem %i de letras 'E' no terceiro nome\n", cont_E);

return 0;
}
