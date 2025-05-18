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

        self.crear_discos{}

        #hago retraso en el algoritmo
        self.root.after(1000, lambda: self.torres_de_hanoi(self.n_discos, 'A', 'B', 'C'))

  def crear_discos(self):
      for i in range(self.n_discos, 0, -1):
          ancho = 20 + i * 20
          disco = self.canvas.create_rectangle(0, 0, ancho, 20, fill="black")
          self.torres['A'].append()
      self.actualizar_dibujos()
