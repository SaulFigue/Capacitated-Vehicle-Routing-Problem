from random import *                        # FOR GENERATE RANDOMS VALUES
import math as m                            # FOR MATH OPERATION (f(x),exp)
import numpy as np                          # FOR CREATE THE WINDOW VISUALIZATION
import cv2                                  # FOR VISUALAZE THE TSP
import matplotlib.pyplot as plt             # FOR EMPIRICAL ANALYSIS (in the future)

# ---------------------------------------------------------------------------------------------------------
# ------------------ RANDOMLY GENERATE A SOLUTION (AN ARRAY WITH THE A RANDOM ROAD) -----------------------
# ---------------------------------------------------------------------------------------------------------
def Current_Solution(number_cities):
    current_solution = []
    for i in range(number_cities):
        current_solution.append(i)            # Add elements from 0 to number of cities in an Array
    shuffle(current_solution)                 # Mix/shuffle the elements in the array
    return current_solution

# ---------------------------------------------------------------------------------------------------------
# --------------- RANDOMLY GENERATE POINTS (CITIES) IN AN AREA GIVEN BY WIDTH AND HEIGHT ------------------
# ---------------------------------------------------------------------------------------------------------
def Cities_Creation (width, height, number_cities):
    h1 = height//2
    w2 = width//2
    Cities = [(w2,h1)]
    for i in range(number_cities-1):
        axis_x = randint(50, width - 50)      # GENERATE A RANDON NUMBER FOR AXIS X
        axis_y = randint(50, height - 50)     # GENERATE A RANDON NUMBER FOR AXIS Y
        Cities.append((axis_x,axis_y))
    return Cities

# ---------------------------------------------------------------------------------------------------------
# ------------------- DEFINING THE COST FUNCTION (DISTANCE) FOR SOLVING THE TSP ---------------------------
# ---------------------------------------------------------------------------------------------------------
def Cost_function (Point_a, Point_b):
    delta_x = Point_a[0] - Point_b[0]
    delta_y = Point_a[1] - Point_b[1]
    Distance = m.sqrt(delta_x ** 2 + delta_y ** 2)   # Formula to calculate the distance btw two Points
    return Distance
    

def Total_Distance (Cities,current_solution):
    # print(current_solution)
    Total_distance = 0
    for i in range (len(Cities)):
        Point_a = current_solution[i]
        Point_b = current_solution[i-1]
        Total_distance += Cost_function (Cities[Point_a], Cities[Point_b])  # Total distance traveled through all cities
        
    return Total_distance

# ---------------------------------------------------------------------------------------------------------
# --------------------- CHOOSING A NEW SOLUTION (SWAPING TWO VALUES IN THE ARRAY) -------------------------
# ---------------------------------------------------------------------------------------------------------
def Neighbour_Solution(Current_Solution):
    New_Solution = Current_Solution[:]
    # --- Randomly choose two positions of the solution road (equivalents to the cities array position) ----
    swap_a = randint(1,len(Current_Solution)-1)
    swap_b = randint(1,len(Current_Solution)-1)
    while swap_b == swap_a:
        swap_b = randint(1,len(Current_Solution)-1)
    # ------- Exchanging/Swaping those positions in the road (Swaping the cities) ----------
    New_Solution[swap_a] , New_Solution[swap_b] = New_Solution[swap_b] , New_Solution[swap_a]
    return New_Solution

# ---------------------------------------------------------------------------------------------------------
# ----------------------------- VISUALIZTION FOR THE TSP SOLVED BY SAA ------------------------------------
# ---------------------------------------------------------------------------------------------------------

