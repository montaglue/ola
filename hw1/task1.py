import sys
sys.path.append('../common')


from input import stubborn_input


def main():
    n = stubborn_input('Enter a number: ')
    for i in range(n):
        padding = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(padding + stars)

if __name__ == '__main__':
    main()