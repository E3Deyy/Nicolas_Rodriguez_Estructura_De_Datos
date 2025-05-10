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
