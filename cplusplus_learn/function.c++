#include<iostream>
using namespace std;
int f() { return 42;}
int main() {
	int n=1;
	int *pn = &n;
	int &r = *pn;
	int m = *pn;
	cout << r << endl;
	cout << m << endl;
	int (*fp)() = &f;
	int (&fr)() = *fp;
	cout << fr() << endl;
	cout << fp() << endl;
}
