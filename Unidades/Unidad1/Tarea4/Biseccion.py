import numpy as np
import matplotlib.pyplot as plt

print("Ejemplos: x**3-x-1 | x**2-4 | np.cos(x)-x")
func_str = input("\nIngrese funcion f(x): ")

def f(x):
    return eval(func_str, {"np": np, "x": x})

xmin = float(input("Valor minimo de x: "))
xmax = float(input("Valor maximo de x: "))

x = np.linspace(xmin, xmax, 400)
y = f(x)

plt.plot(x, y)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.grid()
plt.show()

aplicar = input("\n¿Aplicar método? (s/n): ").lower()

if aplicar == 's':
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))

    if f(a) * f(b) > 0:
        print("No hay cambio de signo.")
    else:
        tol = 1e-6
        for i in range(100):
            c = (a + b) / 2
            if abs(b - a) < tol:
                break
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        print(f"Raíz aproximada = {c}")