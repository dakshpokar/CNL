// Server side C/C++ program to demonstrate Socket programming 
#include <unistd.h> 
#include <stdio.h> 
#include <sys/socket.h> 
#include <stdlib.h> 
#include <netinet/in.h> 
#include <iostream>
#include <string.h>
#include <math.h> 
#define PORT 8082
#define PI 3.14159265
using namespace std;
int main(int argc, char const *argv[]) 
{ 
	int server_fd, new_socket, valread; 
	struct sockaddr_in address; 
	int opt = 1; 
	int addrlen = sizeof(address); 
	char buffer[1024] = {0}; 
	char *hello = "Hello from server"; 

	// Creating socket file descriptor 
	if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) 
	{ 
	perror("socket failed"); 
	exit(EXIT_FAILURE); 
	} 

	// Forcefully attaching socket to the port 8080 
	if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, 
		                                  &opt, sizeof(opt))) 
	{ 
	perror("setsockopt"); 
	exit(EXIT_FAILURE); 
	} 
	address.sin_family = AF_INET; 
	address.sin_addr.s_addr = INADDR_ANY; 
	address.sin_port = htons( PORT ); 

	// Forcefully attaching socket to the port 8080 
	if (bind(server_fd, (struct sockaddr *)&address,  
		                 sizeof(address))<0) 
	{ 
	perror("bind failed"); 
	exit(EXIT_FAILURE); 
	} 
	if (listen(server_fd, 3) < 0) 
	{ 
	perror("listen"); 
	exit(EXIT_FAILURE); 
	} 
	if ((new_socket = accept(server_fd, (struct sockaddr *)&address,  
		       (socklen_t*)&addrlen))<0) 
	{ 
	perror("accept"); 
	exit(EXIT_FAILURE); 
	} 

	//printf("%s\n",buffer ); 
	//send(new_socket , hello , strlen(hello) , 0 ); 
	//printf("Hello message sent\n"); 
	char *ch;
	int choice;
	double angle;
	double calc;
	while(!(strcmp(buffer, "exit") == 0)){
		valread = read( new_socket , buffer, 1024); 
		if(strcmp(buffer,"hello") == 0){
			send(new_socket , hello , strlen(hello) , 0 ); 
			printf("Hello message sent\n"); 
		}
		else if(strcmp(buffer,"file") == 0){
			cout<<"\nFile Transfer";
			ch = "file";
			send(new_socket, ch, strlen(ch), 0);
		}
		else if(strcmp(buffer,"trig") == 0){
			ch = "trig";
			send(new_socket, ch, strlen(ch), 0);
			valread = read(new_socket, &choice, sizeof(choice));
			cout<<choice;
			valread = read(new_socket, &angle, sizeof(angle));
			switch(choice){
				case 1: 
					cout<<"\n Calculating Sine...";
					calc = sin((PI/180)*angle);
					send(new_socket, &calc, sizeof(calc), 0);
					break;
				case 2:
					cout<<"\nCosine";
					calc = cos((PI/180)*angle);
					send(new_socket, &calc, sizeof(calc), 0);
					break;
				case 3:
					cout<<"\nTangent";
					calc = tan((PI/180)*angle);
					send(new_socket, &calc, sizeof(calc), 0);
					break;
				case 4:
					cout<<"\nCoTangent";
					calc = 1/tan((PI/180)*angle);
					send(new_socket, &calc, sizeof(calc), 0);
					break;		
				case 5:
					cout<<"\nCosecant";
					calc = 1/sin((PI/180)*angle);
					send(new_socket, &calc, sizeof(calc), 0);
					break;
				case 6:
					cout<<"\nSecant";
					calc = 1/cos((PI/180)*angle);
					send(new_socket, &calc, sizeof(calc), 0);
					break;
			}
		}
	}
	close(new_socket);
	return 0; 
} 
