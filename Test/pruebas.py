# tests/test_solvers.py
import unittest
import numpy as np
from solvers.gaussian_elimination import gaussian_elimination
from solvers.lu_decomposition import lu_decomposition
from solvers.iterative_methods import jacobi_method, gauss_seidel_method

class TestSolvers(unittest.TestCase):
    def setUp(self):
        self.A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
        self.b = np.array([1, -2, 0])

    def test_gaussian_elimination(self):
        solution = gaussian_elimination(self.A, self.b)
        np.testing.assert_almost_equal(solution, [1, -2, -2])

    def test_lu_decomposition(self):
        solution = lu_decomposition(self.A, self.b)
        np.testing.assert_almost_equal(solution, [1, -2, -2])

    def test_jacobi_method(self):
        solution = jacobi_method(self.A, self.b)
        np.testing.assert_almost_equal(solution, [1, -2, -2], decimal=5)

    def test_gauss_seidel_method(self):
        solution = gauss_seidel_method(self.A, self.b)
        np.testing.assert_almost_equal(solution, [1, -2, -2], decimal=5)

if __name__ == "__main__":
    unittest.main()
