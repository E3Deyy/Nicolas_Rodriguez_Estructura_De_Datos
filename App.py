import tkinter as tk
from tkinter import messagebox

# Interfaz gráfica
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista Circular de Clientes")
        self.lista = ListaCircularClientes()

        self.lbl_cedula = tk.Label(root, text="Cédula:")
        self.lbl_cedula.pack()
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.pack()

        self.lbl_nombre = tk.Label(root, text="Nombre:")
        self.lbl_nombre.pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        self.btn_insertar = tk.Button(root, text="Insertar Cliente", command=self.insertar_cliente)
        self.btn_insertar.pack(pady=5)

        self.btn_listar = tk.Button(root, text="Listar Clientes", command=self.listar_clientes)
        self.btn_listar.pack(pady=5)

        self.btn_salir = tk.Button(root, text="Salir", command=root.quit)
        self.btn_salir.pack(pady=5)

        self.txt_resultado = tk.Text(root, height=10, width=50)
        self.txt_resultado.pack()

    def insertar_cliente(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        if not cedula or not nombre:
            messagebox.showwarning("Campos vacíos", "Por favor, ingresa la cédula y el nombre.")
            return
        self.lista.insertar_cliente(cedula, nombre)
        messagebox.showinfo("Éxito", "Cliente insertado correctamente.")
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)

    def listar_clientes(self):
        clientes = self.lista.listar_clientes()
        self.txt_resultado.delete("1.0", tk.END)
        if clientes:
            for c in clientes:
                self.txt_resultado.insert(tk.END, c + "\n")
        else:
            self.txt_resultado.insert(tk.END, "No hay clientes en la lista.")

# Ejecutar la aplicación
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
