import numpy as np

def lu_factorization(A):
    """
    Factoriza la matriz A en L y U tal que A = LU.
    
    Args:
        A (np.ndarray): Matriz de coeficientes.

    Returns:
        L (np.ndarray): Matriz triangular inferior.
        U (np.ndarray): Matriz triangular superior.
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    return L, U

def lu_solve(L, U, b):
    """
    Resuelve el sistema de ecuaciones LUx = b usando la factorización LU.
    
    Args:
        L (np.ndarray): Matriz triangular inferior.
        U (np.ndarray): Matriz triangular superior.
        b (np.ndarray): Vector de términos independientes.

    Returns:
        np.ndarray: Vector de soluciones x.
    """
    n = b.size
    y = np.zeros(n)
    x = np.zeros(n)
    
    # Solución de Ly = b
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    
    # Solución de Ux = y
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    
    return x
