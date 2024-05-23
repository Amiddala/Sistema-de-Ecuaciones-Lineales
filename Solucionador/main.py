# main.py
import numpy as np
from solvers.gaussian_elimination import gaussian_elimination
from solvers.lu_decomposition import lu_decomposition
from solvers.iterative_methods import jacobi_method, gauss_seidel_method

def main():
    A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    b = np.array([1, -2, 0])
    
    print("Solución por eliminación gaussiana:", gaussian_elimination(A, b))
    print("Solución por factorización LU:", lu_decomposition(A, b))
    print("Solución por método de Jacobi:", jacobi_method(A, b))
    print("Solución por método de Gauss-Seidel:", gauss_seidel_method(A, b))

if __name__ == "__main__":
    main()
