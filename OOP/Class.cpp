#include <iostream>
using namespace std;

// very basic class, just to show how Encapsulation works and how you can use functions inside classes
class Vehicle
{

	public:
		double velocity, acceleration, mass;
		int posX;
		

		// encapsulation example
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


	// Using new
	Vehicle* boat = new Vehicle;
	delete boat;


	return 0;
	

}