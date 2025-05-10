¿Qué es una Lista Circular?
Una lista circular es una estructura de datos lineal en la que el último nodo apunta al primer nodo, formando un ciclo. Puede ser simple (un solo enlace por nodo) o doblemente enlazada (dos enlaces por nodo).

-Características de las Listas Circulares Simples
Cada nodo contiene datos y una referencia al siguiente nodo.

- El último nodo no apunta a None, sino al primer nodo.
- Pueden recorrerse de forma cíclica sin llegar a un final nulo.
- Son útiles para sistemas que requieren rotación continua como turnos, ciclos de tareas o juegos.

- ventajas
Permiten recorrer la lista desde cualquier punto sin necesidad de volver al inicio manualmente.
Eficientes en implementación de colas circulares o sistemas donde los elementos deben rotar constantemente.
Ahorro de memoria en comparación con estructuras más complejas.

- Sus aplicaciones
Planificadores de procesos en sistemas operativos.
Sistemas de turnos (como en cajeros o centros de atención).
Juegos que requieren movimientos por turnos en forma cíclica.
Implementación de colas circulares en buffers o estructuras de red.
