import sys

from input import stubborn_input
sys.path.append('../common')

def repetative_sum_of_digits(n: int) -> int:
    if n == 0:
        return 0
    rem = abs(n) % 9
    return rem if rem != 0 else 9


def main():
    n = stubborn_input('Enter a number: ')
    sum_of_digits = repetative_sum_of_digits(n)
    print(sum_of_digits)

if __name__ == '__main__':
    main()