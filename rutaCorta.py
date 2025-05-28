import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming # type: ignore
import tkinter as tk
from tkinter import messagebox, simpledialog

class TSPApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de TSP")
        self.master.geometry("400x400")  # Tamaño de la ventana
        self.master.configure(bg="#FFB6C1")  # Color de fondo rosa claro

        self.size = 0
        self.matrix = None
        self.entries = []

        # Etiqueta de título
        self.title_label = tk.Label(master, text="Calculadora de Ruta Más Corta (TSP)", font=("Arial", 16), bg="#FFB6C1")
        self.title_label.pack(pady=10)

        # Botón para definir el tamaño de la matriz
        self.size_button = tk.Button(master, text="Definir Tamaño de la Matriz", command=self.set_matrix_size, font=("Arial", 12), bg="#D8BFD8", activebackground="white")
        self.size_button.pack(pady=10)

        # Botón para calcular la ruta más corta
        self.calculate_button = tk.Button(master, text="Calcular Ruta Más Corta", command=self.calculate_route, font=("Arial", 12), bg="#D8BFD8", activebackground="white")
        self.calculate_button.pack(pady=10)

        # Botón para borrar la matriz
        self.clear_button = tk.Button(master, text="Borrar Matriz", command=self.clear_matrix, font=("Arial", 12), bg="#D8BFD8", activebackground="white")
        self.clear_button.pack(pady=10)

        # Marco para la matriz
        self.matrix_frame = tk.Frame(master, bg="#FFB6C1")
        self.matrix_frame.pack(pady=10)

    def set_matrix_size(self):
        size = simpledialog.askinteger("Tamaño de la matriz", "Ingrese el tamaño de la matriz cuadrada (n x n):", minvalue=1)
        if size is not None:
            self.size = size
            self.create_matrix_entries()

    def create_matrix_entries(self):
        # Limpiar entradas anteriores
        for entry in self.entries:
            for e in entry:
                e.destroy()
        self.entries.clear()

        # Crear entradas para la matriz
        for i in range(self.size):
            row_entries = []
            for j in range(self.size):
                entry = tk.Entry(self.matrix_frame, width=5, font=("Arial", 12))
                entry.grid(row=i, column=j, padx=5, pady=5)  # Espaciado entre entradas
                row_entries.append(entry)
            self.entries.append(row_entries)

    def calculate_route(self):
        if self.size == 0:
            messagebox.showwarning("Advertencia", "Defina primero el tamaño de la matriz.")
            return

        # Leer la matriz de las entradas
        self.matrix = np.zeros((self.size, self.size))
        try:
            for i in range(self.size):
                for j in range(self.size):
                    value = self.entries[i][j].get()
                    if value == '':
                        self.matrix[i][j] = 0  # Si está vacío, consideramos 0
                    else:
                        self.matrix[i][j] = float(value)

            # Verificar la matriz antes de resolver
            print("Matriz ingresada:")
            print(self.matrix)

            # Resolver el TSP
            ruta, distancia = solve_tsp_dynamic_programming(self.matrix)

            # Ajustar la ruta para que sea más legible (ciudades numeradas desde 1)
            ruta = np.array(ruta) + 1

            # Mostrar el resultado
            mensaje = f"La ruta más corta es: {ruta}\nLa distancia total es: {distancia}"
            messagebox.showinfo("Resultado", mensaje)
        except ValueError as e:
            messagebox.showerror("Error", f"Por favor, ingrese valores numéricos válidos. Detalle: {e}")

    def clear_matrix(self):
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
app = TSPApp(root)

# Ejecutar el bucle principal de la interfaz
root.mainloop()