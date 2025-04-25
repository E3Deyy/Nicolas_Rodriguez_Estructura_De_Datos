#Ejercicio Listas dobles MVC
import tkinter as tk
from tkinter import messagebox

# Clase Cliente
class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

# Clase Lista Doble
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = Cliente(cedula, nombre)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        elif cedula < self.cabeza.cedula:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.cedula < cedula:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = nuevo
            else:
                self.cola = nuevo
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def listar_derecha(self):
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(f"Cédula: {actual.cedula}, Nombre: {actual.nombre}")
            actual = actual.siguiente
        return resultado
#Creo la ventana que aparecerá
ventana = tk.Tk()
ventana.tittle("Lista doble de clientes")

#Creo el objeto lista
lista = ListaDoble()

#Funciones para los botones
def agregar_cliente():
    cedula_texto = entrada_cedula.get()
    nombre = entrada_nombre.get()
    if cedula_texto.isdigit() and nombre:
        cedula = int(cedula_texto)
        lista.insertar_cliente(cedula, nombre)
        messagebox.showinfo("Muy bien", "El cliente se ha agregado.")
        entrada_cedula.delete(0, tk.END)
        entrada_nombre.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Debes ingresar el tipo válido para la cédula y un nombre.")

def mostrar_derecha():
    salida.delete(1.0, tk.END)
    clientes = lista.listar_derecha()
    for cliente in clientes:
        salida.insert(tk.END, cliente + "\n")

def mostrar_izquierda():
    salida.delete(1.0, tk.END)
    clientes = lista.listar_izquierda()
    for cliente in clientes:
        salida.insert(tk.END, cliente + "\n")
#Elementos que salen en la interfaz
tk.Label(ventana, text="Cédula: ").grid(row=0, column=0)
entrada_cedula = tk.Entry(ventana)
entrada_cedula.grid(row=0, column=1)

tk.label(ventana, text="Nombre: ").grid(row=1, column=0)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=1, column=1)

tk.Button(ventana, text="Agregar cliente", command=agregar_cliente).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(ventana, text="Listar (inicio -> Fin)", command=mostrar_derecha).grid(row=3, column=0, columnspan=2)
tk.Button(ventana, text="Listar (Fin -> Inicio)", command=mostrar_izquierda).grid(row=4, column=0, columnspan=2)
salida = tk.Text(ventana, width=30, height=10)
salida.grid(row=5, column=0, columnspan=2, pady=10)

#ventana
ventana.mainloop()
