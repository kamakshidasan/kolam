import pylab as p
import numpy as np
import mahotas
import cv2

im = cv2.imread("data/flower.png", cv2.IMREAD_GRAYSCALE)
dmap = mahotas.distance(im)
p.imshow(dmap, cmap="coolwarm")
#p.axis('off')
#p.savefig('scalar.png', bbox_inches='tight', pad_inches=0)
p.show()
