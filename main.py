import random as rdm
import matplotlib.pyplot as plt
from tqdm import tqdm
from Point import *


N_ITERATION = 100000
tailleImage = (4000, 3000)
margin = 50

triangle = Point.getABCfull(tailleImage, margin)
currentPoint = Point.random_point_in_triangle(triangle[0], triangle[1], triangle[2])

x = []
y = []

with tqdm(total=N_ITERATION, desc='Calcul des points') as pbar:
    for i in range(N_ITERATION):

        # Enregistrer le point
        x.append(currentPoint.x)
        y.append(currentPoint.y)

        pointTri = triangle[rdm.randint(0, 2)]
        currentPoint = Point.milieu(currentPoint, pointTri)
        pbar.update(1)

fig = plt.figure(figsize=(4, 3), dpi=400)
ax = fig.add_subplot(111)
ax.plot(x, y, marker='o',ms=72./fig.dpi, mew=0, color='black', linestyle="", lw=0)
ax.set_title("Fractale iterrative")
ax.set_xlim(0,tailleImage[0])
ax.set_ylim(0,tailleImage[1])
fig.tight_layout()
fig.savefig("output.jpg")
