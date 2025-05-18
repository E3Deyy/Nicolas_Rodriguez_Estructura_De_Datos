#Ejercicio previamente hecho en clase

import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Bicola:
    def __init__(self):
        self.frente = None
        self.final = None

    def insertar_derecha(self, dato):
        nuevo = Nodo(dato)
        if self.frente is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def insertar_izquierda(self, dato):
        nuevo = Nodo(dato)
        if self.frente is None:
            self.frente = self.final = nuevo
        else:
            nuevo.siguiente = self.frente
            self.frente = nuevo

    def atender_derecha(self):
        if self.frente is None:
            return "Bicola vacía"
        if self.frente == self.final:
            dato = self.final.dato
            self.frente = self.final = None
            return f"Atendido: {dato}"
        actual = self.frente
        while actual.siguiente != self.final:
            actual = actual.siguiente
        dato = self.final.dato
        actual.siguiente = None
        self.final = actual
        return f"Atendido: {dato}"

    def atender_izquierda(self):
        if self.frente is None:
            return "Bicola vacía"
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return f"Atendido: {dato}"

    def listar(self):
        actual = self.frente
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) if elementos else "Bicola vacía"

class App:
    def __init__(self, root):
        self.bicola = Bicola()
        self.root = root
        self.root.title("Bicola - Estructura Dinámica")

        # Entradas
        self.entry = tk.Entry(root, width=30)
        self.entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Botones de insertar
        tk.Button(root, text="Insertar por la izquierda", command=self.insertar_izquierda).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(root, text="Insertar por la derecha", command=self.insertar_derecha).grid(row=1, column=1, padx=10, pady=5)

        # Botones de atender
        tk.Button(root, text="Atender por la izquierda", command=self.atender_izquierda).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(root, text="Atender por la derecha", command=self.atender_derecha).grid(row=2, column=1, padx=10, pady=5)

        # Botón de listar
        tk.Button(root, text="Listar", command=self.mostrar_lista).grid(row=3, column=0, columnspan=2, pady=5)

        # Área de salida
        self.texto = tk.Text(root, height=10, width=50)
        self.texto.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def insertar_izquierda(self):
        dato = self.entry.get()
        if dato:
            self.bicola.insertar_izquierda(dato)
            self.entry.delete(0, tk.END)
            self.mostrar_lista()

    def insertar_derecha(self):
        dato = self.entry.get()
        if dato:
            self.bicola.insertar_derecha(dato)
            self.entry.delete(0, tk.END)
            self.mostrar_lista()

    def atender_izquierda(self):
        resultado = self.bicola.atender_izquierda()
        self.mostrar_resultado(resultado)

    def atender_derecha(self):
        resultado = self.bicola.atender_derecha()
        self.mostrar_resultado(resultado)

    def mostrar_lista(self):
        self.texto.delete(1.0, tk.END)
        contenido = self.bicola.listar()
        self.texto.insert(tk.END, "Contenido de la Bicola:\n" + contenido)

    def mostrar_resultado(self, mensaje):
        self.texto.delete(1.0, tk.END)
        self.texto.insert(tk.END, mensaje + "\n\n" + "Contenido actual:\n" + self.bicola.listar())

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
