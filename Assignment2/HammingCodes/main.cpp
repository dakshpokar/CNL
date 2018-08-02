#include<iostream>
#include<vector>
#include<math.h>
using namespace std;
class HammingCodes
{
private:
	char a;
	int m;
	int r;
	vector<bool> rbitSet;
	vector<bool> bitSet;
	vector<bool> :: iterator i;
	bool redundancy;
public:
	HammingCodes(){
		a = 'n';
		m = 0;
		r = 0;
		for(int i = 0; i<8;i++){
			rbitSet.push_back(0);
		}
		redundancy = false;
	}
	void getInput(){
		cout<<"\nEnter a character to transfer: ";
		cin>>a;
		convertInput();
	}
	void convertInput(){
		int x = (int)a;
		int bit;
		while(x!=0)
		{
			if((int)x % 2 == 1){
				bit = 1;
			}
			else{
				bit = 0;
			}
			cout<<bit;
			x = x / 2;
			rbitSet.push_back(bit);
		}
		if(rbitSet.size() < 8){
			rbitSet.push_back(0);
		}
		cout<<"\nEntered BitSet is: ";


		for(i = rbitSet.end() - 1; i!=rbitSet.begin(); i--){
			bitSet.push_back(*i);
		}
		bitSet.push_back(*rbitSet.begin());
		m = bitSet.size();

		display();
		cout<<"\nCardinality of BitSet: ";
		cout<<m;
	}
	void oboInput(){
		cout<<"\nEnter the bits one by one --";
		int bit;

		for(int j = 7; j>=0;j--){
			cout<<"\nEnter bit "<<j<<": ";
			cin>>bit;
			rbitSet[j] = bit;
		}
		/*if(rbitSet.size() < 8){
			rbitSet.push_back(0);
		}*/
		bitSet = rbitSet;
		cout<<"\nEntered BitSet is: ";
		m = bitSet.size();

		display();
	}
	void redundantBits()
	{
		for(r = 0; r<10; r++){
			if(pow(2, r) >= m + r + 1){
				break;
			}
		}
		cout<<"\nNumber of Redundant Bits: "<<r;
		addRedundantBits();
	}
	void addRedundantBits(){
		int i = pow(2,0);
		while(i<=m){
			bitSet.insert(bitSet.begin() + i - 1, 0);
			i = 2 *i;
		}
		cout<<endl;
		m = bitSet.size();
		int k = 1;
		for(int i = 0;i<r;i++){
			k = pow(2,i);
			bool parity = 0;
			for(int j = 1;j<=12;j++){
				if((j&k) == k){
					parity = parity ^ (bitSet[j-1]);
				}
			}
			bitSet[k-1] = parity;
			cout<<"P"<<k<<" = "<<parity;
			cout<<endl;
		}
		redundancy = true;
		display();
	}
	void display(){
		cout<<endl;
		for(int j = bitSet.size(); j>0;j--){
			if((log(j)/log(2) == int(log(j)/log(2))) && redundancy == true){
				cout<<"P"<<j<<"\t";
			}
			else{
			cout<<"D"<<j<<"\t";
			}
		}
		cout<<endl;
		for(i = bitSet.end() - 1; i!=bitSet.begin(); i--){
			cout<<*i<<"\t";
		}
		cout<<*bitSet.begin();
	}

};
int main()
{
	HammingCodes hammingCodes;
	hammingCodes.oboInput();
	hammingCodes.redundantBits();
}

