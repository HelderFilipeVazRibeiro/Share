#include <stdio.h>

// Função calcular a média de 3 notas
float media(float n1, float n2, float n3)
{
  return (n1 + n2 + n3) / 3;
}

int main()
{
  float n1, n2, n3;
  printf("Digite o valor das suas 3 ultimas notas para calcular a média:\n");
  printf("primeira nota:\n");
  scanf("%f", &n1);
  printf("segunda nota:\n");
  scanf("%f", &n2);
  printf("terceira nota:\n");
  scanf("%f", &n3);

    // calcular a media, podemos chamar varios valores separando por virgula <---- importante!
    float result_media = media(n1, n2, n3);

  // media
  printf("A média é %.2f\n", result_media);

  return 0;
}