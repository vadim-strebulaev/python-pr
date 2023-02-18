import matplotlib.pyplot as plt
import numpy as np

digit = 8
fig, ax = plt.subplots()
if digit == 8:
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.sin(x - np.pi / 2)
    ax.fill_between(x, y1, y2, color='gray')
    ax.fill_between(x, -y1, -y2, color='gray')
# Add additional cases for other digits
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
plt.show()
