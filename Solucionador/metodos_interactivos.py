import numpy as np

def gauss_seidel(A, b, tol=1e-10, max_iterations=1000):
    """
    Resuelve el sistema de ecuaciones Ax = b usando el método iterativo de Gauss-Seidel.
    
    Args:
        A (np.ndarray): Matriz de coeficientes.
        b (np.ndarray): Vector de términos independientes.
        tol (float): Tolerancia para la convergencia.
        max_iterations (int): Número máximo de iteraciones.

    Returns:
        np.ndarray: Vector de soluciones x.
    """
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    
    for k in range(max_iterations):
        x_old = x.copy()
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x[i] = (b[i] - sigma) / A[i, i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    
    return x
