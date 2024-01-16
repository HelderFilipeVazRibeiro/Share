#include <stdio.h>
#include <math.h>

int CUSTO_LATA=20, CAPACIDADE_LATA=5, RENDIMENTO_TINTA=3

// function for calculate total area of cylinder
double calcularAreaBase(double raio) {
    return M_PI * raio * raio;
}

// function for calculate total area cylinder
double calcularAreaTotal(double raio, double altura) {
    return 2 * calcularAreaBase(raio) + 2 * M_PI * raio * altura;
}

// functions for calculate cans are needed
int calcularQuantidadeLatas(double areaTotal) {
    return (int)ceil(areaTotal / (CAPACIDADE_LATA * RENDIMENTO_TINTA));
}

// function for calculate total coast 
double calcularCustoTotal(int quantidadeLatas) {
    return quantidadeLatas * CUSTO_LATA;
}

int main() {
    double raio, altura;

    // Obter entrada do usuário para raio e altura
    printf("Informe o raio do cilindro: ");
    scanf("%lf", &raio);

    printf("Informe a altura do cilindro: ");
    scanf("%lf", &altura);

    // calcular a área total do cylinder
    double areaTotal = calcularAreaTotal(raio, altura);

    // calcular a quantidade de latas
    int quantidadeLatas = calcularQuantidadeLatas(areaTotal);

    //calcular o custo total
    double custoTotal = calcularCustoTotal(quantidadeLatas);

    //print result
    printf("Quantidade de latas necessárias: %d\n", quantidadeLatas);
    printf("Custo total: %.2f €\n", custoTotal);

    return 0;
}