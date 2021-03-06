typeshed
========

|Build Status| |Chat at https://gitter.im/python/typing|

About
-----

Typeshed contains external type annotations for the Python standard
library and Python builtins, as well as third party packages.

This data can e.g. be used for static analysis, type checking or type
inference.

For information on how to use ``typeshed``, read below. Information for
contributors can be found in `CONTRIBUTING.md <CONTRIBUTING.md>`__.
**Please read it before submitting pull requests.**

Typeshed supports Python versions 2.7 and 3.3 and up.

Using
-----

If you're just using mypy (or pytype or PyCharm), as opposed to
developing it, you don't need to interact with the typeshed repo at all:
a copy of typeshed is bundled with mypy.

When you use a checked-out clone of the mypy repo, a copy of typeshed
should be included as a submodule, using

::

    $ git clone --recurse-submodules https://github.com/python/mypy.git

or

::

    $ git clone https://github.com/python/mypy.git
    $ cd mypy
    $ git submodule init
    $ git submodule update

and occasionally you will have to repeat the final command
(``git submodule update``) to pull in changes made in the upstream
typeshed repo.

PyCharm and pytype similarly include a copy of typeshed. The one in
pytype can be updated in the same way if you are working with the pytype
repo.

Format
------

Each Python module is represented by a ``.pyi`` "stub". This is a normal
Python file (i.e., it can be interpreted by Python 3), except all the
methods are empty. Python function annotations (`PEP
3107 <https://www.python.org/dev/peps/pep-3107/>`__) are used to
describe the types the function has.

See `PEP 484 <http://www.python.org/dev/peps/pep-0484/>`__ for the exact
syntax of the stub files.

Syntax example
--------------

The below is an excerpt from the types for the ``datetime`` module.

.. code:: python

    from typing import Union

    MAXYEAR = ...  # type: int
    MINYEAR = ...  # type: int

    class date(object):
        def __init__(self, year: int, month: int, day: int) -> None: ...
        @classmethod
        def fromtimestamp(cls, timestamp: Union[int, float]) -> date: ...
        @classmethod
        def fromordinal(cls, ordinal: int) -> date: ...
        @classmethod
        def today(self) -> date: ...
        def ctime(self) -> str: ...
        def weekday(self) -> int: ...

Directory structure
-------------------

stdlib
~~~~~~

This contains stubs for modules the Python standard library -- which
includes pure Python modules, dynamically loaded extension modules,
hard-linked extension modules, and the builtins.

third\_party
~~~~~~~~~~~~

Modules that are not shipped with Python but have a type description in
Python go into ``third_party``. Since these modules can behave
differently for different versions of Python, ``third_party`` has
version subdirectories, just like ``stdlib``.

NOTE: When you're contributing a new stub for a package that you did not
develop, please obtain consent of the package owner (this is specified
in `PEP
484 <https://www.python.org/dev/peps/pep-0484/#the-typeshed-repo>`__).
The best way to obtain consent is to file an issue in the third-party
package's tracker and include the link to a positive response in your PR
for typeshed.

For more information on directory structure and stub versioning, see
`the relevant section of
CONTRIBUTING.md <https://github.com/python/typeshed/blob/master/CONTRIBUTING.md#stub-versioning>`__.

Contributing
------------

Please read `CONTRIBUTING.md <CONTRIBUTING.md>`__ before submitting pull
requests. If you have questions related to contributing, drop by the
`typing Gitter <https://gitter.im/python/typing>`__.

Running the tests
-----------------

The tests are automatically run by Travis CI on every PR and push to the
repo. There are several sets of tests: ``tests/mypy_test.py`` runs tests
against `mypy <https://github.com/python/mypy/>`__, while
``tests/pytype_test.py`` runs tests against
`pytype <https://github.com/google/pytype/>`__.

Both sets of tests are shallow -- they verify that all stubs can be
imported but they don't check whether stubs match their implementation
(in the Python standard library or a third-party package). Also note
that each set of tests has a blacklist of modules that are not tested at
all. The blacklists also live in the tests directory.

In addition, you can run ``tests/mypy_selftest.py`` to run mypy's own
test suite using the typeshed code in your repo. This will sometimes
catch issues with incorrectly typed stubs, but is much slower than the
other tests.

To manually run the mypy tests, you need to have Python 3.5 or higher;
Python 3.6.1 or higher is recommended.

Run:

::

    $ python3.6 -m venv .venv3
    $ source .venv3/bin/activate
    (.venv3)$ pip3 install -r requirements-tests-py3.txt

This will install mypy (you need the latest master branch from GitHub),
typed-ast, and flake8. You can then run mypy tests and flake8 tests by
invoking:

::

    (.venv3)$ python3 tests/mypy_test.py
    ...
    (.venv3)$ python3 tests/mypy_selftest.py
    ...
    (.venv3)$ flake8
    ...

(Note that flake8 only works with Python 3.6 or higher.)

To run the pytype tests, you need a separate virtual environment with
Python 2.7. Run:

::

    $ virtualenv --python=python2.7 .venv2
    $ source .venv2/bin/activate
    (.venv2)$ pip install -r requirements-tests-py2.txt

This will install pytype from its GitHub repo. You can then run pytype
tests by running:

::

    (.venv2)$ python tests/pytype_test.py

For mypy, if you are in the typeshed repo that is submodule of the mypy
repo (so ``..`` refers to the mypy repo), there's a shortcut to run the
mypy tests that avoids installing mypy:

.. code:: bash

    $ PYTHONPATH=.. python3 tests/mypy_test.py

You can mypy tests to a single version by passing ``-p2`` or ``-p3.5``
e.g.

.. code:: bash

    $ PYTHONPATH=.. python3 tests/mypy_test.py -p3.5
    running mypy --python-version 3.5 --strict-optional # with 342 files

.. |Build Status| image:: https://travis-ci.org/python/typeshed.svg?branch=master
   :target: https://travis-ci.org/python/typeshed
.. |Chat at https://gitter.im/python/typing| image:: https://badges.gitter.im/python/typing.svg
   :target: https://gitter.im/python/typing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


