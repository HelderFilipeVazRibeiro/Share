#include <stdio.h>
#include <stdlib.h>

int main(void) {

    int lim_inf, lim_sup, n;

    printf("Indique o limite inferior do intervalo: ");
    scanf("%i",&lim_inf);
    printf("Indique o limite superior do intervalo: ");
    scanf("%i",&lim_sup);

    if (lim_inf>=lim_sup)
    {
        printf("Os valores indicados estão errados,%i é maior ou igual a %i\n",lim_inf, lim_sup);
        printf("Pressione Enter para continuar...");
        getchar();
    }
    else
    {
        for (n=lim_inf; n < lim_sup;n++)
        {
            printf("%i\n",n);
        }
    }
    return 0;
}
