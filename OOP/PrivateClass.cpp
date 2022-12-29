#include <iostream>
using namespace std;



// Class with private parameters
class Priv
{
	private:
		int x, y;
	
	public:
		//constructor
		Priv(int v1, int v2)
		{
			x = v1;
			y = v2;
		}

	//get values
	int getX(){ return x; }

	int getY(){ return y; }

};





int main()
{


	// Private class
	Priv p(20, 50); // x = 20 and y = 50

    return 0;
}