import numpy as np
import matplotlib.pyplot as plt

print("Ejemplos: x**3 - x - 1 | np.exp(x) - 3*x | np.cos(x) - x")
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
    x0 = float(input("x0: "))
    x1 = float(input("x1: "))
    tol = 1e-6

    for i in range(100):
        fx0, fx1 = f(x0), f(x1)

        if fx1 == fx0:
            break

        x2 = x1 - fx1*(x1 - x0)/(fx1 - fx0)

        if abs(x2 - x1) < tol:
            break

        x0, x1 = x1, x2

    print(f"\nRaíz aproximada = {x2}")