import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("METODO DE REGULA FALSI (Falsa Posicion)")
print("="*60)

print("\nEjemplos de funciones:")
print(" x**3 - x - 2")
print(" np.exp(x) - 3*x")
print(" x*np.sin(x) - 1")

func_str = input("\nIngrese f(x): ")
def f(x):
    return eval(func_str , {"np": np , "x": x})

a_plot = float(input("Limite inferior para grafica: "))
b_plot = float(input("Limite superior para grafica: "))

x = np.linspace(a_plot , b_plot , 500)
y = [f(xi) for xi in x]

plt.figure(figsize =(10, 6))
plt.plot(x, y, "b-", linewidth=2)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.grid()
plt.show()

aplicar = input("Aplicar metodo? (s/n): ")

if aplicar != "s":
    exit()

a = float(input("Extremo izquierdo [a]: "))
b = float(input("Extremo derecho [b]: "))

if f(a) * f(b) >= 0:
    print("ERROR: No hay cambio de signo")
    exit()

tol = float(input("Tolerancia: "))
max_iter = int(input("Maximo de iteraciones: "))

for i in range(max_iter):
    c = b - f(b)*(b - a)/(f(b) - f(a))
    fc = f(c)

    if abs(fc) < tol:
        break

    if f(a)*fc < 0:
        b = c
    else:
        a = c

print("Raiz aproximada: ", c)
print("f(c): ", fc)