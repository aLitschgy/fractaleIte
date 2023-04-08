import random

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def milieu(A, B):
        return Point((A.x+B.x)/2, (A.y+B.y)/2)

    def getABCfull(tailleImage, margin):
        """
        Génère 3 sommets d'un triangle qui rempli au mieux l'image
        """

        A = Point(margin,margin)
        B = Point(tailleImage[0], margin)
        C = Point(tailleImage[0]/2, tailleImage[1]-margin)
        return A, B, C

    def toString(self):
        return "Point : (" + str(self.x) + ", " + str(self.y) + ");"

    def random_point_in_triangle(v1, v2, v3):
        """
        Génère un point aléatoire dans le triangle défini par les 3 sommets v1, v2 et v3.
        """
        # Calcul des vecteurs reliant les sommets
        v12 = Point(v2.x-v1.x, v2.y-v1.y)
        v23 = Point(v3.x-v2.x, v3.y-v2.y)
        v31 = Point(v1.x-v3.x, v1.y-v3.y)

        # Calcul de l'aire du triangle
        triangle_area = abs(v12.x*v31.y - v12.y*v31.x)/2.0

        # Génération de points aléatoires jusqu'à ce que l'un d'entre eux soit à l'intérieur du triangle
        while True:
            # Génère des coordonnées aléatoires dans le rectangle englobant le triangle
            x = random.uniform(min(v1.x, v2.x, v3.x), max(v1.x, v2.x, v3.x))
            y = random.uniform(min(v1.y, v2.y, v3.y), max(v1.y, v2.y, v3.y))

            # Vérifie si le point est à l'intérieur du triangle en calculant l'aire des sous-triangles
            # formés par le point et les sommets du triangle
            sub_triangle1_area = abs(v12.x*(y-v1.y) - v12.y*(x-v1.x))/2.0
            sub_triangle2_area = abs(v23.x*(y-v2.y) - v23.y*(x-v2.x))/2.0
            sub_triangle3_area = abs(v31.x*(y-v3.y) - v31.y*(x-v3.x))/2.0

            # Si la somme des aires des sous-triangles est égale à l'aire du triangle,
            # le point est à l'intérieur du triangle et peut être retourné
            if abs(triangle_area - sub_triangle1_area - sub_triangle2_area - sub_triangle3_area) < 1e-6:
                return Point(x, y)