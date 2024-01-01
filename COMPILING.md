# Building kipy

To update the generated files, build the `python_protobuf` CMake target:

```sh
# From your KiCad build directory
$ make python_protobuf
```

To package the Python library for installation:

```sh
$ pip3 install poetry
$ poetry build
```

# Testing

The easiest way is to install the built module into whatever Python you are running:

```sh
$ pip3 install dist/kipy-<whatever>.whl
```

Then you can do something like

```sh
$ pip3 install pyqt6
$ python3 examples/tracks.py
```
