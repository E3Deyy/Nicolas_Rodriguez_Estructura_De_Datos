# Aplicación gráfica con proceso y eliminación

import tkinter as tk
from tkinter import messagebox

# Clase Nodo
class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None

# Lista circular nueva
class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.trazabilidad = []

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        self.trazabilidad = []
        self.trazabilidad.append(f"Insertando cliente: {cedula} - {nombre}")

        if self.inicio is None:
            self.inicio = nuevo
            nuevo.siguiente = nuevo
            self.trazabilidad.append("Lista vacía. Se enlaza el nuevo nodo a sí mismo.")
        else:
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.inicio
            self.trazabilidad.append(f"Nuevo nodo insertado al final. El nodo con cédula {actual.cedula} ahora apunta al nuevo nodo.")
        self.inicio = nuevo
        self.trazabilidad.append(f"'Inicio' ahora apunta al nuevo nodo con cédula {self.inicio.cedula}.")

    def listar_derecha(self):
        clientes = []
        self.trazabilidad = []
        if self.inicio is None:
            self.trazabilidad.append("La lista está vacía.")
            return clientes, self.trazabilidad
        actual = self.inicio
        self.trazabilidad.append("Iniciando recorrido desde 'Inicio'.")
        while True:
            clientes.append((actual.cedula, actual.nombre))
            self.trazabilidad.append(f"Visitando nodo: {actual.cedula} - {actual.nombre}")
            actual = actual.siguiente
            if actual == self.inicio:
                self.trazabilidad.append("Se ha llegado nuevamente a 'Inicio'. Fin del recorrido.")
                break
        return clientes, self.trazabilidad

    def eliminar_cliente(self, cedula):
        self.trazabilidad = []
        if self.inicio is None:
            self.trazabilidad.append("La lista está vacía. No se puede eliminar.")
            return False

        actual = self.inicio
        anterior = None
        encontrado = False

        self.trazabilidad.append(f"Buscando cliente con cédula {cedula} para eliminar.")

        while True:
            if actual.cedula == cedula:
                encontrado = True
                break
            anterior = actual
            actual = actual.siguiente
            if actual == self.inicio:
                break

        if not encontrado:
            self.trazabilidad.append("Cliente no encontrado.")
            return False

        if actual == self.inicio and actual.siguiente == self.inicio:
            self.trazabilidad.append("Eliminando único nodo en la lista.")
            self.inicio = None
        elif actual == self.inicio:
            self.trazabilidad.append("Eliminando nodo en 'Inicio'.")
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            temp.siguiente = self.inicio.siguiente
            self.inicio = self.inicio.siguiente
        else:
            self.trazabilidad.append(f"Eliminando nodo con cédula {cedula}.")
            anterior.siguiente = actual.siguiente

        return True

# Interfaz grafica
class AppClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista Circular de Clientes")

        self.lista = ListaCircular()

        tk.Label(root, text="Cédula:").pack()
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.pack()

        tk.Label(root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Button(root, text="Insertar Cliente", command=self.insertar_cliente).pack(pady=5)
        tk.Button(root, text="Eliminar Cliente", command=self.eliminar_cliente).pack(pady=5)
        tk.Button(root, text="Listar Clientes Derecha", command=self.listar_clientes).pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

        self.texto_resultado = tk.Text(root, width=60, height=20)
        self.texto_resultado.pack(pady=10)

    def insertar_cliente(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()

        if not cedula or not nombre:
            messagebox.showerror("Error", "Debe llenar todos los campos")
            return

        self.lista.insertar_cliente(cedula, nombre)
        self.mostrar_trazabilidad("Cliente insertado correctamente")

    def eliminar_cliente(self):
        cedula = self.entry_cedula.get()

        if not cedula:
            messagebox.showerror("Error", "Debe ingresar una cédula para eliminar")
            return

        eliminado = self.lista.eliminar_cliente(cedula)
        if eliminado:
            self.mostrar_trazabilidad("Cliente eliminado correctamente")
        else:
            self.mostrar_trazabilidad("No se pudo eliminar el cliente")

    def listar_clientes(self):
        clientes, trazabilidad = self.lista.listar_derecha()
        self.texto_resultado.delete("1.0", tk.END)
        if not clientes:
            self.texto_resultado.insert(tk.END, "La lista está vacía\n")
        else:
            self.texto_resultado.insert(tk.END, "Lista de clientes hacia la derecha:\n")
            for cedula, nombre in clientes:
                self.texto_resultado.insert(tk.END, f"{cedula} - {nombre}\n")
        self.texto_resultado.insert(tk.END, "\n--- Trazabilidad ---\n")
        for paso in trazabilidad:
            self.texto_resultado.insert(tk.END, paso + "\n")

    def mostrar_trazabilidad(self, mensaje):
        self.texto_resultado.delete("1.0", tk.END)
        self.texto_resultado.insert(tk.END, mensaje + "\n\n--- Trazabilidad ---\n")
        for paso in self.lista.trazabilidad:
            self.texto_resultado.insert(tk.END, paso + "\n")

#Ejecuto app
if __name__ == '__main__':
    root = tk.Tk()
    app = AppClientes(root)
    root.mainloop()
