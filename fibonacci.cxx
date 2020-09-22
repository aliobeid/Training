#include <stdio.h>
#include <stdlib.h>

int fib( unsigned int n){ 
    if (n <= 1) return n; 
    else return fib(n-1) +fib(n-2); 
}

int main(int argc, char** argv){ 

    unsigned int n = atoi(argv[1]);

    printf("%i : %i \n",n, fib(n));
}