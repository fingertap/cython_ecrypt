# Cython Encryption for Distributing Python Source Code

In this package, we show how to encrypt the Python source code for distribution. The workflow is:

1. compile all needed files to `so` file on Mac/Linux, or `pyd` file on Windows.
2. distribute the compiled `lib` directory.

**_NOTE: _** `Cython` does not support relative imports, so you should always use absolute imports in your package. See `cython_encrypt/enc_local_import.py` for example.

**_NOTE: _** `Cython` does not keep the structure of modules (no need for `__init__.py`). To import the module, treat the module as a bunch of files located in a same directory.

We include these frequently used packages:

- `Numpy`
- `Pandas`
- `PyTorch`
- Custom class

We also include the following patterns for encryption

- bash script (in `bin/`)
- submodules


Have fun coding!
