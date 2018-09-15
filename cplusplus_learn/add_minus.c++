#include<iostream>
using namespace std;
int main(){
	int *a = new int[2];
	int c[5][2] = {{1,2},{3,4},{4,5},{5,6},{6,7}} ;
	int (* b)[2] = c;
	int *p;
	p = a;
	for(int i=0; i<2; i++){
		a[i] = i;
	}
	for(int i=0; i<2; i++) {
		cout<< a[i] <<endl;
	}
	cout << "len is : " << sizeof(a)/sizeof(a[0]) << endl;
	cout << *(a+1) << endl;
	cout << *a << endl;
	cout << "access : " << *(*(b+2)+1) << endl;
	cout << *(++p) << endl;
	delete[] a;
}
