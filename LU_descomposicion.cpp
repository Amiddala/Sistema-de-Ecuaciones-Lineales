#include <iostream>
#include <vector>

using namespace std;

// Función para imprimir una matriz
void printMatrix(const vector<vector<double>>& mat) {
    int n = mat.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << mat[i][j] << "\t";
        }
        cout << endl;
    }
}

// Función para realizar la descomposición LU
void decomposeLU(const vector<vector<double>>& A, vector<vector<double>>& L, vector<vector<double>>& U) {
    int n = A.size();

    // Inicializar L como una matriz identidad y U como una copia de A
    L = vector<vector<double>>(n, vector<double>(n, 0.0));
    U = A;

    for (int i = 0; i < n; ++i) {
        L[i][i] = 1.0; // Los elementos diagonales de L son 1

        // Calcular los elementos de L y U
        for (int k = i + 1; k < n; ++k) {
            L[k][i] = U[k][i] / U[i][i];
            for (int j = i; j < n; ++j) {
                U[k][j] -= L[k][i] * U[i][j];
            }
        }
    }
}

int main() {
    int n;
    cout << "Ingrese el tamaño de la matriz cuadrada (n): ";
    cin >> n;

    vector<vector<double>> A(n, vector<double>(n));

    // Ingreso de la matriz A
    cout << "Ingrese los elementos de la matriz A (" << n << "x" << n << "):" << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> A[i][j];
        }
    }

    vector<vector<double>> L, U;

    // Realizar la descomposición LU
    decomposeLU(A, L, U);

    // Mostrar L y U
    cout << "Matriz L:" << endl;
    printMatrix(L);

    cout << "Matriz U:" << endl;
    printMatrix(U);

    return 0;
}