def Visualization(Width, Height, Cities,Current_Solution,Initial_Temperature,Initial_Cost_Function_Value):
    # --------------------------- Creating the visualization window -----------------------------
    Window = 255*np.ones((Height,Width,3), dtype = np.uint8)

    # ----------------------- Ploting the road between the nodes (cities) -----------------------
    for i in range (len(Cities)):
        Point_a = Cities[Current_Solution[i]]
        Point_b = Cities[Current_Solution[i-1]]
        cv2.line(Window, Point_a, Point_b, (255,0,0),3)

    # ------------------------ Ploting the nodes (cities) with a circle shape -------------------
    for city in Cities:
        axis_x = city[0]
        axis_y = city[1]
        # cv2.circle(Window, PointLocation, Radious, Color BGR, Linewidth / Fill = -1) ----  FORMAT
        cv2.circle(Window,(axis_x,axis_y),7,(0,0,255),-1)

    # ------------------------ Ploting a depot node (square) in the center ----------------------
    h1 = Height//2 - 10
    w1 = Width//2 - 10
    h2 = Height//2 + 10
    w2 = Width//2 + 10
    #cv2.rectgl("ventana,esq-iz-coor,esq-der-coor,color,rellenar")
    cv2.rectangle(Window,(h1,w1),(h2,w2),(0,0,255),-1)

    
    # ---------------- Ploting the basic datas (Temp change and Distance traveled) --------------
    
    # cv2.putText(Window,"Text",Location in window,Font,Font Size, Color BGR, Linewidth, Line Type) ----  FORMAT
    cv2.putText(Window,f"Temperature Change: ",(50,40),1,0.9,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(Window,f"Total Distance: ",(300,40),1,0.9,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(Window, f" {Initial_Temperature:.2f}", (210, 40), 1, 0.9, (0,0,0),1,cv2.LINE_AA)
    cv2.putText(Window, f" {Initial_Cost_Function_Value:.2f}", (410, 40), 1, 0.9, (0,0,0),1,cv2.LINE_AA)

    cv2.imshow('TSP Solution - Visualization', Window)      #Title of the Window, show window 
    cv2.waitKey(32)          # Time in "ms" to show the frames

    # if k == ord('q'):
    #     cv2.destroyAllWindows()
    # elif k == ord('c'):
    #     cv2.waitKey(5)
    
    # if Initial_Temperature == 999.00:
    #     cv2.imshow('Initial TSP Solution - Visualization', Window2)
    #     cv2.waitKey(0)
        #cv2.imwrite('InitialGraphic3.jpg',Window)

    #if Initial_Temperature < 0.01:
        #cv2.imwrite('FinalGraphic3.jpg',Window)
        ##cv2.destroyAllWindows()


# ---------------------------------------------------------------------------------------------------------
# ------------------------------------ SIMULATED ANNEALING ALGORITHM --------------------------------------
# ---------------------------------------------------------------------------------------------------------

# -------------------------------------------  Pseudocode--------------------------------------------------

#   def SAA(Cities,Temp0,Alpha_rate)
#       Generate initial candidate solution S <-- S0 = [road follow]
#       Evaluate the solution with the Cost Function // f(x)
#       While Temp0 > 0 do:
#           Pick a random Neighbour Snew
#           if f(Snew) < f(S) then:
#               S <-- Snew
#               f(S) <-- f(Snew) // Accept the new solution
#           elif f(Snew) >= f(S) and exp(-Delta_f /Temp0) > random(0,1):
#               S <-- Snew
#               f(S) <-- f(Snew) // Accept the new solution
#          Temp0 = Alpha_rate*Temp0 // Update Temperature (Alpha_rate is between(0,1))

# ----------------------------------------------- Code ----------------------------------------------------

def Simulated_Annealing (Width, Height, Number_Cities, Initial_Temperature, Final_Temperature,Cooling_Rate):
    Cities = Cities_Creation(Width , Height , Number_Cities)    # podria obtener las ciudades fuera de esta funcion e ingresarla como parametro
    Solution = Current_Solution(Number_Cities)
    Initial_Cost_Function_Value = Total_Distance(Cities, Solution)
    while Initial_Temperature > Final_Temperature:              # podria colocar directamente (0 o 1) en vez de Final temperature
        New_Solution = Neighbour_Solution(Solution)
        New_Cost_Function_Value = Total_Distance(Cities,New_Solution)
        if New_Cost_Function_Value < Initial_Cost_Function_Value:
            Solution = New_Solution
            Initial_Cost_Function_Value = New_Cost_Function_Value
        else:
            Probability_criteria = m.exp(-(New_Cost_Function_Value - Initial_Cost_Function_Value)/
                                          Initial_Temperature)
            if Probability_criteria > uniform(0,1):
                Solution = New_Solution
                Initial_Cost_Function_Value = New_Cost_Function_Value
        Initial_Temperature *= Cooling_Rate
        Visualization(Width, Height, Cities,Solution,Initial_Temperature,Initial_Cost_Function_Value)

# ---------------------------------------------------------------------------------------------------------            
# ------------------------------------------- BASIC DATAS -------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
Width = 600
Height = 600
Number_Cities = 15
Initial_Temperature = 1000
Final_Temperature = 0
Cooling_Rate = 0.999

# ---------------------------------------------------------------------------------------------------------
# --------------------------------------CALL THE MAIN ALGORITHM -------------------------------------------
# ---------------------------------------------------------------------------------------------------------
Simulated_Annealing(Width, Height, Number_Cities, Initial_Temperature, Final_Temperature, Cooling_Rate)

