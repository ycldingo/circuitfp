# Overlap module

```
circuitfp.Overlap
```

The `Overlap` class evaluates the overlap bwteen two BCS phase states.


# Mathematical background

The overlap between two BCS phase states is given by
\[
\mathcal{W} (\phi_1,\phi_2)
\equiv
\langle \Psi(\phi_1) | \Psi(\phi_2)
=
\exp
\Big[
n
\big(
\frac{i}{2}\Delta\phi
-
\frac{\pi\Delta}{16B}
(\varphi)^2
\big)
Big],
\]

where \( \varphi = \phi_2 - \phi_1 \) is the phase difference.