#include <stdio.h>
#include <stdlib.h>

int fib( unsigned int n){ 
    if (n <= 1) return n; 
    else return fib(n-1) +fib(n-2); 
}

int main(int argc, char** argv){ 

    unsigned int m = atoi(argv[1]);
    for (int i = 0;i < m; i++){ 
        printf("%i : %i \n",i, fib(i));
    }
}