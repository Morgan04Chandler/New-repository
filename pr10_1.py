import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 200)
# x^1/2 = sqrt x
y = np.sqrt(x) * np.sin(10 * x)

plt.plot(x, y, label='y = sqrt(x)*sin(10x)', color='blue', linewidth=2, linestyle='-',)

plt.title('Графік функції y = sqrt(x) * sin(10x)')
plt.xlabel('x', fontsize=10, color='red')
plt.ylabel('y', fontsize=10, color='green')

plt.legend()
plt.grid(True)
plt.show()