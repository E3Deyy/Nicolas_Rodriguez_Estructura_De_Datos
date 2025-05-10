- __¿Qué es un método de ordenamiento?__

Un método de ordenamiento es un algoritmo utilizado para organizar un conjunto de datos (por ejemplo, una lista de números) en un orden específico, ya sea ascendente o descendente. Estos métodos son fundamentales en informática, ya que optimizan búsquedas, mejoran la legibilidad de la información y facilitan el análisis de datos.

-1. __Método Burbuja (Bubble Sort)__
Descripción:
- Compara elementos adyacentes y los intercambia si están en el orden incorrecto.
- Repite el proceso hasta que la lista esté ordenada.

Características:
- Fácil de implementar.
- Poco eficiente con listas grandes.

Complejidad:
- Tiempo: O(n²) en el peor y promedio de los casos.
- Espacio: O(1)

__Ejemplo Bubble Sort:__

Lista original: [5, 3, 8, 4]

Iteración 1: [3, 5, 4, 8]

Iteración 2: [3, 4, 5, 8] (ordenada)

-2. __Método Secuencial (Inserción)__
Descripción:
- Inserta cada elemento en su posición correcta respecto a los elementos anteriores.
- Ideal para listas pequeñas o parcialmente ordenadas.

Características:
- Más eficiente que Burbuja en algunos casos.
-Bueno para flujos de datos en tiempo real.

Complejidad:
- Tiempo: O(n²) en el peor caso.
- Espacio: O(1)

__Ejemplo inserción:__

Lista original: [5, 3, 8, 4]

Paso 1: [3, 5, 8, 4]

Paso 2: [3, 5, 8, 4]

Paso 3: [3, 4, 5, 8]


-3. __Quicksort__

Descripción:
- Divide y conquista: elige un pivote y divide la lista en menores, iguales y mayores.
-Aplica el mismo proceso recursivamente.

Características:
-Muy eficiente para grandes volúmenes de datos.
-Usado en librerías estándar de muchos lenguajes.

Complejidad:
- Tiempo: O(n log n) en promedio, O(n²) en el peor caso.
- Espacio: O(log n) por la recursividad.

__Ejemplo Quicksort:__

Lista: [5, 3, 8, 4]

Pivote = 4 → Menores: [3], Iguales: [4], Mayores: [5, 8]

Resultado: [3, 4, 5, 8]

