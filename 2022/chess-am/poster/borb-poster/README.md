# Borb poster for CHESS AM 2022

## Installation

With [Graphviz] and [ImageMagick] installed, the python project is installed with

```sh
poetry install
```

from the project root directory. To compile the pdf, activate the python environment and
run `make-poster`:

```sh
poetry shell  # or equivalent with your preferred virtualenv program
make-poster
```

The pdf can then be found in the project root directory, named `poster.pdf`.

## Dependencies

In addition to the dependencies specified in `pyproject.toml`, you need [Graphviz] and
[ImageMagick] installed. On ubuntu you can do

```sh
sudo apt install graphviz
```

For other distributions, find install instructions on their websites.

[graphviz]: https://www.graphviz.org/
[imagemagick]: https://imagemagick.org/script/index.php
