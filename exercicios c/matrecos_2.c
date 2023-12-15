#include <stdio.h>

int main() {
    char resultado[10];
    int golosVermelhos = 0, golosAzuis = 0;

    printf("Jogo de Matrecos\n");

    for (int i = 0; i < 9; ++i) {
        char golo;

        do {
            printf("Introduza o golo (V/A): ");
            scanf(" %c", &golo);

            // Converte o caractere para maiúscula para facilitar a comparação
            golo = toupper(golo);

        } while (golo != 'V' && golo != 'A');

        resultado[i] = golo;

        if (golo == 'V') {
            golosVermelhos++;
        } else {
            golosAzuis++;
        }

        printf("Resultado: Vermelhos %d - %d Azuis\n", golosVermelhos, golosAzuis);
    }

    printf("Jogo terminado!\n");

    if (golosVermelhos > golosAzuis) {
        printf("Vermelhos venceram por %d-%d\n", golosVermelhos, golosAzuis);
    } else if (golosAzuis > golosVermelhos) {
        printf("Azuis venceram por %d-%d\n", golosAzuis, golosVermelhos);
    } else {
        printf("Empate! O resultado final é %d-%d\n", golosVermelhos, golosAzuis);
    }

    char jogarNovamente;
    printf("Pretende jogar novamente? (S/N): ");
    scanf(" %c", &jogarNovamente);

    if (toupper(jogarNovamente) == 'S') {
        // Reiniciar o jogo
        main();
    } else {
        printf("Obrigado por jogar!\n");
    }

    return 0;
}