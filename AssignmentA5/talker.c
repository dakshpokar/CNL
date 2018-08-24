#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<errno.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<netdb.h>
#define LPORT 3160;

int main(int argc, char *argv[]){
	int sockfd;
	struct sockaddr_in their_addr;
	int numbytes;
	if(argc!=3){
		fprintf(stderr, "usage: talker hostname message \n");
		exit(1);
	}
	their_addr.sin_family = ;
	their_addr.sin_port = htons();
	inet_aton(,);
	memset(&(their_addr.sin_zero),"\0",8);
	if((numbytes=sendto(_,_,_,0,_,_)) == -1){
		perror("sendto");
		exit(1);
	}
	printf("send %d bytes to %s IP address: \n", _, inet_ntoa(_));
	close(sockfd);
	return 0;
}
