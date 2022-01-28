### A slide with a dark background

Try to press the down arrow key.

---

### Another slide

Try **Esc** and **F** keys.

- A bullet point
- Another convincing argument

---

### Code blocks are no problem

Here we have some Python code:

```python
from itertools import cycle

fizz = cycle(['', '', 'Fizz'])
buzz = cycle(['', '', '', '', 'Buzz'])

for i in range(1, 101):
    print((next(fizz) + next(buzz)) or i)

# Then do much more to make it long

__GENERATORS__ = {
    0: create.GenerateRandomNormal,
    1: create.GenerateFPP,
    2: create.GenerateSingleVolcano,
}


def create_volcanoes(
    size: int = 251, init_year: int = 1850, version: int = 0, option: int = 0
) -> None:
    """Create volcanoes starting at the year 1850.

    This will re-create the same data as can be found in forcing files used within the
    CESM2 general circulation model.

    Parameters
    ----------
    size: int
        The total number of eruptions
    init_year: int
        First year in the climate model
    version: int
        Choose one of the versions from the '__GENERATORS__' dictionary
    option: int
        Choose which option to use when generating forcing

    Raises
    ------
    IndexError
        If `version` is not a valid index of the generator dictionary.
    """
    # CREATE DATA ---------------------------------------------------------------------- #

    if version not in __GENERATORS__ or version < 0:
        raise IndexError(
            f"No version exists for index {version}. "
            + "It must be one of {__GENERATORS__.keys()}."
        )
    print(f"Generating with '{__GENERATORS__[version].__name__}'...")
    g = __GENERATORS__[version](size, init_year)
    g.generate()
    all_arrs = g.get_arrays()

    # CREATE NETCDF FILE AND SAVE ------------------------------------------------------ #

    frc_cls = create.ReWrite(*all_arrs) if option == 1 else create.Data(*all_arrs)
    frc_cls.make_dataset()
    frc_cls.save_to_file()


def main():
    create_volcanoes(size=300, init_year=1)


if __name__ == "__main__":
    main()
```

[Source](https://github.com/olemb/nonsense/blob/master/fizzbuzz/itertools_cycle.py)

---

### Images (1/2)

An image fetched from the web:

![Sample image](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/The_Young_Cicero_Reading.jpg/316px-The_Young_Cicero_Reading.jpg)
