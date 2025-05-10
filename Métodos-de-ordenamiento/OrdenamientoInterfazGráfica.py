#Por interfaz gráfica
import tkinter as tk
from tkinter import messagebox

# Método de ordenamiento Burbuja
def metodo_burbuja(lista):
    pasos = []
    n = len(lista)
    pasos.append(f"Lista inicial: {lista}")
    for i in range(n):
        for j in range(0, n - i - 1):
            pasos.append(f"Comparando {lista[j]} y {lista[j+ 1]}")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                pasos.append(f"Intercambiados: {lista}")
    pasos.append(f"Lista ordenada: {lista}")
    return lista, pasos

# Método de ordenamiento Secuencial (por inserción)
def metodo_secuencial(lista):
    pasos = []
    pasos.append(f"Lista inicial: {lista}")
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        pasos.append(f"Insertando {actual} en la parte ordenada")
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            pasos.append(f"Moviendo {lista[j]} a la derecha")
            j -= 1
        lista[j + 1] = actual
        pasos.append(f"Lista después de insertar: {lista}")
    pasos.append(f"Lista ordenada: {lista}")
    return lista, pasos

# Método Quicksort (ordenamiento rápido)
def metodo_quicksort(lista, profundidad=0):
    pasos = []
    def quicksort_interno(sublista, profundidad):
        if len(sublista) <= 1:
            return sublista, []
        indent = '  ' * profundidad
        pivote = sublista[len(sublista) // 2]
        izq = [x for x in sublista if x < pivote]
        centro = [x for x in sublista if x == pivote]
        der = [x for x in sublista if x > pivote]
        pasos_locales = [f"{indent}Sublista: {sublista}",
                         f"{indent}Pivote: {pivote}",
                         f"{indent}Izquierda: {izq}",
                         f"{indent}Centro: {centro}",
                         f"{indent}Derecha: {der}"]
        izq_ordenada, izq_pasos = quicksort_interno(izq, profundidad + 1)
        der_ordenada, der_pasos = quicksort_interno(der, profundidad + 1)
        return izq_ordenada + centro + der_ordenada, pasos_locales + izq_pasos + der_pasos
    ordenada, pasos = quicksort_interno(lista, profundidad)
    pasos.append(f"Lista ordenada: {ordenada}")
    return ordenada, pasos

  #interfaz gráfica
class OrdenamientoApp:
    def __init__(self, root):
        self.root = root
        self.root.tittle("Métodos de ordenamiento")

        tk.Label(root, text="Ingrese números separados por , : ").pack()
        self.entry_datos = tk.Entry(root, width=50)
        self.entry_datos.pack(pady=5)

        tk.Button(root, text="Método burbuja", command=self.ordenar_burbuja).pack(pady=2)
        tk.Button(root, text="Método inserción", command=self.ordenar_secuencial).pack(pady=2)
        tk.Button(root, text="Método quicksort", command=self.ordenar_quicksort).pack(pady=2)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

        self.resultado = tk.Text(root, height=11, width=70)
        self.resultado.pack()
    
    def obtener_lista(self):
        entrada = self.entry_datos.get()
        try:
            lista = [int(x.strip()) for x in entrada.split(',')]
            return lista
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese solo números enteros separados por comas.")
            return None

    def mostrar_resultado(self, metodo, lista, pasos):
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, f"Resultado con --{metodo}--:\n")
        for paso in pasos:
            self.resultado.insert(tk.END, paso + '\n')
            
    def ordenar_burbuja(self):
        lista = self.obtener_lista()
        if lista is not None:
            resultado, pasos = metodo_burbuja(lista)
            self.mostrar_resultado("Método Burbuja", resultado, pasos)

    def ordenar_secuencial(self):
        lista = self.obtener_lista()
        if lista is not None:
            resultado, pasos = metodo_secuencial(lista)
            self.mostrar_resultado("Método Secuencial", resultado, pasos)

    def ordenar_quicksort(self):
        lista = self.obtener_lista()
        if lista is not None:
            resultado, pasos = metodo_quicksort(lista)
            self.mostrar_resultado("Método Quicksort", resultado, pasos)

# Ejecutar la aplicación
if __name__ == '__main__':
    root = tk.Tk()
    app = OrdenamientoApp(root)
    root.mainloop()
