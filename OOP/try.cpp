#include <iostream>
using namespace std;

int main()
{

	int x = 10;
	
	// tentar fazer o if
	try{
		if(x < 9)		
			cout << x << endl;


		// caso o if não for, encerrar o try e informar o erro
		else
			throw 1;
	}


	// catch equivalente ao "except", usa os (...) pra não especificar o número do erro
	// caso queira informar o erro é so botar (int erro) para informar o número do erro
	catch(...){
		cout << "erro!" << endl;
	}

	while(true);

	return 0;

}
