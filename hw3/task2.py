import sys
sys.path.append('../common')

from input import read_json, write_json


def main():
    input_file_name = 'input.txt'
    output_file_name = 'output.txt'

    stores = read_json(input_file_name).unwrap_exit()


    result = {}

    for store_name in stores:
        for product_name in stores[store_name]:
            if product_name not in result:
                result[product_name] = 0
            result[product_name] += stores[store_name][product_name]
    write_json(output_file_name, result).unwrap_exit()

if __name__ == '__main__':
    main()