import sys
sys.path.append('../common')

from errors import Result, Ok, Err
from input import read_file, write_file


def parse_input(strings: list[str]) -> Result[list[tuple[str, int]], str]:
    fun = lambda splited_string: (splited_string[0], int(splited_string[1]))
    try:
        return Ok([fun(string.split(',')) for string in strings])
    except BaseException:
        return Err('Error parsing input')

def serialize_students(students: list[tuple[str, int]]) -> list[str]:
    return [f'{student[0]},{student[1]}\n' for student in students]


def main():
    input_file_name = 'input.txt'
    output_file_name = 'output.txt'

    students = parse_input(read_file(input_file_name).unwrap_exit()).unwrap_exit()

    avarage = sum([student[1] for student in students]) / len(students)
    students = [student for student in students if student[1] > avarage]

    write_file(output_file_name, serialize_students(students))



if __name__ == '__main__':
    main()
