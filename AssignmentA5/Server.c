// Server side implementation of UDP client-server model 
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/in.h> 
  
#define PORT     5600 
#define MAXLINE 1024 
  
// Driver code 
int main() { 
    int sockfd; 
    char buffer[MAXLINE]; 
    char *hello = "Hello from server"; 
    struct sockaddr_in servaddr, cliaddr; 
      
    // Creating socket file descriptor 
    if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) { 
        perror("socket creation failed"); 
        exit(EXIT_FAILURE); 
    } 
      
    memset(&servaddr, 0, sizeof(servaddr)); 
    memset(&cliaddr, 0, sizeof(cliaddr)); 
      
    // Filling server information 
    servaddr.sin_family    = AF_INET; // IPv4 
    servaddr.sin_addr.s_addr = INADDR_ANY; 
    servaddr.sin_port = htons(PORT); 
      
    // Bind the socket with the server address 
    if ( bind(sockfd, (const struct sockaddr *)&servaddr,  
            sizeof(servaddr)) < 0 ) 
    { 
        perror("bind failed"); 
        exit(EXIT_FAILURE); 
    } 

	int len, n; 
	n = recvfrom(sockfd, (char *)buffer, MAXLINE,  MSG_WAITALL, ( struct sockaddr *) &cliaddr, &len); 
	buffer[n] = '\0'; 
	printf("Client : %s\n", buffer); 
	sendto(sockfd, (const char *)hello, strlen(hello),  MSG_CONFIRM, (const struct sockaddr *) &cliaddr, len); 
	printf("Hello message sent.\n");  
	
	int choice;
	char name[100];
	FILE *fp;
	char *fileContents;
	char c;
	int MAXSIZE = 32;
	
	printf("\nWelcome to File Transfer Program");
	printf("\n1. Transfer a file");
	printf("\n2. Receive a file");
	printf("\nEnter your choice: ");
	scanf("%d", &choice);
	if(choice == 1){
		printf("\nEnter the name of the file to be sent: ");
		scanf("%s", name);	
		printf("\nOpening %s.....", name);
		fp = fopen(name, "r");
		if(fp == NULL){
			printf("\nCannot open the file");
		}
		else{
			printf("\nFile Opened successfully, reading contents....");
		}
		
		while (fgets(fileContents,1024, fp)!=NULL){
        		printf("%s",fileContents);
        	} 
		sendto(sockfd, (const char *)fileContents, strlen(fileContents),  MSG_CONFIRM, (const struct sockaddr *) &cliaddr, len);

	}
	else	
	{

	}
	close(sockfd);
    return 0; 
} 

