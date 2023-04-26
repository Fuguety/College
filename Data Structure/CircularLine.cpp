#include <iostream>
#include <vector>
using namespace std;

struct Line
{
    public:
    virtual void inqeue(int x) = 0; // adds element to end of list
    virtual int fromqueue() = 0;   // takes out first element and prints it
    virtual bool isEmpty() = 0;     // check if list is empty
    virtual void reset() = 0;   // resets the list
};

class LineVector
{
    private:
        int n;
        int ini;
        int size;
        int vect[5];
        int vect1[3] = { 11, 22, 33 };
        int newVect[8];

    public:        


        void setN() { n = 0; }
        int getN() { return n; }

        void setIni() { ini = 0; }
        int getIni() { return ini; }

        // gets size of array
        void setSize() { size = end(vect) - begin(vect); }
        int getSize() { return size; }

        // inserts x to end of array, if array is full, it cannot be added
        void inqueue(int v)
        {    
            setSize();
            if ( n < size){
                vect[n + 1] = v;
                n = n + 1;
            }
            
            else
                cout << "List is already full, cannot add element";
            
        }

        // check if array is empty
        bool isEmpty()
        {
            if ( n == 0 )
                return true;
            else
                return false;
        }

        // resets list
        void reset()
        {
            n = 0;
            ini = 0;
        }

        // takes out and returns first element of array
        int fromqueue()
        {   
            if ( isEmpty() )
            {
                cout << "List is empty";
                return 0;
            }
            else
            {
                int element = vect[ini];
                ini = ini + 1;
                n = n - 1;
                return element;
            }
        }

        // prints array
        void toString()
        {
            if (isEmpty())
                cout << "List is empty";
            else{
                for (int i = 0; i < n; i++)
                    cout << vect[i];
            }
        }


        void merge()
        {
            if ( isEmpty() )
                cout << "List is empty, please add new elements";
            else
            {
                for (int i; ini <= size; i++ )
                {
                    newVect[i] = vect[ini];
                    newVect[i + 1] = vect1[ini + 1];
                };
            }
            
        }

        void concatena()
        {
            if ( isEmpty() )
                cout << "List is empty, please add new elements";
            else
            {
                int x = 1;
                for (int i; ini < size; i++ )
                {
                    newVect[i] = vect[ini];
                    x = x + 1;
                };
                for ( int first; first < 3; first++)
                {
                    newVect[x] = vect1[first];
                };
            }
            
        }


};

int main()
{
    // Starts list and resets everything
    LineVector lin;
    lin.setSize();
    lin.setIni();
    lin.setN();
    lin.reset();

    // uncommment next line

    // cout << function() you want

    return 0;

}
