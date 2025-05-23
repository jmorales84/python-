import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

# Crear la ventana principal
root = tk.Tk()
root.title("Operaciones y Gráficas Matemáticas")
root.geometry("900x800")

# Crear la figura para graficar
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

# Función para sumar los vectores y graficarlos
def sumar_vectores():
    try:
        v1 = np.array([float(entry_v1x.get()), float(entry_v1y.get()), float(entry_v1z.get())])
        v2 = np.array([float(entry_v2x.get()), float(entry_v2y.get()), float(entry_v2z.get())])
        suma = v1 + v2

        resultado_label.config(text=f"Suma: {suma}")

        ax.clear()
        ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='blue', label='v1')
        ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='green', label='v2')
        ax.quiver(0, 0, 0, suma[0], suma[1], suma[2], color='red', label='v1 + v2')
        ax.legend()
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        canvas.draw()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Función para restar los vectores y graficarlos
def restar_vectores():
    try:
        v1 = np.array([float(entry_v1x.get()), float(entry_v1y.get()), float(entry_v1z.get())])
        v2 = np.array([float(entry_v2x.get()), float(entry_v2y.get()), float(entry_v2z.get())])
        resta = v1 - v2

        resultado_label.config(text=f"Resta: {resta}")

        ax.clear()
        ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='blue', label='v1')
        ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='green', label='v2')
        ax.quiver(0, 0, 0, resta[0], resta[1], resta[2], color='purple', label='v1 - v2')
        ax.legend()
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        canvas.draw()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Función para calcular el producto punto
def producto_punto():
    try:
        v1 = np.array([float(entry_v1x.get()), float(entry_v1y.get()), float(entry_v1z.get())])
        v2 = np.array([float(entry_v2x.get()), float(entry_v2y.get()), float(entry_v2z.get())])
        punto = np.dot(v1, v2)

        resultado_label.config(text=f"Producto punto: {punto}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Función para calcular el producto cruz y graficarlo
def producto_cruz():
    try:
        v1 = np.array([float(entry_v1x.get()), float(entry_v1y.get()), float(entry_v1z.get())])
        v2 = np.array([float(entry_v2x.get()), float(entry_v2y.get()), float(entry_v2z.get())])
        cruz = np.cross(v1, v2)

        resultado_label.config(text=f"Producto cruz: {cruz}")

        ax.clear()
        ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='blue', label='v1')
        ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='green', label='v2')
        ax.quiver(0, 0, 0, cruz[0], cruz[1], cruz[2], color='orange', label='v1 x v2')
        ax.legend()
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        canvas.draw()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Función para graficar curvas paramétricas
def graficar_parametricas():
    try:
        t = np.linspace(float(entry_tmin.get()), float(entry_tmax.get()), 500)
        x = eval(entry_xt.get())
        y = eval(entry_yt.get())

        ax.clear()
        ax.plot(x, y, label="Curva paramétrica")
        ax.legend()
        ax.set_xlabel("x(t)")
        ax.set_ylabel("y(t)")
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar las expresiones: {e}")

# Función para graficar curvas polares
def graficar_polares():
    try:
        theta = np.linspace(0, 2 * np.pi, 500)
        r = eval(entry_rtheta.get())

        ax.clear()
        ax.plot(r * np.cos(theta), r * np.sin(theta), label="Curva polar")
        ax.legend()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar la expresión: {e}")

# Crear el marco de entrada
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Entradas para vectores
tk.Label(frame, text="Vector 1 (x, y, z):").grid(row=0, column=0, sticky="e")
entry_v1x = tk.Entry(frame, width=5)
entry_v1x.grid(row=0, column=1)
entry_v1y = tk.Entry(frame, width=5)
entry_v1y.grid(row=0, column=2)
entry_v1z = tk.Entry(frame, width=5)
entry_v1z.grid(row=0, column=3)

tk.Label(frame, text="Vector 2 (x, y, z):").grid(row=1, column=0, sticky="e")
entry_v2x = tk.Entry(frame, width=5)
entry_v2x.grid(row=1, column=1)
entry_v2y = tk.Entry(frame, width=5)
entry_v2y.grid(row=1, column=2)
entry_v2z = tk.Entry(frame, width=5)
entry_v2z.grid(row=1, column=3)

# Botones para operaciones vectoriales
tk.Button(frame, text="Sumar Vectores", command=sumar_vectores).grid(row=2, column=0, columnspan=4, pady=5)
tk.Button(frame, text="Restar Vectores", command=restar_vectores).grid(row=3, column=0, columnspan=4, pady=5)
tk.Button(frame, text="Producto Punto", command=producto_punto).grid(row=4, column=0, columnspan=4, pady=5)
tk.Button(frame, text="Producto Cruz", command=producto_cruz).grid(row=5, column=0, columnspan=4, pady=5)

# Entradas para curvas paramétricas
tk.Label(frame, text="x(t) =").grid(row=6, column=0, sticky="e")
entry_xt = tk.Entry(frame, width=15)
entry_xt.grid(row=6, column=1, columnspan=3)

tk.Label(frame, text="y(t) =").grid(row=7, column=0, sticky="e")
entry_yt = tk.Entry(frame, width=15)
entry_yt.grid(row=7, column=1, columnspan=3)

tk.Label(frame, text="t mínimo:").grid(row=8, column=0, sticky="e")
entry_tmin = tk.Entry(frame, width=5)
entry_tmin.grid(row=8, column=1)

tk.Label(frame, text="t máximo:").grid(row=8, column=2, sticky="e")
entry_tmax = tk.Entry(frame,width=5)
entry_tmax.grid(row=8, column=3)

tk.Button(frame, text="Graficar Paramétricas", command=graficar_parametricas).grid(row=9, column=0, columnspan=4, pady=5)

# Entradas para curvas polares
tk.Label(frame, text="r(θ) =").grid(row=10, column=0, sticky="e")
entry_rtheta = tk.Entry(frame, width=15)
entry_rtheta.grid(row=10, column=1, columnspan=3)

tk.Button(frame, text="Graficar Polares", command=graficar_polares).grid(row=11, column=0, columnspan=4, pady=5)

# Etiqueta para mostrar los resultados
resultado_label = tk.Label(frame, text="", fg="blue", wraplength=300)
resultado_label.grid(row=12, column=0, columnspan=4, pady=10)

# Crear el canvas para la gráfica
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Iniciar la aplicación
root.mainloop()

