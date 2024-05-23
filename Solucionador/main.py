import numpy as np
from gauss_elimination import gauss_elimination
from lu_factorization import lu_factorization, lu_solve
from iterative_methods import gauss_seidel

def main():
    # Ejemplo de sistema de ecuaciones
    A = np.array([[3, 2, -4], [2, 3, 3], [5, -3, 1]], dtype=float)
    b = np.array([3, 15, 14], dtype=float)
    
    # Solución con eliminación gaussiana
    x_gauss = gauss_elimination(A, b)
    print("Solución con eliminación gaussiana:", x_gauss)
    
    # Solución con factorización LU
    L, U = lu_factorization(A)
    x_lu = lu_solve(L, U, b)
    print("Solución con factorización LU:", x_lu)
    
    # Solución con Gauss-Seidel
    x_gs = gauss_seidel(A, b)
    print("Solución con Gauss-Seidel:", x_gs)

if __name__ == "__main__":
    main()
