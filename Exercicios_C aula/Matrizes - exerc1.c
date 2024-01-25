#include <stdio.h>

// solicita os valores ao user
void input_valores_matriz(int matriz[][4]) // a funçãao valores_matriz vai pedir os parametros para a primeira matriz que está vazia e a segunda já tem 4 parametros. valores inteiros
    { 
    for (int i=0; i<4; i++) 
        {
        for (int j=0; j<4; j++)
        { printf("Insira o valor da posição [%i][%i]: ", i, j);
        scanf("%i", &matriz[i][j]);}
        }
    }

//calcular o triplo dos valores
void triplo_matriz(int matriz_original[][4], int matriz_triplo[][4]) // uma vai guardar os valores da variavel i outra da variavel j
{
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {matriz_triplo[i][j] = matriz_original[i][j]*3;}
    }
}

//imprime a matriz
void print_matriz(int matriz[][4]) {
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {printf("%i ", matriz[i][j]);}
    printf("\n");
    }
}

// Função para encontrar o maior valor na matriz
int maior_valor(int matriz[][4])
{
    int maior = matriz[0][0];
    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
            {
            if (matriz[i][j] > maior)
            {maior = matriz[i][j];}
            }
    }
return maior;
}

// Função para encontrar o menor valor na matriz
int menor_valor(int matriz[][4])
{
    int menor = matriz[0][0];
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (matriz[i][j] < menor)
            {menor = matriz[i][j];}
        }
    }
return menor;
}

int main()
{
    int matriz_original[4][4];
    int matriz_triplo[4][4];

    input_valores_matriz(matriz_original);
    triplo_matriz(matriz_original, matriz_triplo);

        printf("Matriz original:");
        print_matriz(matriz_original);

        printf("Matriz triplo:");
        print_matriz(matriz_triplo);

// maior e menor valor das matrizes
    int maior_matriz_original = maior_valor(matriz_original);
    int menor_matriz_original = menor_valor(matriz_original);
    int maior_matriz_triplo = maior_valor(matriz_triplo);
    int menor_matriz_triplo = menor_valor(matriz_triplo);
// saida de dados
    printf("\nO valor maior na matriz original é: %i\n", maior_matriz_original);
    printf("O valor menor na matriz original é: %i\n", menor_matriz_original);
    printf("\nO valor maior na matriz triplo é: %i\n", maior_matriz_triplo);
    printf("O valor menor na matriz triplo é: %i\n", menor_matriz_triplo);
return 0;
}