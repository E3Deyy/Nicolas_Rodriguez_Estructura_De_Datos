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

        self.lbl_cedula = tk.Label(root, tect="Insertar cliente " , command=self.insertar_cliente)
        self.btn_insertat.pack(pady=5)

        self.btn_salir = tk.Button(root, text="Salir ", command=root.quit)
        self.btn_salir.pack(pady=6)

        self.txt_resultado = tk.Text(root, height=10, width=50)
        self.txt_resultado.pack()

    def insertar_cliente(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre: get().strip()
        if not cedula or not nombre:
            messagebox.showwarning("Hay campos vacíos", "Llene toda la información por favor.")
        self.lista.insertar_cliente(cedula, nombre)
        messagebox.showinfo("Perfecto", "Cliente insertado")
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete("1.0" tk.END)
        if clientes:
            for c in clientes:
                self.txt_resultado.insert(tk.END, c + "\n")
        else: 
            self.txt_resultado.insert(tk.END, "No hay clientes en la lista")
        #Ejecuto la aplicación
        if __name__ == '__main__':
            root = tk.Tk()
            app = App(root)
            root.mainloop()
