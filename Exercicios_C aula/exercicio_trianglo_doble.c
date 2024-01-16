#include <stdio.h>

int main() {
    // Declaração das variáveis A, B e C
    double A, B, C;

    // Solicitar ao usuário que insira os valores
    printf("Digite o valor de A: ");
    scanf("%lf", &A);

    printf("Digite o valor de B: ");
    scanf("%lf", &B);

    printf("Digite o valor de C: ");
    scanf("%lf", &C);

    // Verificar se os lados formam um triângulo
    if (A + B > C && A + C > B && B + C > A) {
        // Verificar o tipo de triângulo
        if (A == B && B == C) {
            printf("Os lados formam um triângulo equilátero.\n");
        } else if (A == B || A == C || B == C) {
            printf("Os lados formam um triângulo isósceles.\n");
        } else {
            printf("Os lados formam um triângulo escaleno.\n");
        }
    } else {
        printf("Os lados fornecidos não formam um triângulo.\n");
    }

    return 0;
}