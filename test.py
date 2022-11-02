import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm



background = plt.imread("backgroundHeatmap.png")

shape = np.shape(background)
print(shape)
print(background)

hsv_modified = cm.get_cmap('hsv', 256)
newcmp = ListedColormap(hsv_modified(np.linspace(0.3, 0.7, 256)))

data = np.random.randint(low=0, high=256, size=(shape[0], shape[1]))
#create colormap
# newcmp = ListedColormap
# print(data)

fig = plt.figure(figsize=(7,6))
ax = fig.add_subplot()

ax.imshow(background)
plt.pcolormesh(data, alpha=0.1, cmap=newcmp)
plt.colorbar()

plt.show()

# plt.figure(figsize=(7,6))
# plt.pcolormesh(data, cmap="inferno")
# plt.colorbar()
# plt.imshow(background)
# plt.show()