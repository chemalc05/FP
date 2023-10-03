def f(x):
    return x**3 - 4*x

def df(x):
    return 3*x**2 - 4

def newton(x0, tol, max_iter):
    x = x0
    for _ in range(max_iter):
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < tol: break
        x = x1
    return x

x0 = 0.8
tol = 1e-6
max_iter = 1000

root = newton(x0, tol, max_iter)
print("La raíz más cercana a x0 es", root)

