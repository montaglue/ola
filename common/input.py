from errors import Result, Ok, Err


def read_file(filename: str) -> Result[str, str]:
    try:
        with open(filename, 'r') as file:
            return Ok(file.readlines())
    except BaseException:
        return Err(f'Error reading the file {filename}')

def read_strings(filename: str) -> Result[list[str], str]:
    try:
        with open(filename, 'r') as file:
            return Ok(file.readlines())
    except BaseException:
        return Err(f'Error reading the file {filename}')

def write_file(filename: str, content: str) -> Result[None, str]:
    try:
        with open(filename, 'w') as file:
            file.write(content)
            return Ok(None)
    except BaseException:
        return Err(f'Error writing the file {filename}')
    
def write_strings(filename: str, content: list[str]) -> Result[None, str]:
    try:
        with open(filename, 'w') as file:
            file.writelines(content)
            return Ok(None)
    except BaseException:
        return Err(f'Error writing the file {filename}')

def stubborn_input(message: str = '') -> int:
    '''
    This function reads an integer from the user input.
    The ignoring of signal interruptions is intended behavior.
    '''
    result = 0
    has_input = False
    while not has_input:
        try:
            result = int(input(message))
        except:
            continue
        has_input = True
    return result


def read_json(filename: str) -> Result[dict, str]:
    try:
        import json
        with open(filename, 'r') as file:
            return Ok(json.load(file))
    except BaseException:
        return Err(f'Error reading the file {filename}')
    
def write_json(filename: str, content: dict) -> Result[None, str]:
    try:
        import json
        with open(filename, 'w') as file:
            json.dump(content, file)
            return Ok(None)
    except BaseException:
        return Err(f'Error writing the file {filename}')