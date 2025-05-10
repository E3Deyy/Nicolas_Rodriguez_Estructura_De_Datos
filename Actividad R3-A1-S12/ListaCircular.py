# Lista Circular
class ListaCircularClientes:
    def __init__(self):
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = NodoCliente(cedula, nombre)
        if self.inicio is None:
            self.inicio = nuevo
            nuevo.siguiente = nuevo  # Apunta a sí mismo
        else:
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.inicio
            self.inicio = nuevo  # Se actualiza inicio al nuevo nodo

    def listar_clientes(self):
        clientes = []
        if self.inicio is None:
            return clientes
        actual = self.inicio
        while True:
            clientes.append(f"Cédula: {actual.cedula}, Nombre: {actual.nombre}")
            actual = actual.siguiente
            if actual == self.inicio:
                break
        return clientes
