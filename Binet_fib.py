import sys 
from math import sqrt

def fib(n):
    phi =  (1+ sqrt(5))/2
    psi =  (1- sqrt(5))/2
    F_n = (phi**n - psi**n)/sqrt(5)
    return int(F_n)

def main():
    n = int(sys.argv[1])
    print(f"{n} : {fib(n)}")

if __name__ == '__main__':
   main()
