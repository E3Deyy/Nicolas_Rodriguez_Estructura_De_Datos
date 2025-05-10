import tkinter as tk
from tkinter import messagebox

# Nodo de la lista circular
class NodoCliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None
