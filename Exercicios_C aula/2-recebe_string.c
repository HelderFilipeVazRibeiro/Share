#include <stdio.h>
#include <string.h>

int main()
{
    char string[100]; // tamanho maximo para a string só recebe 99 pois 0 ocupa 1 slot
    int input_caracteres, Quantidade_A = 0, Quantidade_E = 0, Quantidade_I = 0, Quantidade_O = 0, Quantidade_U = 0; // para contar cada uma das vogais quantidade*100/comprimento da string

    printf("Escreva um conjunto de caracteres para serem lidas a quantidade de vogais e percentagem de utilização: ");
    fgets(string, sizeof(string),stdin); //lê alinha e sizeof retorna o tamanho da string 

    // Remove o caractere de nova linha (\n) do final da string
    string[strcspn(string, "\n")] = '\0';

    int comprimento_string = strlen(string); // ajusta a string lida com fgets para garantir que qualquer caractere de nova linha no final seja removido e que a string seja terminada corretamente com '\0'

    // contador de cada vogal e todos os caracteres
    for (int i = 0; string[i] != '\0'; i++)
    {
    char input_caracteres = string[i]; // Caractere como número inteiro

        if ((input_caracteres>='a' && input_caracteres <= 'z') || (input_caracteres>='A' && input_caracteres<='Z'))
        {
            if (input_caracteres=='a' || input_caracteres=='A')
            {
            Quantidade_A++;
            }
            else if (input_caracteres=='e' || input_caracteres =='E')
            {
            Quantidade_E++;
            } 
            else if (input_caracteres=='i' || input_caracteres=='I')
            {
            Quantidade_I++;
            }
            else if (input_caracteres=='o' || input_caracteres=='O')
            {
            Quantidade_O++;
            } else if (input_caracteres=='u' || input_caracteres=='U')
            {
            Quantidade_U++;
            }
        }
    }
// Saida de dados, resultados
if (comprimento_string>0)
    {
    printf("O comprimento da string é: %d\n",comprimento_string);
    printf("O numero de vogais presente na string é:\n");
    printf("A: %d\n",Quantidade_A);
    printf("E: %d\n",Quantidade_E);
    printf("I: %d\n",Quantidade_I);
    printf("O: %d\n",Quantidade_O);
    printf("U: %d\n",Quantidade_U);
    }
    else
    printf("Não existem caracteres\n");
    // Calculo da percentagem
    if (comprimento_string > 0)
    {
        printf("Porcentagem de cada vogal:\n");
        printf("A: %.2f%%\n",(float)(Quantidade_A*100)/comprimento_string);
        printf("E: %.2f%%\n",(float)(Quantidade_E*100)/comprimento_string);
        printf("I: %.2f%%\n",(float)(Quantidade_I*100)/comprimento_string);
        printf("O: %.2f%%\n",(float)(Quantidade_O*100)/comprimento_string);
        printf("U: %.2f%%\n",(float)(Quantidade_U*100)/comprimento_string);
    }
    else
    printf("Não temos dados para calcular a percentagem!\n");
    return 0;
}