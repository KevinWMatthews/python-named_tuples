# Named Tuples

Short syntax examples of named tuples in Python 3.

Syntax varies between Python 3.5, 3.6, and 3.7.


## `collections`

Named tuples are defined in Python's [`collections` module](https://docs.python.org/3/library/collections.html#collections.namedtuple).

Available in Python 3 and up.


## `typing`

Named tuples can be created with typing using Python's [`typing` module](https://docs.python.org/3/library/typing.html#typing.NamedTuple).

Available in Python 3.6 and up.


## `dataclass`

A typed class can be created using Python's [`dataclass` module](https://docs.python.org/3/library/dataclasses.html#module-dataclasses).

Available in Python 3.7 and up.


## Containers

Docker containers allow multiple versions of Python to be run on the same machine. Find official Python images on [Docker Hub](https://hub.docker.com/_/python).

One approach is to bind mount the current directory to the container:

```bash
$ docker run --rm -it -w /usr/src --mount type=bind,src=$PWD,dst=/usr/src IMAGE_NAME bash
```

This runs an interactive shell in the container and allows you to run all scripts in the current directory.

Alternatively, run an individual script once:

```bash
$ docker run --rm -w /usr/src --mount type=bind,src=$PWD/SCRIPT_NAME,dst=/usr/src/example.py IMAGE_NAME python example.py
```
