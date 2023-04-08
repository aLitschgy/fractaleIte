import random as rdm
import matplotlib.pyplot as plt
from Point import *


N_ITERATION = 5000
tailleImage = (800, 600)
margin = 20

triangle = Point.getABCfull(tailleImage, margin)
currentPoint = Point.random_point_in_triangle(triangle[0], triangle[1], triangle[2])

fig, ax = plt.subplots()
ax.plot([p.x for p in triangle], [p.y for p in triangle] , 'k.')

for i in range(N_ITERATION):

    # Afficher le point sur le graphique
    ax.plot(currentPoint.x, currentPoint.y, 'k.')

    # Actualiser le graphique
    plt.draw()
    plt.pause(0.001)

    pointTri = triangle[rdm.randint(0, 2)]
    currentPoint = Point.milieu(currentPoint, pointTri)
