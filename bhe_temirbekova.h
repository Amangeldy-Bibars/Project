/*
15.01.2021
library for binary homomorphic encryption
author Temirbekova Zhanerke
*/

#include <bits/stdc++.h>

int gcd(int a, int h)
{
    int temp;
    while (1)
    {
        temp = a % h;
        if (temp == 0)
            return h;
        a = h;
        h = temp;
    }
}

double esepteu_n(double p, double q)
{
	return p * q;	
}

double esepteu_phi(double p, double q)
{
	return (p - 1) * (q - 1);	
}

double esepteu_e(double e, double phi)
{
	 while (e < phi)
    {

        if (gcd(e, phi) == 1)
            break;
        else
            e++;
    }
    
	return e;	
}

double esepteu_d(double k, double phi, double e)
{
	return (1 + (k * phi)) / e;	
}

double esepteu_c(double msg, double e, double n)
{
	double c = pow(msg, e);
    c = fmod(c, n);
    
	return c;	
}

double esepteu_m(double c, double d, double n)
{
	double m = pow(c, d);
    m = fmod(m, n);
    
	return c;	
}
