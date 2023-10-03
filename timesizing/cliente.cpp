#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>

using namespace std;

int main() {
    int sockfd;
    struct sockaddr_in server_addr;
    socklen_t server_len = sizeof(server_addr);

    // Criar um socket UDP
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd == -1) {
        cerr << "Erro ao criar o socket." << endl;
        return 1;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(9734); // Porta do servidor
    server_addr.sin_addr.s_addr = inet_addr("IP_DO_SERVIDOR"); // Endereço IP do servidor

    // Dados a serem enviados
    const char* message = "Mensagem de teste";
    int message_size = strlen(message);

    // Medir o tempo de envio
    struct timeval start_time, end_time;
    gettimeofday(&start_time, NULL);

    // Enviar a mensagem para o servidor
    sendto(sockfd, message, message_size, 0, (struct sockaddr*)&server_addr, server_len);

    // Receber a resposta do servidor (se necessário)
    // recvfrom(...);

    gettimeofday(&end_time, NULL);

    // Calcular o tempo de processamento
    double elapsed_time = (end_time.tv_sec - start_time.tv_sec) + (end_time.tv_usec - start_time.tv_usec) / 1e6;

    cout << "Tempo de processamento e comunicação: " << elapsed_time << " segundos." << endl;

    close(sockfd);
    return 0;
}
