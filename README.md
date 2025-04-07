# estructura-de-datos
Instrucciones 

Realizar una investigación sobre tipos de datos abstractos y su uso sobre listas dinámicas simples.
Realizar una aplicación usando estructuras lineales simples
Se debe evidenciar el proceso de creación desde la programación orientada a objetos
Crear un programa usando el lenguaje de programación JAVA aplicando conceptos de listas simples.

Crear un menú de opciones con a siguiente estructura:
Insertar cliente: Esta opción permite pedir la cedula y nombre del cliente a ser insertado sobre la lista simple. Esta inserción se deberá realizar de forma ordenada
Listar Clientes hacia la derecha: Esta opción permitirá imprimir los n clientes que han sido cargados sobre la lista doble desde el primer nodo hasta el último nodo
Salir: Esta opción permite finalizar la aplicación

Solución

Investigación: Tipos de datos abstractos y listas dinámicas simples

Tipo de dato abstracto: es un modelo matemático para estructuras con datos. Este describe que operaciones se pueden hacer y que comportamiento se espera, sin preocuparse por cómo están implementadas.

Ejemplo de tipos de datos abstractos comunes: Pilas, colas, listas, árboles y grafos.

Lista enlazada simple o dinámica simple

Es una colección lineal de nodos donde cada nodo apunta al siguiente.

Ventajas:

Inserciones y eliminaciones eficientes.

Crecimiento dinámico que nos ayuda al desperdicio de memoria.

Ideal para estructuras como agendas, catálogos, listas de tareas, entre otros.

Algunas cosas que implementé en el código son: 

Un uso de clases para organizar la información.

Inserción de datos usando CompareTo, esto lo apliqué en el método "insertar" de la clase "Lista simple" para que se organice mejor.

también un "Scanner" para leer dato desde la consola ypara el control del menú, usé el ciclo "while"y agregué un contador para que se vea cuando incrementan los clientes.