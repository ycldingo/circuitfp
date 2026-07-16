# circuitfp
This is the official repository for the publication ["Circuit quantization from first principles", _Phys. Rev. Research_ **7**, 033144 (2025)](https://journals.aps.org/prresearch/abstract/10.1103/dfrq-44vk).

[![GitHub Release](https://shields.io)](https://github.com)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

---

## Overview

circuitfp provides numerical tools for constructing low-energy Hilbert space directly from microscopic BCS theory.

This project is based on 
> Yun-Chih Liao, Benjamin J. Powell & Thomas M. Stace
> ["Circuit quantization from first principles", _Phys. Rev. Research_ **7**, 033144 (2025)](https://journals.aps.org/prresearch/abstract/10.1103/dfrq-44vk)

### Current features
- Overlap of BCS phase states
- Overlap matrix in phase representation
- Unit tests

### Future versions will include
- Fourier transform between phase and number space
- Phase operator
- Number operator
- Hamiltonian projection
- and more...

### Repository structure
```
circuitfp/

├── src/
│   └── circuitfp/
│       ├── overlap.py
│       ├── ...
│
├── tests/
│       ├── test_overlap.py
│       ├── ...
│
├── examples/
│       ├── ...
│
├── docs/
│       ├── ...
│
└── README.md
```


---

## Installation

Clone the repository
```bash
conda create -n circuitfp python=3
conda activate circuitfp
```

---

## Citation

If you use this package, please kindly cite

Y.-C. Liao, B. J. Powell, and T. M. Stace, Circuit quantization from first principles, Phys. Rev. Res. **7**, 033144 (2025)

---

## License

MIT License