import numpy as np
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(-4, 4), ylim=(0, 16))

x = np.arange(-4,5,0.1)
ax.plot(x,x**2)
ax.plot(x,-x**2+16)
plt.title('Mechanical Energy')
plt.axis('off')
plt.legend()

plt.axvline(0, 0, 16, color='gray')
plt.axhline(0, -4, 4, color='gray')
plt.axhline(16, -4, 4, color='gray')

dot_1, = plt.plot([], [], 'ro')
dot_2, = plt.plot([], [], 'ro')

def animate(frame):
    dot_1.set_data(frame, frame**2)
    dot_2.set_data(frame, -frame**2+16)
    return dot_1

ani = FuncAnimation(fig, animate, frames=np.arange(-4, 4, 0.01), interval=5)

plt.show()
