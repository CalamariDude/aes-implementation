from Crypto import *
from Crypto.Util.number import long_to_bytes
from math import ceil


plaintext = 'hello'
key = '11'

####### start of logic - do not touch

#precomputed shifter
shift_amount = int(key[0])
mapping = {}#todo
for i in range(256):
    mapping[long_to_bytes(i)] = long_to_bytes((i+shift_amount)%16)
print(len(mapping.items()), "))))")
for k, v in mapping.items():
    print(k,v)

undo_mapping = {(v, k) for k,v in mapping.items()}
print(undo_mapping)
print(len(undo_mapping))

row_shift_amount = int(key[1])
zero = long_to_bytes(0)
def byte_recategorize(byte_boi):
    return mapping[byte_boi]

#def byte_decatorize(byte_boi):


def shift_bytes_in_square(square):
    for i in range(len(square)):
        for j in range(len(square[0])):
            square[i][j] = mapping[square[i][j]]
    return square

def square_up(data):
    bytes_data = data.encode('ascii')
    n_matrices = ceil(len(bytes_data)/16)
    squares = [[[zero, zero, zero, zero] for _ in range(4)] for _ in range(n_matrices) ]#0x0is default_padding
    return squares

def row_shift(squares):
    shifted_squares = []
    for i in range(len(squares)):
        shifted_squares.append((squares[i]+row_shift_amount)%len(squares))
    return shifted_squares


