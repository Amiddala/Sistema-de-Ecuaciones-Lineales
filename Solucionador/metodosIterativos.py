# solvers/iterative_methods.py
import numpy as np

def jacobi_method(A, b, tol=1e-10, max_iterations=1000):
    x = np.zeros_like(b)
    for _ in range(max_iterations):
        x_new = np.copy(x)
        for i in range(A.shape[0]):
            s = sum(A[i, j] * x[j] for j in range(A.shape[1]) if i != j)
            x_new[i] = (b[i] - s) / A[i, i]
        if np.allclose(x, x_new, atol=tol):
            break
        x = x_new
    return x

def gauss_seidel_method(A, b, tol=1e-10, max_iterations=1000):
    x = np.zeros_like(b)
    for _ in range(max_iterations):
        x_new = np.copy(x)
        for i in range(A.shape[0]):
            s1 = sum(A[i, j] * x_new[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, A.shape[1]))
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, atol=tol):
            break
        x = x_new
    return x

  
