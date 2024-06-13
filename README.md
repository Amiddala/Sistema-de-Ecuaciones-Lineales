# Proyecto de Álgebra Lineal

Este proyecto contiene tres implementaciones clave de algoritmos de álgebra lineal:

1. **Cálculo de la Determinante por el Método de Cofactores**
2. **Inversa de una Matriz usando el Método de Gauss-Jordan**
3. **Descomposición LU de una Matriz**

## Descripción

Este proyecto está diseñado para realizar cálculos esenciales en álgebra lineal utilizando el lenguaje de programación C++. Cada funcionalidad se implementa en un archivo separado para una mejor organización y facilidad de uso.

### 1. Cálculo de la Determinante por el Método de Cofactores

Este programa calcula la determinante de una matriz cuadrada utilizando el método de cofactores. El usuario ingresa el tamaño de la matriz y sus elementos, y el programa devuelve la determinante de la matriz.

### 2. Inversa de una Matriz usando el Método de Gauss-Jordan

Este programa encuentra la inversa de una matriz cuadrada mediante el método de eliminación de Gauss-Jordan. El usuario ingresa la matriz y, si es invertible, el programa devuelve su inversa.

### 3. Descomposición LU de una Matriz

Este programa descompone una matriz cuadrada en dos matrices, L (inferior) y U (superior), tales que `A = L * U`. La descomposición LU es útil para resolver sistemas de ecuaciones lineales y calcular determinantes y matrices inversas.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `determinante_cof.cpp`: Código para calcular la determinante por el método de cofactores.
- `gauss_jordan.cpp`: Código para calcular la inversa de una matriz usando Gauss-Jordan.
- `LU_descomposicion.cpp`: Código para realizar la descomposición LU de una matriz.
- `README.md`: Este archivo, que proporciona una descripción del proyecto y cómo utilizar los programas.

## Cómo Utilizar

### Requisitos

- Un compilador de C++, como `g++`.

### Compilación y Ejecución

Para compilar y ejecutar cada programa, siga estos pasos:

1. **Cálculo de la Determinante por el Método de Cofactores**:

   g++ -o determinante_cof determinante_cof.cpp
   ./determinante_cof

2. **Inversa de una Matriz usando el Método de Gauss-Jordan**:
g++ -o inversa_gauss_jordan inversa_gauss_jordan.cpp
./inversa_gauss_jordan
3. **Descomposición LU de una Matriz**:
g++ -o descomposicion_lu descomposicion_lu.cpp
./descomposicion_lu
## Uso
### Cálculo de la Determinante por el Método de Cofactores
El programa solicitará el tamaño de la matriz (n x n).
Luego, solicitará los elementos de la matriz.
Finalmente, mostrará la determinante de la matriz.
### Inversa de una Matriz usando el Método de Gauss-Jordan
El programa solicitará el tamaño de la matriz (n x n).
Luego, solicitará los elementos de la matriz.
Si la matriz es invertible, mostrará la matriz inversa; de lo contrario, indicará que la matriz no es invertible.
### Descomposición LU de una Matriz
El programa solicitará el tamaño de la matriz (n x n).
Luego, solicitará los elementos de la matriz.
Mostrará las matrices L y U resultantes de la descomposición LU.
## Contribución
Las contribuciones son bienvenidas. Por favor, abra un issue o envíe un pull request para mejoras o correcciones.