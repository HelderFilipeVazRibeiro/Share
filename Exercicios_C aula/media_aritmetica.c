#include <stdio.h>
#include <stdlib.h>

int main() {
    char aluno[30];  // Array de caracteres para o nome do aluno
    float nota1, nota2, nota3, media_aluno;

    // Pedir a identificação do aluno
    printf("Escreva o nome do aluno:\n");
    scanf("%s", aluno);  //Usa %s para ler uma string de caracteres, ou seja [n de caractere]

    printf("Nota da 1ª avaliação:\n");
    scanf("%f", &nota1);

    printf("Nota da 2ª avaliação:\n");
    scanf("%f", &nota2);

    printf("Nota da 3ª avaliação:\n");
    scanf("%f", &nota3);

    media_aluno = (nota1 + nota2 + nota3) / 3;

    printf("A média das 3 avaliações para o aluno %s é de: %.2f\n", aluno, media_aluno);
    return 0;
}