#include <stdio.h>

//função calcular dobro
int dobro(int n) {
  return n * 2;
}

int main()
{
int n1, n2, n3;

  //Ler os numeros
  printf("Digite os números que quer calcular o dobro:\n");
  printf("O 1º número é:\n");
  scanf("%i", &n1);
  printf("O 2º número é:\n");
  scanf("%i", &n2);
  printf("O 3º número é:\n");
  scanf("%i", &n3);

  // Chamada da função para calcular o dobro de cada número
  int dobro_1 = dobro(n1);
  int dobro_2 = dobro(n2);
  int dobro_3 = dobro(n3);

  // Impressão do resultado
  printf("O dobro do primeiro número é %i\n", dobro_1);
  printf("O dobro do segundo número é %i\n", dobro_2);
  printf("O dobro do terceiro número é %i\n", dobro_3);

return 0;
}