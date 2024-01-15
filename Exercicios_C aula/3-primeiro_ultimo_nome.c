#include <stdio.h>
#include <string.h>

int main()
{
    char primeiro_nome[20];
    char apelido[20];

    printf("Digite o seu primeiro nome: ");
    fgets(primeiro_nome, sizeof(primeiro_nome), stdin);
    primeiro_nome[strcspn(primeiro_nome, "\n")] = '\0';  // Remover o caractere de nova linha

    printf("Digite o seu apelido: ");
    fgets(apelido, sizeof(apelido), stdin);
    apelido[strcspn(apelido, "\n")] = '\0';  // Remover o caractere de nova linha

    // concatenar os 2 nomes
    char nome_completo[100];
    strcpy(nome_completo, primeiro_nome);
    strcat(nome_completo, " ");  // Adicionar espaço
    strcat(nome_completo, apelido);

    printf("Nome completo: %s\n", nome_completo);
    return 0;
}
