import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Definimos la función
def f(x):
    return 4 * x - 5

# Configuramos la figura y los ejes
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)  # Ajustamos el espacio para los sliders

# Definimos el rango de x
x = np.linspace(1, 3, 400)
y = f(x)

# Graficamos la función
line, = plt.plot(x, y, label='f(x) = 4x - 5')
plt.axvline(x=2, color='r', linestyle='--', label='x = 2')
L = f(2)
plt.axhline(y=L, color='g', linestyle='--', label=f'L = {L}')

# Dibujamos el rectángulo alrededor del punto (2, L)
rect = plt.fill_between([2 - 1, 2 + 1], L - 1, L + 1, color='yellow', alpha=0.3, label='ε y δ')[0]

# Configuramos los límites del gráfico
plt.xlim(1, 3)
plt.ylim(L - 2, L + 2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Concepto de Límite: f(x) = 4x - 5 cuando x tiende a 2')
plt.legend()
plt.grid(True)

# Creamos los sliders para epsilon y delta
ax_epsilon = plt.axes([0.2, 0.15, 0.65, 0.03])  # Posición del slider de epsilon
ax_delta = plt.axes([0.2, 0.1, 0.65, 0.03])    # Posición del slider de delta

epsilon_slider = Slider(ax_epsilon, 'ε', 0.1, 2.0, valinit=1.0)
delta_slider = Slider(ax_delta, 'δ', 0.1, 2.0, valinit=1.0)

# Función para actualizar el gráfico cuando se mueven los sliders
def update(val):
    epsilon = epsilon_slider.val
    delta = delta_slider.val
    
    # Actualizamos el rectángulo
    rect.set_xy([[2 - delta, L - epsilon],
                [2 + delta, L - epsilon],
                [2 + delta, L + epsilon],
                [2 - delta, L + epsilon]])
    
    # Redibujamos la figura
    fig.canvas.draw_idle()

# Conectamos los sliders a la función de actualización
epsilon_slider.on_changed(update)
delta_slider.on_changed(update)

# Mostramos la gráfica
plt.show()