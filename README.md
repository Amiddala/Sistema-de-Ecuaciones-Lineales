# Solucionador de Sistemas de Ecuaciones Lineales

## Introducción

El álgebra lineal es una rama fundamental de las matemáticas con aplicaciones en numerosas disciplinas, incluyendo la ingeniería, la física, la economía y la informática. Entre las muchas herramientas y técnicas del álgebra lineal, la capacidad de resolver sistemas de ecuaciones lineales es particularmente importante. Este proyecto se centra en el desarrollo de un programa que puede resolver sistemas de ecuaciones lineales utilizando varios métodos avanzados.

## Objetivo del Proyecto

El objetivo principal de este proyecto es crear un solucionador de sistemas de ecuaciones lineales que sea:

- **Preciso**: Capaz de proporcionar soluciones exactas para sistemas de cualquier tamaño.
- **Flexible**: Implementar múltiples métodos de resolución para adaptarse a diferentes tipos de sistemas y condiciones.
- **Eficiente**: Utilizar algoritmos y bibliotecas optimizadas para garantizar un rendimiento rápido y eficiente.

## Metas del Proyecto

Para alcanzar este objetivo, hemos establecido las siguientes metas específicas:

### Implementación del Solucionador de Sistemas de Ecuaciones Lineales

1. **Desarrollo de Métodos de Resolución**:
   - **Eliminación Gaussiana**: Implementación de un algoritmo clásico para resolver sistemas de ecuaciones mediante la reducción de la matriz a una forma escalonada.
   - **Factorización LU**: Descomposición de la matriz en dos matrices triangulares (L y U) para simplificar la resolución del sistema.
   - **Métodos Iterativos**: Implementación de métodos como Jacobi y Gauss-Seidel, adecuados para sistemas grandes y dispersos.

2. **Funciones Específicas para Cada Método**:
   - Desarrollar funciones dedicadas para cada método de resolución, garantizando modularidad y claridad en el código.

3. **Manejo de Sistemas de Cualquier Tamaño**:
   - Asegurar que el programa pueda manejar sistemas de ecuaciones de cualquier tamaño, desde pequeños hasta muy grandes, utilizando estructuras de datos dinámicas y matrices de tamaño variable.

### Pruebas y Depuración

1. **Pruebas Exhaustivas**:
   - Realizar pruebas exhaustivas del solucionador utilizando sistemas de ecuaciones de diferentes tamaños y complejidades para asegurar la precisión y la fiabilidad de los resultados.

2. **Identificación y Corrección de Errores**:
   - Identificar y corregir cualquier error o comportamiento inesperado a través de un riguroso proceso de depuración y pruebas unitarias.

## Metodología

### Desarrollo del Solucionador

#### Eliminación Gaussiana

La eliminación gaussiana es un método clásico en el álgebra lineal para resolver sistemas de ecuaciones lineales. Este método involucra la transformación de la matriz del sistema a una forma triangular, de manera que se pueda resolver fácilmente mediante sustitución hacia atrás.

#### Factorización LU

La factorización LU es una técnica que descompone una matriz en el producto de una matriz triangular inferior (L) y una matriz triangular superior (U). Esta descomposición facilita la solución de sistemas de ecuaciones, así como el cálculo de determinantes y la inversión de matrices.

#### Métodos Iterativos

Los métodos iterativos, como Jacobi y Gauss-Seidel, son especialmente útiles para sistemas grandes y dispersos. Estos métodos proporcionan aproximaciones sucesivas a la solución, mejorando iterativamente hasta alcanzar un nivel de precisión deseado.

### Implementación Técnica

Para la implementación de estos métodos, se ha utilizado Python junto con bibliotecas de álgebra lineal como NumPy y SciPy. Estas bibliotecas ofrecen funciones optimizadas y eficientes para operaciones matriciales, lo que facilita la implementación y mejora el rendimiento del solucionador.

## Pruebas y Validación

### Pruebas Unitarias

Se han desarrollado pruebas unitarias para cada método de resolución, asegurando que cada función se comporte correctamente bajo una variedad de condiciones. Las pruebas unitarias se implementaron utilizando el framework `unittest` de Python.

### Pruebas de Integración

Además de las pruebas unitarias, se realizaron pruebas de integración para garantizar que todos los componentes del solucionador funcionen juntos de manera coherente y eficiente.

## Uso del Solucionador

### Ejecución del Programa

El programa principal (`main.py`) permite al usuario introducir un sistema de ecuaciones lineales y seleccionar el método de resolución deseado. A continuación se muestra un ejemplo de cómo ejecutar el programa:

### Métodos Disponibles

El programa incluye los siguientes métodos de resolución:

- **Eliminación Gaussiana**
- **Factorización LU**
- **Método de Jacobi**
- **Método de Gauss-Seidel**

Cada uno de estos métodos puede ser seleccionado y ejecutado desde la interfaz del programa, proporcionando una solución precisa al sistema de ecuaciones ingresado.

## Conclusiones

Este proyecto ha desarrollado un solucionador robusto y eficiente para sistemas de ecuaciones lineales, implementando varios métodos avanzados de resolución. A través del uso de Python y bibliotecas especializadas, hemos asegurado la precisión, flexibilidad y eficiencia del solucionador. El uso de GitHub y Git ha facilitado la gestión del proyecto, permitiendo una colaboración efectiva y un control de versiones detallado.

```bash
python main.py
