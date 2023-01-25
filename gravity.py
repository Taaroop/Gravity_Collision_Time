from decimal import *
import matplotlib.pyplot as plt

M = 1.989E30
v_M = 0
radius_1 = 6.9634E8

m = 5.972E24
v_m = 0
radius_2 = 6.3781E6

d = 148.6E9

G = 6.67384 * (10**-11) # Gravity is a very weak force

dt = 1
t_elapsed = 0
collision = False

li_distance = [d]
li_time = [0]

def displacement(u, a, t):
    return u*t + 0.5*a*(t**2)

def v_new(u, a, t):
    return u + a*t

while collision == False:
    acc_M = (G*m)/(d**2)
    acc_m = (G*M)/(d**2)
    
    dis_M = displacement(v_M, acc_M, dt)
    dis_m = displacement(v_m, acc_m, dt)
    
    v_M = v_new(v_M, acc_M, dt)
    v_m = v_new(v_m, acc_m, dt)
    
    d = d - (dis_M + dis_m)
    t_elapsed += dt
    
    li_distance.append(d)
    li_time.append(t_elapsed)
    
    if d <= radius_1 + radius_2:
        collision = True

print("Simulation time:", t_elapsed, "seconds")
plt.plot(li_time, li_distance)
