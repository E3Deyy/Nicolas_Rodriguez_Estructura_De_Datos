class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        self.raiz = self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, dato)
        return nodo

    def in_orden(self):
        self._in_orden_recursivo(self.raiz)
        print()

    def _in_orden_recursivo(self, nodo):
        if nodo:
            self._in_orden_recursivo(nodo.izquierda)
            print(nodo.dato, end=" ")
            self._in_orden_recursivo(nodo.derecha)

    def pre_orden(self):
        self._pre_orden_recursivo(self.raiz)
        print()

    def _pre_orden_recursivo(self, nodo):
        if nodo:
            print(nodo.dato, end=" ")
            self._pre_orden_recursivo(nodo.izquierda)
            self._pre_orden_recursivo(nodo.derecha)

    def post_orden(self):
        self._post_orden_recursivo(self.raiz)
        print()

    def _post_orden_recursivo(self, nodo):
        if nodo:
            self._post_orden_recursivo(nodo.izquierda)
            self._post_orden_recursivo(nodo.derecha)
            print(nodo.dato, end=" ")

# Menu de opciones
def menu():
    arbol = ArbolBinario()

    while True:
        print("\nMenú Árbol Binario Ordenado")
        print("1. Insertar dato")
        print("2. Imprimir en in orden")
        print("3. Imprimir en Post orden")
        print("4. Imprimir en Pre orden")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                valor = int(input("Ingrese un numero entero: "))
                arbol.insertar(valor)
            except ValueError:
                print("Por favor, ingrese un número valido.")
        elif opcion == "2":
            print("Recorrido In Orden:")
            arbol.in_orden()
        elif opcion == "3":
            print("Recorrido Post Orden:")
            arbol.post_orden()
        elif opcion == "4":
            print("Recorrido Pre Orden:")
            arbol.pre_orden()
        elif opcion == "5":
            print("Saliendo.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

#Ejecutar
if __name__ == "__main__":
    menu()
