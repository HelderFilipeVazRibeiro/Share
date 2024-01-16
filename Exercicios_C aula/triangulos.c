#include <stdio.h>

//funcão core do C
int main() {

//variaveis
float A, B, C;

//pedidos de valores para atribuir às variveis
printf ("\nDigite os lados de um triângulo para definirmos a sua tipologia.\n");

printf ("\nDigite a dimensão do lado A: ");
    scanf ("%f",&A);

printf ("\nDigite a dimensão do lado B: ");
    scanf ("%f",&B);

printf ("\nDigite a dimensão do lado C: ");
    scanf ("%f",&C);

    if (A==B && B==C)
        {
        printf("Triângulo Equilátero\n");
        }
   
    else if (A==B || B==C || A==C)
        {
        printf("Triângulo Escaleno\n");
        }

    else
        printf("Triângulo Isósceles\n");

return 0;	
}




