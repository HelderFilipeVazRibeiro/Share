#include <stdio.h>

/* Funçao para verificar se um número é primo */
int Primo(int n)
{
  int i;
  /* Se o numero for menor ou igual a 1 não é primo */
    if (n <= 1) {
    return 0;
    }
  /* Verifica se o número é divisível por algum número de 2 até a metade dele */
     for (i = 2; i <= n / 2; i++)
     {
        if (n % i == 0)
    {
    return 0;
    }
    }

  /* Se o número não for divisível por nenhum número de 2 até a metade dele */
  return 1;
}

int main() {
  int n;

  printf("Digite um número: ");
  scanf("%d", &n);

  if (Primo(n)) {
    printf("O número %d é primo.\n", n);
  } else {
    printf("O número %d não é primo.\n", n);
  }

  return 0;
}