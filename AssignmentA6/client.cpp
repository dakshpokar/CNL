// Client side C/C++ program to demonstrate Socket programming 
#include <stdio.h> 
#include <iostream>
#include <sys/socket.h> 
#include <stdlib.h> 
#include <netinet/in.h> 
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h> 
#define PORT 8082 
using namespace std;
int main(int argc, char const *argv[]) 
{ 
	struct sockaddr_in address; 
	int sock = 0, valread; 
	struct sockaddr_in serv_addr; 
	char *hello = "hello"; 
	char buffer[1024] = {0}; 
	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
	{ 
	printf("\n Socket creation error \n"); 
	return -1; 
	} 

	memset(&serv_addr, '0', sizeof(serv_addr)); 

	serv_addr.sin_family = AF_INET; 
	serv_addr.sin_port = htons(PORT); 

	// Convert IPv4 and IPv6 addresses from text to binary form 
	if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0)  
	{ 
	printf("\nInvalid address/ Address not supported \n"); 
	return -1; 
	} 

	if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) 
	{ 
	printf("\nConnection Failed \n"); 
	return -1; 
	} 
	//send(sock , hello , strlen(hello) , 0 ); 
	//printf("Hello message sent\n"); 
	//valread = read( sock , buffer, 1024); 
	//printf("%s\n",buffer ); 
	int choice, intchoice, omch;
	double angle, calc;
	char *ch, *fileName;
	choice = 1;
	
		cout<<"\nChoose from the following";
		cout<<"\n1. Send Hello message";
		cout<<"\n2. Transfer a file";
		cout<<"\n3. Trignometric Ratios";
		cout<<"\nEnter your choice: ";
		cin>>choice;
		switch(choice){
			case 1:
				cout<<"\nHello Message Window";
				send(sock, hello, strlen(hello), 0);
				printf("\nSent Hello Message");
				valread = read( sock , buffer, 1024); 
				cout<<"\n"<<buffer;
				break;
			case 2:
				cout<<"\nFile Transfer Window";
				omch = 1;
				while(omch!=0){
					ch = "file";
					send(sock, ch, strlen(ch), 0);
					valread = read(sock, buffer, 1024);
					if(strcmp(buffer,"file") == 0){
						omch = 0;
						cout<<"\nConnected for File Transfer";
						cout<<"\nEnter the name of file to be transferred: ";
						cin>>fileName;
					}
					else{
						cout<<"\nThere are some errors in connecting with client";
						cout<<"\nDo you want to reconnect[1/0]: ";
						cin>>omch;
					}
				}
				break;
			case 3:
				cout<<"\nTrignometric Ratios Calculator Window";
				omch = 1;
				while(omch!=0){
					ch = "trig";
					send(sock, ch, strlen(ch), 0);
					valread = read(sock, buffer, 1024);
					if(strcmp(buffer,"trig") == 0){
						omch = 0;
						cout<<"\nConnected for Trignometric Ratios Calculation";
						cout<<"\nSelect which ratio you want to calculate";
						cout<<"\n1. Sine";
						cout<<"\n2. Cosine";
						cout<<"\n3. Tangent";
						cout<<"\n4. CoTangent";
						cout<<"\n5. Cosecant";
						cout<<"\n6. Secant";
						cout<<"\nEnter your choice: ";
						cin>>intchoice;
						send(sock, &intchoice, sizeof(intchoice), 0);
						cout<<"\nEnter the Angle: ";
						cin>>angle;
						send(sock, &angle, sizeof(angle), 0);
						valread = read(sock, &calc, sizeof(calc));
						cout<<"\n"<<calc;
					}
					else{
						cout<<"\nThere are some errors in connecting with client";
						cout<<"\nDo you want to reconnect[1/0]: ";
						cin>>omch;
					}
				}
			
				break;
			
		}
	ch = "exit";
	send(sock, ch, strlen(ch), 0);
	close(sock);
	return 0; 
} 
