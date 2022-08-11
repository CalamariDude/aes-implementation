
from aes_encryption import *

zero = long_to_bytes(0)
one = long_to_bytes(1)
ff = long_to_bytes(255)
def test_square_up():
    assert len(square_up('AA')) == 1
    assert len(square_up('AAAAAAAAAAAAAAAA')) == 1
    assert len(square_up('AAAAAAAAAAAAAAAABB')) == 2

def test_shift_bytes_in_square():
    square =[[zero, zero, zero, zero], [zero, zero, zero, zero], [ff, ff, zero, zero], [zero, zero, zero, zero]]
    expected_output = [[one, one, one, one], [one, one, one, one], [zero, zero, one, one], [one, one, one, one]]
    output = shift_bytes_in_square(square)
    for i in range(len(output)):
        for j in range(len(output[i])):
            assert expected_output[i][j] == output[i][j]



test_square_up()
test_shift_bytes_in_square()
print('tests passed')