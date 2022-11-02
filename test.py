import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm



background = plt.imread("backgroundHeatmap.png")

form = np.shape(background)
print(form)

print("testshape: " + str(np.shape(background)[1]))

# print(background)

print("shape 0: " + str(form[0]))
print("shape 1: " + str(form[1]))
print("shape 2: " + str(form[2]))

print("x Eintrag background" + str(len(background[0])))

print("y Eintrag background" + str(len(background[1])))

print("3te Dimension" + str(len(background[2])))

"""
hsv_modified = cm.get_cmap('hsv', 256)
# newcmp = ListedColormap(hsv_modified(np.linspace(0.3, 0.7, 256)))

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
"""
# plt.figure(figsize=(7,6))
# plt.pcolormesh(data, cmap="inferno")
# plt.colorbar()
# plt.imshow(background)
# plt.show()