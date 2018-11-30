import mahotas
import numpy as np
from matplotlib import pyplot as plt
import random
from matplotlib import colors as c

nuclear = mahotas.imread('data/flower.png')
nuclear = nuclear[:,:,0]
nuclear = mahotas.gaussian_filter(nuclear, 1.)
threshed  = (nuclear > nuclear.mean())
distances = mahotas.stretch(mahotas.distance(threshed))
Bc = np.ones((9,9))

maxima = mahotas.morph.regmax(distances, Bc=Bc)
spots,n_spots = mahotas.label(maxima, Bc=Bc)
surface = (distances.max() - distances)
areas = mahotas.cwatershed(surface, spots)
areas *= threshed

plt.jet()

rmap = c.ListedColormap(np.random.rand(256,3))

plt.imshow(areas, cmap=rmap)
plt.show()
