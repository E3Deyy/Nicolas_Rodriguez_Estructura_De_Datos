import tkinter as tk
from tkinter import messagebox

class NodoCLiente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None

class ListaCircularCliente:
    def __init__(self):
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = NodoCliente(cedula, nombre)
        if self.inicio is None:
            self.inicio = nuevo
            nuevo.siguiente = nuevo #Esto apunta a sí mismo
        else:
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.inicio
            self.inicio = nuevo #Se actualiza inicio al nodo nuevo

def listar_clientes(self):
    cliente = []
    if self.inicio is None:
            return clientes
    actual = self.inicio
    while True:
        clientes.append(f"Cédula: {actual.cedula}, Nombre: {actual.nombre}")
        if actual == self.inicio:
            break
        return clientes

class App:
    def __init__(self, root):
        self.root = root
        self.root.tittle("Listar circular de clientes")
        self.lista = ListaCircularCliente()

        self.lbl_cedula = tk.Label(root, text="Cédula:")
        self.lbl_cedula.pack()
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.pack()

        self.lbl_nombre = tk.Label(root, text="Nombre:")
        self.lbl_cedula.pack()
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.pack()

        
