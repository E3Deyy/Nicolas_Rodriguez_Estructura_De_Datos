#Por interfaz gráfica

import tkinter as tk
from tkinter impor messagebox

# Método de ordenamiento Burbuja
def metodo_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Método de ordenamiento Secuencial (por inserción)
def metodo_secuencial(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

# Método Quicksort (ordenamiento rápido)
def metodo_quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return metodo_quicksort(izquierda) + centro + metodo_quicksort(derecha)

  #interfaz gráfica


    def obtener_lista(self):
        entrada = self.entry_datos.get()
        try:
            lista = [int(x.strip()) for x in entrada.split(',')]
            return lista
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese solo números enteros separados por comas.")
            return None

    def mostrar_resultado(self, metodo, lista):
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, f"Resultado con {metodo}:\n{lista}")

    def ordenar_burbuja(self):
        lista = self.obtener_lista()
        if lista is not None:
            ordenada = metodo_burbuja(lista)
            self.mostrar_resultado("Método Burbuja", ordenada)

    def ordenar_secuencial(self):
        lista = self.obtener_lista()
        if lista is not None:
            ordenada = metodo_secuencial(lista)
            self.mostrar_resultado("Método Secuencial", ordenada)

    def ordenar_quicksort(self):
        lista = self.obtener_lista()
        if lista is not None:
            ordenada = metodo_quicksort(lista)
            self.mostrar_resultado("Método Quicksort", ordenada)

# Ejecutar la aplicación
if __name__ == '__main__':
    root = tk.Tk()
    app = OrdenamientoApp(root)
    root.mainloop()
