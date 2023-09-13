/*
UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
CENTRO DE TECNOLOGIA
DEPARTAMENTO DE ENGENHARIA DE COMPUTAÇÃO E AUTOMAÇÃO
DCA0125 - SISTEMAS DE TEMPO REAL

BRUNO VALNIERY GOMES DE SOUSA - 20210073222

Implementação do seguinte programa:
- O usuário fornece a data de seu aniversário.
- O programa calcula quantos segundos o usuário tem de vida.
*/

#include <stdio.h>
#include <time.h>

int main() {
    // Obtém a data de aniversário do usuário
    int dia, mes, ano;
    printf("Digite sua data de aniversário (dia mês ano): ");
    scanf("%d %d %d", &dia, &mes, &ano);

    // Obtém a data e hora atuais
    time_t agora;
    time(&agora);
    struct tm *data_atual = localtime(&agora);

    // Calcula os segundos de vida
    struct tm data_aniversario = {0};
    data_aniversario.tm_year = ano - 1900;
    data_aniversario.tm_mon = mes - 1;
    data_aniversario.tm_mday = dia;
    
    time_t aniversario_em_segundos = mktime(&data_aniversario);
    time_t diferenca = difftime(agora, aniversario_em_segundos);

    // Exibe a quantidade de segundos de vida
    printf("Você viveu cerca de %ld segundos.\n", diferenca);

    return 0;
}
