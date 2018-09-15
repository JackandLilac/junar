#include<iostream>
using namespace std;
int main(){
    cout << "begin" << endl;
    int a;
	int *b;
    int c[3] = {1,2,3};
	int (* d)[3];
    int e[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
	int (* f)[3];
	d = &c;
	f = e;
	int array[5] = {1, 2, 3, 4, 5};
	b = array;
	int *g = array;
	int (*h)[3] = e;
	int *i = new int[5];
	delete[] i;
	int *j = new int(6);
	delete j;
	int **k = new int *[3];
	for(int i=0; i<3; i++) {
	    k[i] = new int[5];
	}
	for(int i=0; i<3; i++){
		delete[] k[i];
	}
	cout << sizeof(a) << endl;
	cout << sizeof(b) << endl;
	cout << sizeof(c) << endl;
	cout << sizeof(d) << endl;
	cout << "==============================" << endl;
	for (int i=0; i<3; i++){
	    cout << c[i] << endl;
	}
	for (int i=0; i<3; i++){
	    cout << d[i] << endl;
	}
	cout << "==============================" << endl;
	for (int i=0; i<3; i++){
	    for(int j=0; j<3; j++){
	        cout << d[i][j] << endl;
		}
	}
	cout << "==============================" << endl;
	d = new int[3][3];
	for (int i=0; i<3; i++){
	    for(int j=0; j<3; j++){
		    d[i][j] = i*j;
		}
	}
    for (int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            cout << d[i][j] << endl;
        }
    }
	cout << "==============================" << endl;
	delete[] d;
	int* p_int;
	double *p_double;
	int (*p_func)(int, int);
	int ** p_pointer;
	p_int = new int(3);
	cout << p_int << endl;
	cout << *p_int << endl;
	cout << "==============================" << endl;
    p_pointer = &p_int;
	cout << **p_pointer << endl;
	cout << *p_pointer << endl;
	delete[] p_int;
	cout << "==============================" << endl;
    int *p2;
	p2 = c;
	for(int i=0; i<3; i++){
	    cout << p2[i] << endl;
	}
	cout << "==============================" << endl;
	int *p3;
	p3 = *p_pointer;
	cout << *p3 << endl;
	cout << p3 << endl;
	cout << "==============================" << endl;
	int ***p4;
	p4 = &p_pointer;
	cout << p4 << endl;
	cout << *p4 << endl;
	cout << **p4 << endl;
	cout << ***p4 << endl;
	cout << "==============================" << endl;
	cout << "end" << endl;
}
