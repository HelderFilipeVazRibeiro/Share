#include <stdio.h>

int main()
{
    int num_alunos = 6;
    char nomes[num_alunos][100], situacao[num_alunos][50]; 
    float notasPR1[num_alunos], notasPR2[num_alunos], notasPR3[num_alunos],medias[num_alunos];

    //para
    for (int i = 0; i<num_alunos; i++)
    {
        printf("Digite o nome do aluno %d: ", i + 1);
        scanf("%s", nomes[i]);
        printf("Digite a nota da PR1 para o aluno %d: ", i+1);
        scanf("%f", &notasPR1[i]);
        printf("Digite a nota da PR2 para o aluno %d: ", i+1);
        scanf("%f", &notasPR2[i]);
        printf("Digite a nota da PR3 para o aluno %d: ", i+1);
        scanf("%f", &notasPR3[i]);

    medias[i] = (notasPR1[i] + notasPR2[i] + notasPR3[i])/3;
        // se
        if (medias[i] >= 10)
        {
        snprintf(situacao[i], sizeof(situacao[i]), "Aprovado com sucesso!");
        } 
        else
        {
        snprintf(situacao[i], sizeof(situacao[i]), "Reprovado, volta para o ano!");
        }
    }
    printf("Resultados:\n"); 
    for (int i = 0; i < num_alunos; i++)
    {
        printf("Aluno: %s\n", nomes[i]);
        printf("Média: %.2f\n", medias[i]);
        printf("Situação: %s\n\n", situacao[i]);
    }
    return 0;
}
