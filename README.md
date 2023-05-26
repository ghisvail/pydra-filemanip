# pydra-filemanip

----

Pydra tasks for file manipulation.

[Pydra][pydra] is a dataflow engine which provides
a set of lightweight abstractions for DAG
construction, manipulation, and distributed execution.

This project provides a selection of Pydra tasks
for common file manipulations such as reading, writing and (de)compressing.

## Installation

```console
pip install pydra-filemanip
```

## Development

This project is managed with [Hatch][hatch]:

```console
pipx install hatch
```

To run the test suite:

```console
hatch run test
```

To fix linting issues:

```console
hatch run lint:fix
```

## License

This project is distributed under the terms of the [Apache License, Version 2.0][license].

[hatch]: https://hatch.pypa.io/

[license]: https://spdx.org/licenses/Apache-2.0.html

[pydra]: https://pydra.readthedocs.io/
