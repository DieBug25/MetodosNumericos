import numpy as np 
import math
from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7]
y = [0.5,1.5,3.5,6,10,14.5,19.5]
sumXY
sumX2 
sumX3
sumX4
sumX5
sumX6
sumatoriaX
sumatoriaY
sumX2Y
sumX3Y
promY
st
sr
sy
syx
r
    
for i in range(len(x)):
        
    sumXY += float(x[i])*float(y[i])
    sumX2 += pow(float(x[i]),2)
    sumX3 += pow(float(x[i]),3)
    sumX4 += pow(float(x[i]),4)
    sumX5 += pow(float(x[i]),5)
    sumX6 += pow(float(x[i]),6)
    sumatoriaX += float(x[i])
    sumatoriaY += float(y[i])
    sumX2Y += pow(float(x[i]),2)*float(y[i])
    sumX3Y += pow(float(x[i]),3)*float(y[i])

a = np.array([[len(x),sumatoriaX,sumX2,sumX3],[sumatoriaX,sumX2,sumX3, sumX4],[sumX2,sumX3,sumX4,sumX5],[sumX3,sumX4,sumX5,sumX6]])
b = np.array([sumatoriaY,sumXY,sumX2Y,sumX3Y])
print("Matriz a:")
print(a)
print("Array b:")
print(b)
gauss = np.linalg.solve(a,b)
print("a0",gauss[0])
print("a1",gauss[1])
print("a2",gauss[2])
print("a3",gauss[3])

promY = sumatoriaY/(len(y))

for i in range(len(x)):
    st += pow(float(y[i])-promY,2)
    sr += pow(float(y[i])-gauss[0]-(gauss[1]*float(x[i]))-pow(float(x[i]),2)*gauss[2]-pow(float(x[i]),3)*gauss[3],2)

sy =  math.sqrt(st/(len(x)-1))
syx = math.sqrt(sr/(len(x)-3))
r = math.sqrt((st-sr)/st)*100

rta.append(gauss[0])
rta.append(gauss[1])
rta.append(gauss[2])
rta.append(gauss[3])
rta.append(sy)
rta.append(syx)
rta.append(r)