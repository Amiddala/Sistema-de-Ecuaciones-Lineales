#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

// Función para imprimir una matriz
void printMatrix(const vector<vector<double>>& matrix) {
    for (const auto& row : matrix) {
        for (double val : row) {
            cout << setw(10) << setprecision(5) << val << " ";
        }
        cout << endl;
    }
    cout << endl;
}

// Función para realizar el algoritmo de Gauss-Jordan
vector<vector<double>> gaussJordan(vector<vector<double>> matrix) {
    int n = matrix.size();

    // Augmentar la matriz con la matriz identidad
    for (int i = 0; i < n; ++i) {
        matrix[i].resize(2 * n);
        matrix[i][n + i] = 1.0;
    }

    for (int i = 0; i < n; ++i) {
        // Encontrar el pivote
        double pivot = matrix[i][i];
        if (pivot == 0) {
            for (int j = i + 1; j < n; ++j) {
                if (matrix[j][i] != 0) {
                    swap(matrix[i], matrix[j]);
                    pivot = matrix[i][i];
                    break;
                }
            }
        }

        // Hacer pivote 1
        for (int j = 0; j < 2 * n; ++j) {
            matrix[i][j] /= pivot;
        }

        // Hacer ceros en las otras filas
        for (int j = 0; j < n; ++j) {
            if (i != j) {
                double factor = matrix[j][i];
                for (int k = 0; k < 2 * n; ++k) {
                    matrix[j][k] -= factor * matrix[i][k];
                }
            }
        }
    }

    // Extraer la matriz inversa
    vector<vector<double>> inverse(n, vector<double>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            inverse[i][j] = matrix[i][n + j];
        }
    }

    return inverse;
}

int main() {
    int n;

    // Leer el tamaño de la matriz
    cout << "Ingrese el tamaño de la matriz: ";
    cin >> n;

    vector<vector<double>> matrix(n, vector<double>(n));

    // Leer la matriz
    cout << "Ingrese los elementos de la matriz:" << endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    cout << "Matriz original:" << endl;
    printMatrix(matrix);

    vector<vector<double>> inverse = gaussJordan(matrix);

    cout << "Matriz inversa:" << endl;
    printMatrix(inverse);

    return 0;
}