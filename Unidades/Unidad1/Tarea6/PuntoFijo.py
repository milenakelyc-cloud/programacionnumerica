import numpy as np
import matplotlib.pyplot as plt

print("Método Punto Fijo — x = g(x)")
print("Ejemplos:")
print("  x**2 - 5 = 0 → np.sqrt(5)")
print("  x**3 - x - 1 = 0 → (x + 1)**(1/3)")
print("  cos(x) - x = 0 → np.cos(x)")

func_str = input("\nIngrese g(x): ")

def g(x):
    return eval(func_str, {"np": np, "x": x})

xmin = float(input("x min: "))
xmax = float(input("x max: "))

x = np.linspace(xmin, xmax, 400)
y_g = [g(xi) for xi in x]
y_id = x

plt.plot(x, y_g, label="g(x)")
plt.plot(x, y_id, "--", label="y=x")
plt.grid()
plt.legend()
plt.show()

aplicar = input("\n¿Aplicar método? (s/n): ").lower()

if aplicar == 's':
    x0 = float(input("x0: "))
    tol = 1e-6

    for i in range(100):
        x1 = g(x0)
        error = abs(x1 - x0)

        print(f"Iter {i+1}: x = {x1:.10f}, error = {error:.2e}")

        if error < tol:
            break

        x0 = x1

    print(f"\nPunto fijo encontrado ≈ {x1}")