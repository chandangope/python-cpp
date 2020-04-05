#include "mylib.h"
#include <math.h>

int isPrime(int n)
{
	for (int i=2; i<=sqrt(n); i++)
	{
		if(n%i == 0)
			return 0;
	}
	return 1;
}


int getPrimes(int* ints, int numInts, int* outInts)
{
    for(int i=0; i<numInts; i++)
    {
    	outInts[i] = isPrime(ints[i]);
    }

    return 0;

}
