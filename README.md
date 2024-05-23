# Solucionador de Sistemas de Ecuaciones Lineales

## Introducción

El objetivo de este proyecto es desarrollar una herramienta para resolver sistemas de ecuaciones lineales utilizando diferentes métodos. Los métodos implementados incluyen la eliminación gaussiana, la factorización LU y varios métodos iterativos. Este proyecto se ha estructurado cuidadosamente para asegurar que sea escalable, fácil de mantener y extensible para futuras mejoras.

## Metas

1. **Implementación del Solucionador de Sistemas de Ecuaciones Lineales:**
   - Desarrollar un programa que acepte sistemas de ecuaciones lineales y los resuelva utilizando métodos como la eliminación gaussiana, la factorización LU y métodos iterativos.
   - Crear funciones específicas para cada método de resolución.
   - Garantizar que el programa sea capaz de manejar sistemas de ecuaciones de cualquier tamaño y proporcione soluciones precisas.

2. **Uso de GitHub y Git para la Gestión del Proyecto:**
   - Crear un repositorio en GitHub para alojar el código fuente.
   - Utilizar Git para el control de versiones.
   - Facilitar la colaboración y el seguimiento del progreso del proyecto mediante las funciones de GitHub como issues y pull requests.

## Desarrollo del Proyecto

### Preparación del Entorno

1. **Configurar el entorno de desarrollo:**
   - Instalar Python.
   - Crear un entorno virtual para el proyecto.
   - Instalar las bibliotecas necesarias como NumPy y SciPy.

2. **Crear un repositorio en GitHub:**
   - Crear un nuevo repositorio en GitHub.
   - Clonar el repositorio en la máquina local.
   - Configurar Git en el proyecto local.

### Implementación del Solucionador de Sistemas de Ecuaciones Lineales

1. **Definir la estructura del proyecto:**
   - Crear un directorio para el proyecto.
   - Dentro del directorio, crear un archivo principal (`main.py`) y un directorio para las funciones de resolución (`solvers`).

2. **Implementación de los métodos de resolución:**
   - Implementar la eliminación gaussiana en un archivo llamado `gaussian_elimination.py`.
   - Implementar la factorización LU en un archivo llamado `lu_decomposition.py`.
   - Implementar los métodos iterativos (Jacobi, Gauss-Seidel) en un archivo llamado `iterative_methods.py`.

3. **Crear una función principal para aceptar y resolver sistemas de ecuaciones:**
   - En el archivo `main.py`, importar las funciones de resolución y proporcionar ejemplos de uso para cada método.

### Pruebas y Depuración

1. **Escribir pruebas unitarias para cada método:**
   - Crear un directorio `tests`.
   - Escribir pruebas para cada método de resolución utilizando un framework de pruebas como `unittest` o `pytest`.

2. **Ejecutar las pruebas y corregir errores:**
   - Ejecutar las pruebas unitarias y realizar depuración según sea necesario para asegurar que cada método funcione correctamente.

### Gestión de Versiones y Colaboración

1. **Uso de Git para control de versiones:**
   - Realizar commits regulares para documentar los cambios en el código.
   - Push de los cambios al repositorio remoto en GitHub.

2. **Colaboración en GitHub:**
   - Utilizar issues para gestionar tareas, errores y sugerencias de mejora.
   - Crear pull requests para revisar y fusionar cambios en el código.

3. **Documentación:**
   - Documentar cada función con docstrings.
   - Crear un archivo `README.md` con instrucciones de uso y detalles del proyecto.

### Conclusiones

Este proyecto ha resultado en la creación de una herramienta robusta para resolver sistemas de ecuaciones lineales utilizando múltiples métodos. A través de la implementación de una estructura de proyecto clara y el uso de Git y GitHub para la gestión de versiones y la colaboración, se ha asegurado que el proyecto sea fácil de mantener y extender en el futuro. Este enfoque garantiza una gestión eficiente del desarrollo del proyecto y facilita la colaboración y el mantenimiento a largo plazo.

## Métodos Implementados
- Eliminación Gaussiana
- Factorización LU
- Métodos Iterativos (Jacobi, Gauss-Seidel)

## Uso
Ejecute `main.py` para ver un ejemplo de uso:
```bash
python main.py
