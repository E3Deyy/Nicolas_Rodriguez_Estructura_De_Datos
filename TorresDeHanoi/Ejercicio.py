import tkinter as tk
import time

class TorreDeHanoiGUI:
    def __init__(self, root, n_discos):
        self.root = root
        self.root.tittle("Torres de Hanoi")
        self.n_discos = n_discos

        #Configuración de canvas
        self.canvas = tk.Canvas(root, width=600, height=300, bg="White")
        self.canvas.pack

        self.torres = {'A': [], 'B': [], 'C': []}
        self.coords_torres = {'A': 100, 'B': 300, 'C':500}
        self.altura_base = 250

        self.crear_discos()

        #hago retraso en el algoritmo
        self.root.after(1000, lambda: self.torres_de_hanoi(self.n_discos, 'A', 'B', 'C'))

  def crear_discos(self):
      for i in range(self.n_discos, 0, -1):
          ancho = 20 + i * 20
          disco = self.canvas.create_rectangle(0, 0, ancho, 20, fill="black")
          self.torres['A'].append(disco)
      self.actualizar_dibujos()
      
  def actualizar_dibujos(self):
      for torre in ['A', 'B', 'C']:
          x_base = self.coords_torres[torre]
          for idx, disco in enumerate(reversed(self.torres[torre])):
              ancho = self.canvas.coords(disco)[2]
              x1 = x_base - ancho // 2
              y1 = self.altura_base - (idx + 1) * 22
              x2 = x_base + ancho
              y2 = y1 + 20
              self.canvas.coords(disco, x1, y1, x2, y2)
      self.root.update()
      time.sleep(0.5)

def mover_disco(self, origen, destino):
    disco = self.torres[origen].pop()
    self.torres[destino].append(disco)
    self.actualizar_dibujos()

def torres_de_hanoi(self, n, origen, destino, ayudante):
    if n ==1:
        self.mover_disco(origen, destino)
    else:
        self.torres_de_hanoi(n - 1, origen, ayudante, destino)
        self.mover_disco(origen, destino)
        self.torres_de_hanoi(n - 1, ayudante, destino, origen)

#Programa main
if __name__ == "__main__":
    discos = int(input("ingrese el numero de discos: "))
    root = tk.Tk()
    app = TorreDeHanoiGUI(root, discos)
    riit.mainloop()
