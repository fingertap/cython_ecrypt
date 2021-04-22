from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize([
        'cython_encrypt/*.py',
        'cython_encrypt/enc_module/*.py',
        'bin/enc_script.py'
    ])
)