#include <stdio.h>
void Asteriscos()
{ int i;
    for (i = 1; i <= 30; i++)
        printf("*");
    printf("\n");
}
void ABC (int a)
{ int i;
    for (i = 0; i <= a; i++)
        printf("ABC-");
    printf("\n");
}
main()
{Asteriscos();
Asteriscos();
ABC(6); ABC(6);
ABC(4); ABC(2);
ABC(4);ABC(6);ABC(6);
Asteriscos();Asteriscos();Asteriscos();
}
