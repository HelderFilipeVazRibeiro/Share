#include <stdio.h>
#include <math.h>

int main()
{
    float raio, altura, area_cilindro, quantidade_latas, custo_total, custo_lata=20, litros_lata=5, rendimento_litro=3;

    printf("Qual o raio da base do cilindro: ");
    scanf("%f", &raio);

    printf("Qual a altura do cilindro: ");
    scanf("%f", &altura);

    area_cilindro = 2 * M_PI * pow(raio, 2)+2 * M_PI * raio * altura;  // <-- area total do cilindro
    quantidade_latas = (area_cilindro / rendimento_litro) / litros_lata;
    custo_total = quantidade_latas * custo_lata;

    printf("A area do cilindro é: %.2f metros quadrados\n", area_cilindro);
    printf("A quantidade de latas necessárias são: %.2f\n", quantidade_latas);
    printf("O custo total de pintar o tanque é: %.2f €\n", custo_total);
    return 0;
}
