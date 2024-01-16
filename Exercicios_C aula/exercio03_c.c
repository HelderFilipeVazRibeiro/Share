#include <stdio.h>

    int main()
    {   
        int c1, c2, c3, c4, c5,c6;
        int a1;

        printf("Linguagem C - exemplificação da aplicação das regras de prioridade dos operadores\n");
        printf("Determinar o resultado das expressões seguintes:\n");
        printf("!((6>=3)&&(5!=6))||10*2>22\n");
            c1=6>=3;
            c2=5!=6;

        printf("= !(%d && %d)||10*2>22\n",c1,c2); //1ª prioridade --> ()
            c3=c1&&c2;
        printf("!(%d)||10*2>22\n",c3); // 1ª prioridade --> ()
            c4=!(c3);
        printf("%d||10*2>22\n",c4); // 2ª prioridade --> !
            a1=10*2;
        printf("%d||%d>22\n",c4,a1); // 3ª prioridade --> *
            c5=a1>22;
        printf("=%d||%d\n",c4,c5); // 7ª prioridade --> ||
            c6=c5||c4;
        printf("=%d",c6);
        return 0;
    }