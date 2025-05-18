import tkinter as tk
import time
import random

class TorreDeHanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanoi")
        self.altura_base = 350
        self.altura_canvas = 500
        self.ancho_canvas = 700
        self.torres = {'A': [], 'B': [], 'C': []}
        self.coords_torres = {'A': 150, 'B': 350, 'C': 550}
        self.n_discos = 0

        self.mostrar_pantalla_inicial()

    def mostrar_pantalla_inicial(self):
        self.frame_inicio = tk.Frame(self.root)
        self.frame_inicio.pack(pady=20)

        tk.Label(self.frame_inicio, text="Ingrese el número de discos:").pack()
        self.entry_discos = tk.Entry(self.frame_inicio)
        self.entry_discos.pack(pady=5)

        tk.Button(self.frame_inicio, text="Iniciar", command=self.iniciar_juego).pack(pady=10)

    def iniciar_juego(self):
        try:
            self.n_discos = int(self.entry_discos.get())
            if self.n_discos < 1:
                raise ValueError
        except ValueError:
            self.entry_discos.delete(0, tk.END)
            self.entry_discos.insert(0, "Número inválido")
            return

        self.frame_inicio.destroy()
        self.canvas = tk.Canvas(self.root, width=self.ancho_canvas, height=self.altura_canvas, bg="white")
        self.canvas.pack()

        self.boton_reiniciar = tk.Button(self.root, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack(pady=10)

        self.dibujar_bases()
        self.crear_discos()
        self.root.after(1000, lambda: self.torres_de_hanoi(self.n_discos, 'A', 'C', 'B'))

    def dibujar_bases(self):
        # Palos
        for x in self.coords_torres.values():
            self.canvas.create_rectangle(x - 5, 100, x + 5, self.altura_base, fill="gray")
        # Base negra
        self.canvas.create_rectangle(50, self.altura_base, 650, self.altura_base + 10, fill="black")

    def crear_discos(self):
        colores = self.generar_colores(self.n_discos)
        max_ancho = 120
        min_ancho = 40
        paso_ancho = (max_ancho - min_ancho) // max(self.n_discos - 1, 1)

        for i in range(self.n_discos, 0, -1):
            ancho = min_ancho + (i - 1) * paso_ancho
            color = colores[i - 1]
            disco_id = self.canvas.create_rectangle(0, 0, ancho, 20, fill=color, outline="black")
            disco_info = {"id": disco_id, "ancho": ancho, "color": color}
            self.torres['A'].insert(0, disco_info)
        self.actualizar_dibujos()

    def actualizar_dibujos(self):
        for torre in ['A', 'B', 'C']:
            x_base = self.coords_torres[torre]
            for idx, disco in enumerate(self.torres[torre]):
                ancho = disco["ancho"]
                disco_id = disco["id"]
                x1 = x_base - ancho // 2
                y1 = self.altura_base - (idx + 1) * 15
                x2 = x_base + ancho // 2
                y2 = y1 + 12
                self.canvas.coords(disco_id, x1, y1, x2, y2)
        self.root.update()
        time.sleep(0.3)

    def mover_disco(self, origen, destino):
        disco = self.torres[origen].pop(0)
        self.torres[destino].insert(0, disco)
        self.actualizar_dibujos()

    def torres_de_hanoi(self, n, origen, destino, auxiliar):
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.torres_de_hanoi(n - 1, origen, auxiliar, destino)
            self.mover_disco(origen, destino)
            self.torres_de_hanoi(n - 1, auxiliar, destino, origen)

    def generar_colores(self, n):
        colores = []
        for _ in range(n):
            colores.append("#%06x" % random.randint(0x555555, 0xAAAAAA))
        return colores

    def reiniciar(self):
        self.canvas.destroy()
        self.boton_reiniciar.destroy()
        self.torres = {'A': [], 'B': [], 'C': []}
        self.mostrar_pantalla_inicial()

# Programa principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TorreDeHanoiGUI(root)
    root.mainloop()
