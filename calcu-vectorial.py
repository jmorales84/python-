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
        # Valores de t
        t = np.linspace(float(entry_tmin.get()), float(entry_tmax.get()), 500)

        # Evaluación de las expresiones ingresadas
        x = eval(entry_xt.get(), {"t": t, **np.__dict__})
        y = eval(entry_yt.get(), {"t": t, **np.__dict__})

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
        # Valores de theta
        theta = np.linspace(0, 2 * np.pi, 500)

        # Evaluación de la expresión ingresada
        r = eval(entry_rtheta.get(), {"theta": theta, **np.__dict__})

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

# Entradas para vectores y gráficas
# ... (la parte restante del código no cambia)

# Iniciar la aplicación
root.mainloop()
