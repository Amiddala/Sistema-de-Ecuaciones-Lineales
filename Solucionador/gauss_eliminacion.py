# solvers/gaussian_elimination.py
import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    # Formar la matriz aumentada
    Ab = np.hstack([A, b.reshape(-1, 1)])
    for i in range(n):
        # Pivot
        for k in range(i, n):
            if Ab[k, i] != 0:
                Ab[[i, k]] = Ab[[k, i]]
                break
        # Eliminar
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j] = Ab[j] - factor * Ab[i]
    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    return x
