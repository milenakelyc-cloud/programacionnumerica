import matplotlib.pyplot as plt
import numpy as np

def procesar_funcion_lineal(expresion):
    # Limpiar espacios
    expresion = expresion.replace(" ", "")
    
    # Normalización básica de la expresión
    if expresion == "x":
        funcion_procesada = "1*x"
    elif expresion.startswith("x"):
        funcion_procesada = "1*" + expresion
    else:
        funcion_procesada = expresion

    # Lógica para extraer pendiente e intercepto
    # Nota: Esta lógica es simple y asume un formato 'mx+b'
    try:
        if '*x' in funcion_procesada:
            pendiente = funcion_procesada.split('*x')[0]
        else:
            pendiente = funcion_procesada.split('x')[0]
            if pendiente == "" or pendiente == "+": pendiente = "1"
            if pendiente == "-": pendiente = "-1"
    except:
        pendiente = "1"

    if '+' in funcion_procesada:
        partes = funcion_procesada.split('+')
        intercepto = partes[1] if len(partes) > 1 else '0'
    elif '-' in funcion_procesada and funcion_procesada.count('-') > (1 if funcion_procesada.startswith('-') else 0):
        # Manejo simple para signos negativos
        partes = funcion_procesada.rsplit('-', 1)
        intercepto = '-' + partes[1]
    else:
        intercepto = '0'

    print(f"Función procesada: y = {pendiente}x + {intercepto}")
    print(f"Pendiente: {pendiente}")
    print(f"Intercepto con Y: {intercepto}")
    
    return float(pendiente), float(intercepto), expresion

def graficar_funcion_lineal():
    entrada = input("Introduce la función lineal (ej. 2*x + 3 o x - 5): ")
    try:
        m, b, original = procesar_funcion_lineal(entrada)
    except Exception as e:
        print(f"Error al procesar la función: {e}")
        return

    # Crear datos para la gráfica
    x_valores = np.linspace(-10, 10, 400)
    y_valores = m * x_valores + b

    # Configuración de la gráfica
    plt.figure(figsize=(12, 8))
    plt.plot(x_valores, y_valores, color='red', linewidth=3, label=f'f(x) = {entrada}')
    
    # Ejes cartesianos
    plt.axhline(y=0, color='black', linewidth=1, alpha=0.7)
    plt.axvline(x=0, color='black', linewidth=1, alpha=0.7)
    
    # Estética
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    plt.title(f'Gráfico de la función: y = {entrada}', fontsize=14)
    plt.xlabel('Eje X', fontsize=12)
    plt.ylabel('Eje Y', fontsize=12)
    plt.legend(fontsize=12)
    
    plt.tight_layout()
    plt.show()

if __name__ == "_main_":
    graficar_funcion_lineal()