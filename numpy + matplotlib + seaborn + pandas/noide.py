import matplotlib.pyplot as plt
from math import sin
import numpy as np


np.random.seed(58008)


def normalise(func):
    o = []
    for p in func:
        res = median(p)
        res = easy_mean(res)

        o.append(res)
    return o


def noised(func, k=0.3, fitob=0.03):
    o = []
    for p in func:
        r = (np.random.random()*2-1) * k

        # Standard noise and random emissions
        if np.random.random() < fitob: c = p + r*7
        else: c = p + r

        o.append(c)
    return o


def arith_mean(f, buffer_size=10):
    # Creating buffer
    if not hasattr(arith_mean, "buffer"):
        arith_mean.buffer = [f] * buffer_size

    # Move buffer to actually values ( [0, 1, 2, 3] -> [1, 2, 3, 4] )
    arith_mean.buffer = arith_mean.buffer[1:]
    arith_mean.buffer.append(f)

    # Calculation arithmetic mean
    mean = 0
    for e in arith_mean.buffer: mean += e
    mean /= len(arith_mean.buffer)

    return mean


def easy_mean(f, s_k=0.2, max_k=0.9, d=1.5):
    # Creating static variable
    if not hasattr(easy_mean, "fit"):
        easy_mean.fit = f

    # Adaptive ratio
    k = s_k if (abs(f - easy_mean.fit) < d) else max_k

    # Calculation easy mean
    easy_mean.fit += (f - easy_mean.fit) * k

    return easy_mean.fit


def median(f):
    # Creating buffer
    if not hasattr(median, "buffer"):
        median.buffer = [f] * 3

    # Move buffer to actually values ( [0, 1, 2] -> [1, 2, 3] )
    median.buffer = median.buffer[1:]
    median.buffer.append(f)

    # Calculation median
    a = median.buffer[0]
    b = median.buffer[1]
    c = median.buffer[2]
    middle = max(a, c) if (max(a, b) == max(b, c)) else max(b, min(a, c))

    return middle


def kalman(f, q=0.25, r=0.7):
    if not hasattr(kalman, "Accumulated_Error"):
        kalman.Accumulated_Error = 1
        kalman.kalman_adc_old = 0

    if abs(f-kalman.kalman_adc_old)/50 > 0.25:
        Old_Input = f*0.382 + kalman.kalman_adc_old*0.618
    else:
        Old_Input = kalman.kalman_adc_old

    Old_Error_All = (kalman.Accumulated_Error**2 + q**2)**(1/2)
    H = Old_Error_All**2/(Old_Error_All**2 + r**2)
    kalman_adc = Old_Input + H * (f - Old_Input)
    kalman.Accumulated_Error = ((1 - H)*Old_Error_All**2)**(1/2)
    kalman.kalman_adc_old = kalman_adc

    return kalman_adc

# Generals variables
length = 30
resolution = 20

# Creating arrays with graphic
sinus_g = [sin(i / resolution) for i in range(length * resolution)]

square_g = [(1 if p > 0 else -1) for p in sinus_g]

triangle_g = []
t = -1
for _ in range(length * resolution):
    t = t+0.035 if t < 1 else -1
    triangle_g.append(t)

# Output of graphs
graphics = [sinus_g, square_g, triangle_g]

fig, axs = plt.subplots(3, 1)

for i in range(len(graphics)):
    noised_f = noised(graphics[i])

    axs[i].plot(noised_f, color='blue')
    axs[i].plot(graphics[i], color='black')
    #axs[i].plot(normalise(noised_f), linewidth=3, color='red')

    axs[i].set_ylim([-2, 2]), axs[i].set_xlim([0, length*resolution]),
    axs[i].set_yticklabels([]), axs[i].set_xticklabels([])

plt.show()