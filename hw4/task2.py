import sys
sys.path.append('../common')

from input import stubborn_input

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    a = stubborn_input('Enter the first number: ')
    b = stubborn_input('Enter the second number: ')
    print(gcd(abs(a), abs(b)))

if __name__ == '__main__':
    main()