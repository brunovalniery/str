#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>

using namespace std;

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);

    // Criar um socket UDP
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd == -1) {
        cerr << "Erro ao criar o socket." << endl;
        return 1;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(9734); // Porta do servidor
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Vincular o socket ao endereço do servidor
    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        cerr << "Erro ao vincular o socket." << endl;
        return 1;
    }

    while (true) {
        char buffer[1024];
        int received_bytes;

        // Receber dados do cliente
        received_bytes = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&client_addr, &client_len);
        if (received_bytes == -1) {
            cerr << "Erro ao receber dados." << endl;
            continue;
        }

        // Processar os dados (se necessário)

        // Enviar uma resposta ao cliente (se necessário)
        // sendto(...);
    }

    close(sockfd);
    return 0;
}
