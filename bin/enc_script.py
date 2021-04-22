#!/usr/bin/env python

import cython_encrypt as ce
import cython_encrypt.enc_module as cem


if __name__ == '__main__':
    assert ce.enc_numpy.test() == 'OK'
    assert ce.enc_pandas.test() == 'OK'
    assert cem.enc_torch.test() == 'OK'
