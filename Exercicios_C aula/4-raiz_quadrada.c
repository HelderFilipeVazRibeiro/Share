#include <stdio.h>
#include <math.h>

int main()
{
    float num;

    printf("Digite um número para saber a sua raiz quadrada: ");
    scanf("%f", &num);
    
        if (num>=0)
        {
        float raizQuadrada = sqrt(num);
        printf("A raiz quadrada de %.2f é %.2f\n", num, raizQuadrada);
        }
        else {
        printf("Não é possivel calcular a raiz quadrada de 0 ou um número negativo.\n");
        }
    return 0;
}
