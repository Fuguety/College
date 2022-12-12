#include <iostream>
using namespace std;

// very basic class, just to show how Encapsulation works and how you can use functions inside classes
class Vehicle
{

	public:
		double velocity, acceleration, mass;
		int posX;
		

		// encapsulation
		int changePosition() 
		{
			posX = posX + velocity;
			return posX;
		}

		// function inside class (changes the velocity)
		double accelerate(double vel, double acce){
			for(int i = 0; i < 10; i++) // accelerates for 10 seconds
				vel = vel + acce;
			return vel;
		}

		// static function to create a static variable
		static int driver(){
			static int driver = 1;
			return driver;
		}

};


// Default Constructor
class Default
{
	public:
		int a, b;
	
		Default()
		{
			a = 100;
			b = 200;
		}

};


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



	//Declaring variable for vehicle class and using polymorphism 
	Vehicle car;
	car.velocity = 1;
	car.acceleration = 1;
	//Accelerate the car
	car.velocity = car.accelerate(car.velocity, car.acceleration);


	Vehicle plane;
	plane.velocity = 10;
	plane.acceleration = 15;
	//Accelerate the car
	plane.velocity = plane.accelerate(plane.velocity, plane.acceleration);


	// Default class
	Default def();


	// Private class
	Priv p(20, 50); // x = 20 and y = 50


	// Destroy class
	Destroy d();


	//Copy class
	Copy c1(100, 500); //Use first construct
	Copy c2 = c1;	//Use copy construct


	// Inheritance class
	Child cc;
	cc.age_dad = 100;
	cc.age_child = 50;


	while(true);


	return 0;
	

}
