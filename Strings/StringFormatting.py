"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to .
Each value should be space-padded to match the width of the binary value of  and the values should be
separated by a single space.
"""

def print_formatted(number):
    width = len(bin(number)[2:])
    ''' Space-padded to match the width of the binary value of number '''

    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        '''
           for => Number = 2,
           output of oct(i) => 0o1 ,0o2
           So use oct(i)[2:]
        '''

        hexa = hex(i)[2:].upper()
        '''
           output of hex(i) => 0x1  0x2  0x3  0x4  0x5  0x6  0x7  0x8  0x9  0xa  0xb  0xc  0xd  0xe
           So Similar to above use [2:] and since the requirement is All Caps, use upper()
        '''
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)