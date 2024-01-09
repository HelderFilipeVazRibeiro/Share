#include <stdio.h>

/* Funçao para verificar se um número é primo */
int primo(int num)
{
  int i;
  /* Se o numero for menor ou igual a 1 não é primo */
    if (num <= 1)
    {
    return 0;
    }
  /* Verifica se o número é divisível por algum número de 2 até a metade dele */
     for (i = 2; i <= num/2; i++)
     {
        if (num % i==0)
    {
    return 0;
    }
    }

  /* Se o número não for divisível por nenhum número de 2 até a metade dele */
  return 1;
}

int main() 
{
  int num;

  printf("Digite um número: ");
  scanf("%i", &num);

  if (primo(num)) 
  {
    printf("O numero %i é primo!\n", num);
  } 

  else
  {
    printf("O numero %i não é primo!\n", num);
  }

  return 0;
}