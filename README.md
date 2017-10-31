# What is `MIPCL-PY`

`MIPCL-PY` is a Python module designed for rapid development of `MIPCL`-applications. Its functionality is very similar to that of `MIPshell`.

Not everybody, who applies optimization in practice, knows `C++`. `Python` is easy for beginners, and therefore we believe that MIPCL-PY can be useful for writing application prototypes.

`MIPCL-PY` comprises:

* shared MIPCL-library mipcl.so (mipcl.pyd on windows computers) with an additional interface for calling it in Python programs;
* module mipshell.py with a collection of Python classes that represent variables, constraints, and optimization problems.

Currently, `MIPCL-PY` implements only a part of functions available in MIPshell. In particular, `MIPCL-PY` does not allow us to develop applications that generate cuts because it is not efficient to implement such applications in script programming languages.

*Important Notes*
* Under Win64: it currently only works with `Python 2.7` and` 3.5`
* Under Linux: Please change `<MIPCL path>/mipcl_py/mipshell/mipcl-py*.so` to match your version

Author: Nicolai N. Pisaruk

http://www.mipcl-cpp.appspot.com/static/docs/mipcl-py/html/intro.html
