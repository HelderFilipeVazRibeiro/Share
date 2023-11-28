#include <stdio.h>
#include <stdlib.h>

int main() {
    char nome[60];  // Array de tamanho de caracteres
    float peso, altura, imc;
    int idade;

    printf("Escreva o seu nome:\n");
    scanf("%s", nome); 

    printf("A sua idade é:\n");
    scanf("%i", &idade);

    printf("O seu peso é (KG):\n");
    scanf("%f", &peso);

    printf("A sua altura é (cm):\n");
    scanf("%f", &altura);

    altura = altura/100;
    imc = (peso/(altura*altura));

    printf("O meu nome é %s , tenho %i anos, o meu peso é %.2f kgs, a minha altura é de %.2f Metros, sendo o meu IMC de: %.2f ", nome, idade, peso, altura, imc);
    return 0;
}