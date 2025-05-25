import re
import random
import string
import tkinter as tk
from tkinter import messagebox

def limpiar_nombre(nombre):
    """
    Función que limpia y convierte el nombre a mayúsculas, eliminando tildes y caracteres especiales.
    """
    return re.sub(r'[áéíóú]', lambda x: {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}[x.group(0)], nombre).upper()

def obtener_consonantes_internas(apellido_paterno, apellido_materno, nombre):
    """
    Obtiene las primeras consonantes internas de los apellidos y el primer nombre.
    """
    consonantes = ''
    
    # Buscar consonantes internas (después de la primera vocal) en el apellido paterno
    consonantes += re.search(r'[^aeiou]*([bcdfghjklmnpqrstvwxyz])', apellido_paterno[1:], re.IGNORECASE).group(1) if apellido_paterno else ''
    
    # Buscar consonantes internas en el apellido materno
    consonantes += re.search(r'[^aeiou]*([bcdfghjklmnpqrstvwxyz])', apellido_materno[1:], re.IGNORECASE).group(1) if apellido_materno else ''
    
    # Buscar consonantes internas en el nombre
    consonantes += re.search(r'[^aeiou]*([bcdfghjklmnpqrstvwxyz])', nombre[1:], re.IGNORECASE).group(1) if nombre else ''
    
    return consonantes[:3]  # Tomamos solo las 3 primeras consonantes

def obtener_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais_origen):
    """
    Genera la CURP de una persona.
    
    :param nombre: Primer nombre de la persona.
    :param apellido_paterno: Apellido paterno de la persona.
    :param apellido_materno: Apellido materno de la persona.
    :param fecha_nacimiento: Fecha de nacimiento (DD/MM/AAAA).
    :param sexo: Sexo de la persona ('M' o 'H').
    :param pais_origen: País de origen de la persona (usa 'MEX' para México o 'NE' para Nacidos en el extranjero).
    :return: CURP generada.
    """
    # Limpiar y convertir a mayúsculas
    apellido_paterno = limpiar_nombre(apellido_paterno)
    apellido_materno = limpiar_nombre(apellido_materno)
    nombre = limpiar_nombre(nombre)

    # Primeras letras del apellido paterno
    curp = apellido_paterno[:2]

    # Primera letra del apellido materno
    curp += apellido_materno[0] if apellido_materno else 'X'

    # Primera letra del primer nombre
    curp += nombre[0] if nombre else 'X'

    # Fecha de nacimiento (en formato año, mes, día)
    dia, mes, anio = fecha_nacimiento.split('/')
    curp += anio[2:]  # Los dos últimos dígitos del año
    curp += mes  # El mes con dos dígitos
    curp += dia  # El día con dos dígitos

    # Sexo
    curp += sexo.upper()  # Sexo (M para masculino, H para femenino)

    # Entidad de nacimiento (2 letras)
    if pais_origen.upper() == "MEX":
        entidad = input("Ingresa la entidad de nacimiento (Código de dos letras): ").upper()
        curp += entidad
    else:
        # Si es nacido en el extranjero, se coloca "NE"
        curp += "NE"

    # Primeras consonantes internas de los apellidos paterno, materno y nombre
    curp += obtener_consonantes_internas(apellido_paterno, apellido_materno, nombre)

    # Homoclave (4 caracteres aleatorios)
    homoclave = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    curp += homoclave

    return curp

def mostrar_curp():
    """
    Función para mostrar la CURP en la interfaz gráfica.
    """
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    sexo = entry_sexo.get()
    pais_origen = entry_pais_origen.get()

    # Verificar que todos los campos estén llenos
    if not (nombre and apellido_paterno and apellido_materno and fecha_nacimiento and sexo and pais_origen):
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    try:
        # Generar CURP
        curp = obtener_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais_origen)
        label_resultado.config(text=f"Tu CURP es: {curp}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de CURP")
ventana.geometry("500x500")
ventana.config(bg="#f0f0f0")

# Etiquetas y campos de texto
label_nombre = tk.Label(ventana, text="Nombre:", bg="#f0f0f0")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack(pady=5)

label_apellido_paterno = tk.Label(ventana, text="Apellido Paterno:", bg="#f0f0f0")
label_apellido_paterno.pack(pady=5)
entry_apellido_paterno = tk.Entry(ventana, width=30)
entry_apellido_paterno.pack(pady=5)

label_apellido_materno = tk.Label(ventana, text="Apellido Materno:", bg="#f0f0f0")
label_apellido_materno.pack(pady=5)
entry_apellido_materno = tk.Entry(ventana, width=30)
entry_apellido_materno.pack(pady=5)

label_fecha_nacimiento = tk.Label(ventana, text="Fecha de Nacimiento (DD/MM/AAAA):", bg="#f0f0f0")
label_fecha_nacimiento.pack(pady=5)
entry_fecha_nacimiento = tk.Entry(ventana, width=30)
entry_fecha_nacimiento.pack(pady=5)

label_sexo = tk.Label(ventana, text="Sexo (M para masculino, H para femenino):", bg="#f0f0f0")
label_sexo.pack(pady=5)
entry_sexo = tk.Entry(ventana, width=30)
entry_sexo.pack(pady=5)

label_pais_origen = tk.Label(ventana, text="País de Origen (MEX para México, NE para Nacido en el Extranjero):", bg="#f0f0f0")
label_pais_origen.pack(pady=5)
entry_pais_origen = tk.Entry(ventana, width=30)
entry_pais_origen.pack(pady=5)

# Botón para generar la CURP
btn_generar = tk.Button(ventana, text="Generar CURP", command=mostrar_curp)
btn_generar.pack(pady=20)

# Etiqueta para mostrar la CURP generada
label_resultado = tk.Label(ventana, text="", bg="#f0f0f0", fg="blue")
label_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()


