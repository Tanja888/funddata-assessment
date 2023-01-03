import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0.0, 1.0

x = np.linspace(-3, 3.0, 100000)

y = 1.0/np.sqrt(2 * np.pi * sigma**2) * np.exp(-((x-mu)**2/(2*sigma**2)))

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(x, y, color='red', linewidth=1)
ax.axvline(x=1, color='green', ymax=0.58, linewidth=.8, linestyle='--')
ax.axvline(x=0, color='green', ymax=0.95, linewidth=.8, linestyle='--')
ax.axvline(x=2, color='green', ymax=0.16, linewidth=.8, linestyle='--')
ax.axvline(x=3, color='green', ymax=0.04, linewidth=.8, linestyle='--')
ax.axvline(x=-1, color='green', ymax=0.58, linewidth=.8, linestyle='--')
ax.axvline(x=-2, color='green', ymax=0.16, linewidth=.8, linestyle='--')
ax.axvline(x=-3, color='green', ymax=0.04, linewidth=.8, linestyle='--')


ax.axhline(y=0.25, xmin=0.5, xmax=0.64, color='black', linewidth=0.4)
ax.text(x=0.3, y=0.26, s='34%');

ax.axhline(y=0.25, xmin=0.36, xmax=0.5, color='black', linewidth=0.4)
ax.text(x=-0.6, y=0.26, s='34%');

ax.axhline(y=0.1, xmin=0.25, xmax=0.35, color='black', linewidth=0.4)
ax.text(x=-1.45, y=0.11, s='13.5%');

ax.axhline(y=0.1, xmin=0.65, xmax=0.75, color='black', linewidth=0.4)
ax.text(x=1.1, y=0.11, s='13.5%');

ax.axhline(y=0.00, xmin=0.05, xmax=0.2, color='black', linewidth=0.4)

ax.text(x=-2.4, y=0.005, s='2.35%');

ax.set_title('Normal distribution');

plt.show()