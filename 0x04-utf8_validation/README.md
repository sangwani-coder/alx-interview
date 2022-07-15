# 0x04-utf8_validation
In this project I wrote a Python function that determines if a given data set represents a valid UTF-8 encoding.
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore only handle the least 8 significant bits of each integer.

## Example
- If given the input data = [65] output should be **True**
- If given input data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33] output should be **True**
- If given input data = [229, 65, 127, 256] output should be **False**