import numpy as np


def test():
    a = np.arange(15).reshape(3, 5)
    b = np.arange(10).reshape(5, 2)
    c = a.dot(b)
    np.testing.assert_array_equal(
        c, np.array([[ 60,  70], [160, 195], [260, 320]])
    )
    return 'OK'
