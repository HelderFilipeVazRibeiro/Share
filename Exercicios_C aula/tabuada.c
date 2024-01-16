#include <stdio.h>
#include <stdlib.h>

int main(void) {

    int n, i;
    for (i=1;i<= 10;i++) 
    {
        printf("Tabuada do %d\n",i);
        for (n=1;n<=10;n++) 
        {
            printf("%d x %d = %d\n",i,n,i*n);
        }  
        printf("Pressione Enter para continuar...");
        getchar();
        system ("clear");
       // system("pause");
    }return 0;
}
