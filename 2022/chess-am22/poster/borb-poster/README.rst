Borb poster for CHESS AM 2022
=============================

Installation
------------

With `Graphviz <https://www.graphviz.org/>`__ and
`ImageMagick <https://imagemagick.org/script/index.php>`__ installed,
the python project is installed with

.. code:: sh

   poetry install

from the project root directory. To compile the pdf, activate the python
environment and run ``make-poster``:

.. code:: sh

   poetry shell  # or equivalent with your preferred virtualenv program
   make-poster

The pdf can then be found in the project root directory, named
``poster.pdf``.

Dependencies
------------

In addition to the dependencies specified in ``pyproject.toml``, you
need `Graphviz <https://www.graphviz.org/>`__ and
`ImageMagick <https://imagemagick.org/script/index.php>`__ installed. On
ubuntu you can do

.. code:: sh

   sudo apt install graphviz

For other distributions, find install instructions on their websites.
