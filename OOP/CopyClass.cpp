#include <iostream>
using namespace std;



// Copy Class (Build a class uusing old parameters from same class)
class Copy
{

	private:
	 int copyX, copyY;

	public:

		// Construct 1
		Copy(int parameter1, int parameter2)
		{
			copyX = parameter1;
			copyY = parameter2;
		}


		// Construct using old Class parameters
		Copy(const Copy& c1)
		{
			copyX = c1.copyX;
			copyY = c1.copyY;
		}

	    int getCopyX() { return copyX; }
    	int getCopyY() { return copyY; }

};





int main()
{

    	//Copy class
	Copy c1(100, 500); //Use first construct
	Copy c2 = c1;	//Use copy construct


    return 0;
}