#include <stdio.h>

int main()
{
    int V[4][3]; // imaginar que cria 4 linhas e 3 colunas. nomes depois os meses

    printf("Insisra os valores das vendas:\n");
    for (int i = 0; i<4; i++)
    {
        for (int j = 0; j<3; j++)
        {
        printf("Vendas do funcionário %i no mês %i: ", i + 1, j + 1);
        scanf("%i", &V[i][j]);
        }
    }

    printf("\nInsira o índice do funcionário que pretende consultar: ");
    int indice_funcionario;
    scanf("%i", &indice_funcionario);

    printf("\nAs vendas do funcionário %i são: ", indice_funcionario + 1);
    for (int j = 0; j < 3; j++)
    {
        printf("%i ", V[indice_funcionario][j]);
    }


    printf("\nInsira o índice do mês que pretende consultar: ");
    int indice_mes;
    scanf("%i", &indice_mes);

    printf("\nAs vendas do mês %i são: ", indice_mes + 1);
    for (int i=0; i<4; i++)
    {
        printf("%i ", V[i][indice_mes]);
    }
    
return 0;
}