#include <stdio.h>
#include <math.h>

int main() {
    float numero, resultado;
    int expoente;

    printf("Escreva um número: ");
    scanf("%f", &numero);

    printf("escreva um expoente: ");
    scanf("%i", &expoente);

    resultado = pow(numero, expoente);
    printf("%.2f elevado a %i é %.2f\n", numero, expoente, resultado);
    return 0;
}
