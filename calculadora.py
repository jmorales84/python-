import cmath
import math
import matplotlib.pyplot as plt
from colorama import Fore, Style

# Función para mostrar el menú de opciones
def menu():
    print("----------MENU----------")
    print(f"{Fore.GREEN}1. SUMA")
    print(f"{Fore.YELLOW}2. RESTA")
    print(f"{Fore.BLUE}3. MULTIPLICACION")
    print(f"{Fore.MAGENTA}4. DIVISION")
    print(f"{Fore.CYAN}5. POTENCIAS A LA N")
    print(f"{Fore.RED}6. POTENCIAS DE i")
    print(f"{Fore.GREEN}7. RAICES DE NUMEROS COMPLEJOS")
    print(f"{Fore.YELLOW}8. SALIR")
    print(Style.RESET_ALL)

# Función para realizar operaciones entre números complejos
def realizar_operacion(complejo1, complejo2, operacion):
    if operacion == 1:
        resultado = complejo1 + complejo2
    elif operacion == 2:
        resultado = complejo1 - complejo2
    elif operacion == 3:
        resultado = complejo1 * complejo2
    elif operacion == 4:
        # Manejo de división por cero
        if complejo2 == 0:
            print(f"{Fore.RED}Error: No se puede dividir por cero.")
            return None
        resultado = complejo1 / complejo2
    return resultado

# Función para graficar números complejos en el plano cartesiano
def graficar_cartesiano(complejo1, complejo2, resultado):
    fig, ax = plt.subplots()
    # Graficar operandos y resultado si son distintos
    if complejo1 != resultado:
        ax.plot([complejo1.real, complejo2.real], [complejo1.imag, complejo2.imag], 'bo-', label='Operandos')
        ax.text(complejo1.real, complejo1.imag, f'({complejo1.real}, {complejo1.imag})', fontsize=10, ha='right')
        ax.text(complejo2.real, complejo2.imag, f'({complejo2.real}, {complejo2.imag})', fontsize=10, ha='right')
    ax.plot([resultado.real], [resultado.imag], 'ro', label='Resultado')
    ax.text(resultado.real, resultado.imag, f'({resultado.real}, {resultado.imag})', fontsize=10, ha='right')
    # Ajustes estéticos del gráfico
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('gray')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_aspect('equal', adjustable='box')
    ax.legend(loc='upper left')
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.title("Gráfica cartesiana", fontsize=15, color='red', fontname="Times New Roman")
    plt.grid(True)
    plt.show()

# Función para graficar números complejos en el plano polar
def graficar_polar(complejo1, complejo2, resultado):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    # Graficar operandos y resultado si son distintos
    if complejo1 != resultado:
        ax.plot([cmath.phase(complejo1), cmath.phase(complejo2)], [abs(complejo1), abs(complejo2)], 'bo-', label='Operandos')
    ax.plot([cmath.phase(resultado)], [abs(resultado)], 'ro', label='Resultado')
    ax.legend(loc='upper right')
    ax.set_title("Gráfica polar", fontsize=15, fontname="Times New Roman")  # Modificado el título aquí
    plt.show()

# Bucle principal
repetir = True
while repetir:
    print(f"{Fore.CYAN}**************Calculadora de Numeros Complejos**************")
    print("Numeros de la forma a+bi")
    print("Con a como la parte real y b la parte imaginaria")
    print("************************************************************")
    menu()
    case = int(input(f"{Fore.YELLOW}Selecciona una operacion: {Style.RESET_ALL}"))
    if case == 8:
        # Opción para salir
        print(f"{Fore.RED}Saliendo de la calculadora...")
        repetir = False
    elif case in [1, 2, 3, 4]:
        # Ingresar números complejos para operaciones binarias
        a = float(input(f"{Fore.YELLOW}Digite la parte real del primer numero complejo: {Style.RESET_ALL}"))
        b = float(input(f"{Fore.YELLOW}Digite la parte imaginaria del primer numero complejo: {Style.RESET_ALL}"))
        complejo1 = complex(a, b)
        print(f"{Fore.GREEN}Numero ingresado: {complejo1}")
        c = float(input(f"{Fore.YELLOW}Digite la parte real del segundo numero complejo: {Style.RESET_ALL}"))
        d = float(input(f"{Fore.YELLOW}Digite la parte imaginaria del segundo numero complejo: {Style.RESET_ALL}"))
        complejo2 = complex(c, d)
        print(f"{Fore.GREEN}Numero ingresado: {complejo2}")
        resultado  = realizar_operacion(complejo1, complejo2, case)
        if resultado is not None:
            print(f"{Fore.GREEN}El resultado: {resultado}")
            graficar_cartesiano(complejo1, complejo2, resultado)
            graficar_polar(complejo1, complejo2, resultado)
        elif case == 5:
            #Ingresar numero complejo y potencia para operacion de potencia
            a = float(input(f"{Fore.YELLOW}Digite la parte real del numero complejo:{Style.RESET_ALL}"))
            b = float(input(f"{Fore.YELLOW}Digite la parte imaginaria del numero complejo:{Style.RESET_ALL}"))
            c = float(input(f"{Fore.YELLOW}Ingrese la potencia:{Style.RESET_ALL}"))
            complejo = complex(a,b)
            print(f"{Fore.GREEN}Numero ingresado: {complejo}^{c}")
            resultado = complejo ** c 
            print(f"{Fore.GREEN}El resultado es {resultado}")
            graficar_cartesiano(complejo,complejo,resultado)
            graficar_polar(complejo, complejo,resultado)
        elif case == 6:
            #Ingresar potencia para operacion de potencia i
            a = int(input(f"{Fore.YELLOW}Ingrese la potencia a elevar a i: {Style.RESET_ALL}"))
            print(f"{Fore.GRENN}Numero Ingresado i^{a}")
            b = a % 4
            if b == 0:
                print(f"{Fore.GREEN}El resultado es 1")
            elif b == 1:
                print(f"{Fore.GREEN}El resultado es i")
            elif b == 2:
                print(f"{Fore.GREEN}El resultado es -1")
            elif b == 3:
                print(f"{Fore.GREEN}El resultado es -i")
            graficar_cartesiano(b,0,b)
            graficar_polar(b,0,b)
        elif case == 7:
            #Ingresar numero complejo y raiz para operacion de raices
            a = float(input(f"{Fore.YELLOW}Digite la parte real del numero complejo: {Style.RESET_ALL}"))
            b = float(input(f"{Fore.YELLOW}Digite la parte imaginaria del numero complejo: {Style.RESET_ALL}"))
            c = float(input(f"{Fore.YELLOW}Ingresa la raiz: {Style.RESET_ALL}"))
            complejo = complex(a,b)
            if c <= 0:
                print(f"{Fore.RED}Error: La raiz debe ser un entero positivo.")
            else: 
                s = abs(complejo)
                angulo = cmath.phase(complejo)
                raiz = cmath.phase(complejo ** (1 / float (c)))
                for contador in range (c):
                    z = cmath.rect(s ** (1 / float (c)),(raiz + 2 * math.pi * contador) / c)
                    print(f"{Fore.GREEN}Forma polar: MAGNITUD: {abs(z)} ANGULO: {math.degress(cmath.phase(z))}")
                    print(f"{Fore.GREEN}El resultado es: {z}")
                    graficar_cartesiano(complejo, complejo, z)
                    graficar_polar(complejo, complejo, z)
    rep = input(f"{Fore.YELLOW}Desea realizar otra operacion? [Si/No]: {Style.RESET.ALL}")
    if rep.lower() != "si":
        repetir = False  
                       
                
                