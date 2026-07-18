Examples coming soon...
# Examples

This directory contains Jupyter notebooks demonstrating how to use the
`circuitfp` package.

The notebooks are intended as tutorials that reproduce key results from the
paper while illustrating the Python API.

## Available notebooks

### BCS_overlap.ipynb

Introduction to the `Overlap` class. This notebook demonstrates how to

- compute the overlap between two BCS states,
- visualize the overlap as a function of phase difference,
- generate an overlap matrix,
- reproduce the Gaussian approximation of the BCS overlap presented in the paper.

## Running the examples

Install the package first:

```bash
pip install -e .
```

or

```bash
pip install circuitfp
```

Then launch Jupyter:

```bash
jupyter lab
```

or

```bash
jupyter notebook
```

and open one of the notebooks in this directory.