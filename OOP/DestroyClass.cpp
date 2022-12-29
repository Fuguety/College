#include <iostream>
using namespace std;



// Very simple example of destructor
class Destroy
{
	private:
	 int * variable;
	
	public:
		Destroy(int *variable);
		~Destroy(){delete[] variable;};
};

//Define the function
Destroy::Destroy(int *variable)
{
	*variable = 10;
}




int main()
{

    // Destroy class
    Destroy d();


    return 0;
}