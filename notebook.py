from random import *
import math as m
import cv2
import numpy as np
"""
Width = 600
Height = 600

window = 255*np.ones((Height,Width,3), dtype = np.uint8)

cv2.line(window,(300,0),(300,600),(255,0,0),3)
cv2.line(window,(0,300),(600,300),(255,0,0),3)

cv2.rectangle(window,(10,10),(20,20),(0,255,0),-1)
cv2.rectangle(window,(570,570),(590,590),(0,255,0),-1)

H = [[0]]*4
H1 = [(0,0)]
H2 = [(0,0)]
H3 = [(0,0)]
H4 = [(0,0)]

D = {}
zone_num = 4
for j in range (zone_num):
    D[j] = [(300,300)]

for i in range(6):
    x = randint(50,550)
    y = randint(50,550)

    cv2.circle(window, (x,y), 7,(0,0,255),-1)

    # ------------- desplazamiento del centro (0,0) - (300,300) --------
    x1 = (300 - x)
    y1 = (300 - y)
    x2 = (x - 300)
    y2 = (y - 300)

    z1 = y1/x2
    z2 = y1/x1
    z3 = y2/x1
    z4 = y2/x2

    ang = 0

    if x >= 300 and y <= 300:   # I cuadrante
        ang = m.degrees((m.atan(z1)))
        print((x2,y1))


    if x < 300 and y <= 300:    # II cuadrante
        ang = m.degrees((m.atan(z2)))
        ang += 90
        print((x1,y1))

    if x < 300 and y > 300:    # III cuadrante
        ang = m.degrees((m.atan(z3)))
        ang += 180
        print((x1,y2))

    if x >= 300 and y > 300:  # IV cuadrante
        ang = m.degrees((m.atan(z4)))
        ang += 270  
        print((x2,y2))

    theta = 360/zone_num

    for i in range (0,zone_num):
        if ang >= i*theta and ang < (i+1)*theta:
            D[i].append((x,y))
        
    print("angulo = ",ang)

cv2.imshow('Prueba',window)
cv2.waitKey(0)


for key in D:
    print(key ," : ",D[key])



    # if x > 300 and y < 300:
    #     #H1.append((x,y))
    #     #H[0].append((x,y))

    # if x <= 300 and y < 300 :
    #     #H2.append((x,y))
    #     #H[1].append((x,y))
    # if x <= 300 and y >= 300:
    #     #H3.append((x,y))
    #     #H[2].append((x,y))
    # if x > 300 and y >= 300:
        #H4.append((x,y))
        #H[3].append((x,y))
    
#H.append(H1)
#H.append(H2)

                    # 0           1            2           3
Clients  = {0  :  [(300, 300), (458, 300), (467, 180), (431, 217)]}

            #  0           3            2            1
Clients2 = [(300, 300), (431, 217), (467, 180), (458, 300)]


[[0  0  0  1],
 [1  0  0  0],
 [0  1  0  0],
 [0  0  1  0]]



num_Clients = len(Clients.get(0))
Adjacency_Matrices = {}
Matrix = np.zeros((num_Clients,num_Clients))#[[0]*num_Clients]*num_Clients
Adjacency_Matrices[0] = Matrix
for key in Adjacency_Matrices:
    print(key, " : ", Adjacency_Matrices[key])

Aux = []

for i in range(num_Clients):
    for j in range(num_Clients):
        if Clients2[i] == Clients.get(0)[j]:
            Aux.append(j)
            break
Aux.append(0)
print("Aux = ",Aux)

#Adjacency_Matrices.fromkeys([0], )
for i in range(len(Aux)-1):
    fil = Aux[i]
    col = Aux[i+1]
    Matrix[fil][col] = 1
    
Adjacency_Matrices.fromkeys([0],Matrix)
#Matrix[Aux[-1]][Aux[0]]
for key in Adjacency_Matrices:
    print(key, " : ", Adjacency_Matrices[key])

"""
print(m.ceil(3/5))