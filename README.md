# Solucionador de Sistemas de Ecuaciones Lineales

Este proyecto implementa diferentes métodos para resolver sistemas de ecuaciones lineales y está estructurado de la siguiente manera:


## Gauss eliminacion

Este módulo contiene la implementación del método de eliminación gaussiana para resolver sistemas de ecuaciones lineales.

### Función

### `gauss_elimination(A, b)`

Resuelve el sistema de ecuaciones lineales Ax = b utilizando eliminación gaussiana.

- **Argumentos**:
  - `A (np.ndarray)`: Matriz de coeficientes.
  - `b (np.ndarray)`: Vector de términos independientes.

- **Retorna**:
  - `np.ndarray`: Vector de soluciones x.

## LU Factorizacion

Este módulo contiene la implementación del método de factorización LU para resolver sistemas de ecuaciones lineales.

### Funciones

### `lu_factorization(A)`

Factoriza la matriz A en L y U tal que A = LU.

- **Argumentos**:
  - `A (np.ndarray)`: Matriz de coeficientes.

- **Retorna**:
  - `L (np.ndarray)`: Matriz triangular inferior.
  - `U (np.ndarray)`: Matriz triangular superior.

### `lu_solve(L, U, b)`

Resuelve el sistema de ecuaciones LUx = b usando la factorización LU.

- **Argumentos**:
  - `L (np.ndarray)`: Matriz triangular inferior.
  - `U (np.ndarray)`: Matriz triangular superior.
  - `b (np.ndarray)`: Vector de términos independientes.

- **Retorna**:
  - `np.ndarray`: Vector de soluciones x.

## Iterative Methods

Este módulo contiene la implementación de métodos iterativos para resolver sistemas de ecuaciones lineales.

### Función

### `gauss_seidel(A, b, tol=1e-10, max_iterations=1000)`

Resuelve el sistema de ecuaciones Ax = b usando el método iterativo de Gauss-Seidel.

- **Argumentos**:
  - `A (np.ndarray)`: Matriz de coeficientes.
  - `b (np.ndarray)`: Vector de términos independientes.
  - `tol (float)`: Tolerancia para la convergencia.
  - `max_iterations (int)`: Número máximo de iteraciones.

- **Retorna**:
  - `np.ndarray`: Vector de soluciones x.

## Main

Este módulo contiene la función principal del proyecto, la cual muestra ejemplos de uso de los diferentes métodos para resolver sistemas de ecuaciones lineales.

### Uso

El archivo `main.py` importa las funciones de los otros módulos y resuelve un ejemplo de sistema de ecuaciones utilizando los métodos de eliminación gaussiana, factorización LU y Gauss-Seidel.

### Ejemplo de ejecución

Para ejecutar el archivo y ver los resultados:

``bash
python main.py

## Test gauss

Este módulo contiene pruebas unitarias para el método de eliminación gaussiana.

### Clase

### `TestGaussElimination`

Prueba la función `gauss_elimination`.

- **Métodos**:
  - `test_gauss_elimination`: Verifica que la solución de un sistema de ecuaciones utilizando eliminación gaussiana es correcta.


## Test LU

Este módulo contiene pruebas unitarias para el método de factorización LU.

### Clase

### `TestLUFactorization`

Prueba las funciones `lu_factorization` y `lu_solve`.

- **Métodos**:
  - `test_lu_factorization`: Verifica que la solución de un sistema de ecuaciones utilizando factorización LU es correcta.

## Test Iterative

Este módulo contiene pruebas unitarias para el método iterativo de Gauss-Seidel.

### Clase

### `TestIterativeMethods`

Prueba la función `gauss_seidel`.

- **Métodos**:
  - `test_gauss_seidel`: Verifica que la solución de un sistema de ecuaciones utilizando Gauss-Seidel es correcta.


## Requisitos

- Python 3.x
- NumPy

## Instrucciones

1. Clona el repositorio.
2. Instala las dependencias.
3. Ejecuta el archivo `main.py` para ver ejemplos de uso.
4. Ejecuta los tests para verificar la correcta implementación de los métodos.

## Métodos Implementados

- **Eliminación Gaussiana**: Resuelve sistemas de ecuaciones lineales usando eliminación gaussiana.
- **Factorización LU**: Factoriza una matriz

# Resumen de Álgebra Lineal

El álgebra lineal es una rama de las matemáticas que estudia los vectores, las matrices y las transformaciones lineales. Es fundamental en muchas áreas de las matemáticas y la ciencia aplicada, incluyendo la ingeniería, la física, la economía y la informática.

## Conceptos Clave

### Vectores y Espacios Vectoriales

Un vector es un objeto que tiene magnitud y dirección. En el contexto del álgebra lineal, los vectores se representan como elementos de un espacio vectorial, que es un conjunto de vectores que pueden sumarse entre sí y multiplicarse por escalares (números).

### Matrices

Una matriz es una tabla rectangular de números dispuestos en filas y columnas. Las matrices se utilizan para representar sistemas de ecuaciones lineales, transformaciones lineales y muchas otras aplicaciones. Las operaciones básicas con matrices incluyen la suma, la multiplicación y la transposición.

### Sistemas de Ecuaciones Lineales

Un sistema de ecuaciones lineales es un conjunto de ecuaciones lineales que se resuelven simultáneamente. Estos sistemas pueden representarse en forma matricial como Ax = b, donde A es una matriz de coeficientes, x es un vector de incógnitas y b es un vector de términos independientes.

### Transformaciones Lineales

Una transformación lineal es una función que toma un vector como entrada y produce otro vector como salida, preservando la operación de suma y multiplicación por escalares. Las transformaciones lineales se pueden representar mediante matrices.

### Determinantes y Valores Propios

El determinante es un escalar que se puede calcular a partir de una matriz cuadrada y proporciona información sobre las propiedades de la matriz, como si es invertible. Los valores propios y los vectores propios son conceptos que describen cómo las transformaciones lineales cambian los vectores.

## Aplicaciones

El álgebra lineal tiene numerosas aplicaciones prácticas, tales como:

- **Resolución de sistemas de ecuaciones lineales**: Encontrar soluciones para sistemas de ecuaciones en ingeniería y ciencias.
- **Gráficos por computadora**: Manipulación de imágenes y animaciones.
- **Análisis de datos**: Métodos de regresión y reducción de dimensionalidad.
- **Mecánica cuántica**: Descripción de estados y operadores cuánticos.
- **Economía**: Modelos de equilibrio y optimización.

Este resumen cubre los conceptos básicos del álgebra lineal que son esenciales para comprender y utilizar los métodos implementados en este proyecto.
