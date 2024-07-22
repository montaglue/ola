import sys
sys.path.append('../common')

from input import stubborn_input

def calculate_number_of_ways(n: int, memoization: list[int]) -> int:
    if n < 0:
        return 0
    if len(memoization) > n:
        return memoization[n]
    if n == 0:
        memoization.append(1)
    else:
        memoization.append(calculate_number_of_ways(n - 1, memoization) + calculate_number_of_ways(n - 2, memoization))
    return memoization[n]

def main():
    n = stubborn_input('Enter the number of steps: ')
    print(calculate_number_of_ways(n, []))

if __name__ == '__main__':
    main()