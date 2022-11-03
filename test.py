import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable


background = plt.imread("backgroundHeatmap.png")

shape = np.shape(background)

colormap = mpl.colormaps['YlOrRd']  # type: ignore
newcolors = colormap(np.linspace(0, 0.7, 256))
cmap = cm.get_cmap("YlOrRd", 100)
white = np.array([1, 1, 1, 1])
newcolors[:25, :] = white

# newcmap = ListedColormap(cmap(np.linspace(0, 0.7, 100)))  # type: ignore
newcmap = ListedColormap(newcolors)  # type: ignore
# Farbe "YlOrRd"
# newcmap = mpl.colormaps['YlOrRd']  # type: ignore

data = np.random.randint(low=0, high=500, size=(shape[0], shape[1]))
#create colormap



fig = plt.figure(figsize=(7,6))
ax = plt.gca()
# plt.imshow(background)
plt.imshow(background)
plt.pcolormesh(data, alpha=0.6, cmap=newcmap)


# Calculate (height_of_image / width_of_image)
# im_ratio = background.shape[0]/background.shape[1]

# plt.colorbar(fraction=0.047*im_ratio)

#-----------------------
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.25)

plt.colorbar(cax=cax)
#----------------------

plt.show()

