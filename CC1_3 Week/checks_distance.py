'it checks if two points in a cartesian is close or far from each other'

import math
CoordenadaX1 = float(input("Coordenada x1:"))
CoordenadaY1 = float(input("Coordenada y1:"))
CoordenadaX2 = float(input("Coordenada x2:"))
CoordenadaY2 = float(input("Coordenada y2:"))
Distancia = math.sqrt((CoordenadaX1-CoordenadaX2)**2+(CoordenadaY1-CoordenadaY2)**2)
if Distancia >= 10:
  print("longe")
else:
  print("perto")
