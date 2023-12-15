/* Jogo Matrecos:
Implemente um programa em Linguagem C que registe o resultado de um jogo de Matrecos.
Neste  jogo  vamos  ter  9  bolas  e  o  jogo  acabará  após  os  9  golos registados.
O jogo será entre os Vermelhos (‘V’) e os Azuis (‘A’).
Cada vez que os vermelhos marcarem um golo será premido o caráter ‘V’, quando for golo dos Azuis  será  premido  o  caráter ‘A’, o  programa  deve  irmostrando o  resultado atual.  
Após  os  9  golos  introduzidos  deverá  mostrar  qual  a  equipa  vencedora  e qual o resultado obtido.
O programa apenas deve aceitar as letras a, A, v ou V, caso contrário deve voltar a pedir o golo obtido.
No final do jogo deve mostrar se  pretende  jogar  novamente,  se  sim,  repete  todo  o  jogo,  se  não,  termina  o programa.   */

#include <stdio.h>
#include <stdlib.h>

int main() {
    // variaveis
    char golos;
    int golos_V = 0, golos_A = 0; //inicializar var
    
    // ciclo do while - inicio
    do {
        // perguntar e responder com os resultados do jogo
        for (int i = 0; i < 9; i++) {
            printf("Jogo a decorrer! Vermelhos: %d, Azuis: %d\n", golos_V, golos_A);
            printf("Introduza o resultado (V para Vermelhos, A para Azuis): ");
            scanf(" %c", &golos);

            // Validar entrada, maiusculas e minusculas
            if (golos == 'V' || golos == 'v') {
                golos_V++; // incrementa o golo em v
            } else if (golos == 'A' || golos == 'a') {
                golos_A++;// incrementa o golo em a
            } else {
                printf("Entrada invalida. Introduza V ou A\n");
                i--;  // Repetir para corrigir a entrada inválida
            }
        }

        //resultado final
        printf("\nFim do jogo! - Vermelhos: %d, Azuis: %d\n", golos_V, golos_A);

        // maior que, para determinar o vencedor
        if (golos_V > golos_A) { // >>>>>>>>>>>>>>>>>>>> vermelhos marcaram mais que os azuis
            printf("Vermelhos são so vencedores!\n");
        } else if (golos_A > golos_V) { // >>>>>>>>>>>>>>>>>>>> azuis marcaram mais que os vermelhos
            printf("Azuis são so vencedores!\n");
        } else {
            printf("EMPATE!\n"); // aplica-se quando número de jogas forem pares
        }

        // Perguntar se deseja jogar novamente
        printf("Deseja jogar novamente? (s/n): ");
        scanf(" %c", &golos);

        // Reiniciar as variáveis para um novo jogo senão continua as jogadas anteriores
        golos_V = 0;
        golos_A = 0;

    } while (golos == 's' || golos == 'S');   // fim do ciclo do while

    printf("Obrigado! Até o próximo jogo!\n");

    return 0;
}
