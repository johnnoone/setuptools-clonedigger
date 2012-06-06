Setuptools clonedigger command
==============================

This package adds clonedigger command to setup.py.



Usage
-----

::

  python setup.py clonedigger


Differences with the standalone library
---------------------------------------

In order to not conflict with other setuptools commands, some options differ
from the original library.

* all options are prefixed by clonedigger-, so short options are disabled
* original `output` and `cpd-output` were replaced by a single `clonedigger-file`