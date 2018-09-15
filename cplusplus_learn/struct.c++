#include<iostream>
using namespace std;
struct test{
	string name;
	int count;
};
int main() {
	test a = {"zj", 4};
	test *b = &a;
	test *c = new test();
	c->name = "oys";
	c->count = 5;
	cout << b->name  << " " << (*b).count << endl;
	cout << c->name  << " " << (*c).count << endl;
}
