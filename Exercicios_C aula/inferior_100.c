#include <stdio.h>

int main() {
    int num, somatorio = 0, contador = 0;
    
    while (somatorio < 500) {
        printf("Introduza um valor inferior a 100: ");
        scanf("%i", &num);

        // Validar se o valor é inferior ou igual a 100 
        if (num <= 100) {
            somatorio += num;
            contador++;
        } else {
            printf("Valor invalido tente novamente.\n");
        }
    }

    // Calcula media
    float media = (float)somatorio / contador;

    // Imprimir resultados
    printf("\nSomatório: %i\n", somatorio);
    printf("Média: %.2f\n", media);

    printf("\nBom trabalho, continua assim!\n");
    return 0;
}