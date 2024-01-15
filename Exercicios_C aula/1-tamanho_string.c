#include <stdio.h>
#include <string.h>

int main()
{
    char string[100];  // tamanho maximo de caracteres que a string pode ter

    printf("Escreva um conjunto de cacteres para ser lido o seu número: ");
    fgets(string, sizeof(string), stdin);

    // Remove o caractere de nova linha (\n) do final da string
    string[strcspn(string,"\n")] ='\0';
    int comprimento = strlen(string);
    printf("O comprimento da string inserida é: %d\n", comprimento);
    return 0;
}
