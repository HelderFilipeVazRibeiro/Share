#include <stdio.h>

// Função para calcular o novo valor do produto com base na percentagem de desconto
float calcularNovoValor(float valorProduto, float percentualDesconto) {
    // Calcula o valor do desconto
    float desconto = (percentualDesconto / 100) * valorProduto;

    // Calcula o novo valor do produto após o desconto
    float novoValor = valorProduto - desconto;

    return novoValor;
}

int main() {
    // Declaração de variáveis
    float valorProduto, percentualDesconto;

    // Leitura do valor do produto e percentual de desconto
    printf("Informe o valor do produto: ");
    scanf("%f", &valorProduto);
    
    printf("Informe a percentagem de desconto: ");
    scanf("%f", &percentualDesconto);

    // Chamada da função para calcular o novo valor do produto
    float novoValor = calcularNovoValor(valorProduto, percentualDesconto);

    // Exibição do resultado
    printf("O novo valor do produto com %.2f%% de desconto é %.2f\n", percentualDesconto, novoValor);

    return 0;
}