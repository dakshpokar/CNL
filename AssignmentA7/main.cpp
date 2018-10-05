#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
        int choice;
        int count;
	ifstream file ( "file.csv" ); 
	string value, sr_no,time,source,destination,info,proto,len;
	cout<<"\nSelect which protocol you want to search";
	cout<<"\n1. Ethernet";
        cout<<"\n2. IP";
        cout<<"\n3. TCP";
        cout<<"\n4. UDP";
        cout<<"\nEnter your choice: ";
        cin>>choice;
        string protocol;
        switch(choice){
        	case 1:
        		protocol = "ARP";
			break;
		case 2:
			protocol = "IP";
			break;
		case 3:
			protocol = "TCP";
			break;
		case 4:
			protocol = "UDP";
			break;
	}
	count = 0;
	while ( file.good() )
	{
		count+=1;
	     	getline(file,sr_no,','); 
		getline(file,time,',');
		getline(file,source,',');
		getline(file,destination,',');
		getline(file,proto,',');
		getline(file,len,',');
		getline(file,info,'\n');
		string s1 = string( proto, 1, proto.length()-2 );
		if(s1.find(protocol) != std::string::npos)	{
			cout << source <<"\t"<< destination <<"\t"<< proto<< "\t"<<len<<"\t"<<info<<endl; 
		}
	}
	cout<<"\nTotal number of packets: "<<count<<endl;
	return 0;
}
