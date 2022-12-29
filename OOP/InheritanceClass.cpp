#include <iostream>
using namespace std;



// inheritance
class Dad
{
	public:
		int age_dad;
		virtual int random(int r){return r = 10;}; // virtual function lets you change the function
		virtual void print() = 0; //creates function to be defined on another class (pure virtual function)
};

class Child : public Dad
{
	public:
		const int *number; // const can be changed, but it is not recommended since it is mostly used as a permanent number
		
		int age_child;

		// + all the varibles inside class Dad
		int random(int mmm){return mmm = 20;}; // it overides the old function
		void print() {cout << "Virtual Function";}; // define the print function

};



int main()
{

    	// Inheritance class
	Child cc;
	cc.age_dad = 100;
	cc.age_child = 50;


    return 0;
}