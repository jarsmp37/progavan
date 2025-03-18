import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Definir la función de la parábola
def parabola(a, h, k, x):
    return a * (x - h)**2 + k

# Configurar la figura y los ejes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.4)  # Ajustar espacio para los sliders

# Rango de x
x = np.linspace(-10, 10, 500)

# Parámetros iniciales
a0, h0, k0 = 1, 0, 0

# Graficar la parábola inicial
l, = plt.plot(x, parabola(a0, h0, k0, x), lw=2)
plt.title('Parábola Interactiva')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-10, 10)
plt.xlim(-10, 10)

# Crear sliders
ax_a = plt.axes([0.2, 0.25, 0.6, 0.03])  # Posición del slider a
ax_h = plt.axes([0.2, 0.20, 0.6, 0.03])  # Posición del slider h
ax_k = plt.axes([0.2, 0.15, 0.6, 0.03])  # Posición del slider k

slider_a = Slider(ax_a, 'a', -5, 5, valinit=a0)
slider_h = Slider(ax_h, 'h', -5, 5, valinit=h0)
slider_k = Slider(ax_k, 'k', -5, 5, valinit=k0)

# Función para actualizar la gráfica cuando los sliders cambian
def update(val):
    a = slider_a.val
    h = slider_h.val
    k = slider_k.val
    l.set_ydata(parabola(a, h, k, x))
    fig.canvas.draw_idle()

# Conectar los sliders a la función de actualización
slider_a.on_changed(update)
slider_h.on_changed(update)
slider_k.on_changed(update)

# Mostrar la gráfica
plt.show()