#include <iostream>
#include <vector>

// Función para calcular la determinante de una matriz
int determinante(std::vector<std::vector<int>>& matriz, int n) {
    if (n == 1)
        return matriz[0][0];

    int det = 0;
    std::vector<std::vector<int>> subMatriz(n, std::vector<int>(n));  // Submatriz temporal

    int signo = 1;
    for (int i = 0; i < n; i++) {
        int subFila = 0;
        for (int fila = 1; fila < n; fila++) {
            int subCol = 0;
            for (int col = 0; col < n; col++) {
                if (col == i)
                    continue;
                subMatriz[subFila][subCol] = matriz[fila][col];
                subCol++;
            }
            subFila++;
        }
        det += signo * matriz[0][i] * determinante(subMatriz, n - 1);
        signo = -signo;
    }
    return det;
}

int main() {
    int n;
    std::cout << "Ingrese el tamaño de la matriz (n x n): ";
    std::cin >> n;

    std::vector<std::vector<int>> matriz(n, std::vector<int>(n));

    std::cout << "Ingrese los elementos de la matriz:" << std::endl;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> matriz[i][j];
        }
    }

    int resultado = determinante(matriz, n);
    std::cout << "La determinante de la matriz es: " << resultado << std::endl;

    return 0;
}
