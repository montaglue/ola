import sys
sys.path.append('../common')

from input import stubborn_input, read_strings, write_strings
from errors import Result, Ok, Err

def parse_cities(strings: list[str]) -> Result[list[tuple[str, int]], str]:
    fun = lambda splited_string: (splited_string[0], int(splited_string[1]))
    try:
        return Ok([fun(string.split(':')) for string in strings])
    except BaseException:
        return Err('Error parsing input')

def serialize_cities(cities: list[tuple[str, int]]) -> list[str]:
    return [f'{city[0]}:{city[1]}\n' for city in cities]

def main():
    input_file_name = 'cities.txt'
    output_file_name = 'filtered_cities.txt'
    file = parse_cities(read_strings(input_file_name).unwrap_exit()).unwrap_exit()

    threashold = stubborn_input('Enter the threashold citizens: ')

    cities = serialize_cities([city for city in file if city[1] >= threashold])

    write_strings(output_file_name, cities).unwrap_exit()



if __name__ == '__main__':
    main()