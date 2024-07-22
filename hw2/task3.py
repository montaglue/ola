import sys
sys.path.append('../common')

from input import read_strings, write_strings


def canonize_strings(strings: list[str]) -> list[str]:
    if strings[-1][-1] != '\n':
        strings[-1] += '\n'
    return strings


def main():
    input_file1_name = 'input1.txt'
    input_file2_name = 'input2.txt'
    output_file_name = 'output.txt'
    
    file1 = canonize_strings(read_strings(input_file1_name).unwrap_exit())
    
    file2 = canonize_strings(read_strings(input_file2_name).unwrap_exit())

    output = sorted(file1 + file2)

    write_strings(output_file_name, output).unwrap_exit()

if __name__ == '__main__':
    main()
