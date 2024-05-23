import numpy as np

def gauss_elimination(A, b):
    """
    Resuelve el sistema de ecuaciones Ax = b usando el método de eliminación gaussiana.
    
    Args:
        A (np.ndarray): Matriz de coeficientes.
        b (np.ndarray): Vector de términos independientes.

    Returns:
        np.ndarray: Vector de soluciones x.
    """
    n = len(b)
    # Convertir A y b a matrices flotantes para evitar problemas de precisión
    A = A.astype(float)
    b = b.astype(float)

    # Eliminación hacia adelante
    for i in range(n):
        # Encontrar el máximo en la columna i
        max_row = np.argmax(np.abs(A[i:, i])) + i
        # Intercambiar filas
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Hacer ceros debajo del pivote
        for k in range(i + 1, n):
            factor = A[k, i] / A[i, i]
            A[k, i:] -= factor * A[i, i:]
            b[k] -= factor * b[i]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x
