#include <stdio.h>

//calcula o preço final com percentagem
float preco_final(float preco_prod, float percentagem_desconto)
{
    float desconto = (percentagem_desconto/100) * preco_prod;
    float valor_novo = preco_prod-desconto;
    return (valor_novo);
}
int main()
{
    float preco_prod, percentagem_desconto;

    printf("Informe o valor do produto: ");
    scanf("%f", &preco_prod);
    printf("Informe a percentagem de desconto: ");
    scanf("%f", &percentagem_desconto);

        float valor_novo=preco_final(preco_prod, percentagem_desconto);
        printf("O novo valor do produto com %.2f%% de desconto é %.2f€\n", percentagem_desconto, valor_novo);
    return 0;
}