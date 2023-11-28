#include <stdio.h>
#include <stdlib.h>

int main() {
    float consumo_carro, cons_viagem, pre_unirario=2.00;
    int dist;

    printf("Digite o consumo médio do veiculo(Litros/Km):\n");
    scanf("%f", &consumo_carro); 

    printf("Digite a distância a percorrer (em kms):\n");
    scanf("%d", &dist);

    cons_viagem = (dist / consumo_carro)*pre_unirario;

    printf("Tendo em conta que vamos percorrer, %d kms e o preço do combustivél é de %.1f € por litro, o custo estimado da viagem é de: %.1f€", dist, pre_unirario, cons_viagem);
    return 0;
}