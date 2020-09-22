import sys 
def fib(n):
    if type(n) is not int or n< 0:
        raise TypeError(f"{n} is not a positive integer")
    elif n <=1:
        return n
    else: 
        return fib(n-1) +fib(n-2)

def main():
    m = int(sys.argv[1])
    for i in range(m):
        print(f"{i} : {fib(i)}")

if __name__ == '__main__':
   main()
