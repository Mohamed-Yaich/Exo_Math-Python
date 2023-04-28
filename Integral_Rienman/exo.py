import matplotlib.pyplot as plt
import time, numpy, math

def f(x):
    return numpy.exp(-x/10) * numpy.sin(x)



a, b = 1, 10
nb_points = 10000
step = (b-a)/nb_points

x_values, y_values = [], []

# 1
x_values = numpy.linspace(a, b, nb_points)
y_values = f(x_values)
for index_point in range(0, nb_points+1):
    numpy.append(x_values, a + index_point*step)
    numpy.append(y_values, f(a + index_point*step))

# 2
gradient = numpy.gradient(y_values, x_values)

# 3 
y_slice = slice(3000, 7000)
# print(y_values[y_slice])
sum_y_slice = sum(y_values[y_slice])/len(y_values[y_slice])
# print(sum_y_slice)

std_dev = numpy.std(y_values[y_slice])
# print(std_dev)

# 4

def f_x(x) :
    return ((numpy.exp(-x/10.0) + numpy.cos(x)) - ((0.1 * numpy.exp(-x/10.0)) + numpy.sin(x)))



def dichotomie(f, a, b):
    eps= 1e-6
    while (b - a) > eps:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

print(dichotomie(f_x , 0 , 3))
print(dichotomie(f_x , 3 , 6))
print(dichotomie(f_x , 6 , 10))

plt.figure(figsize=(10,6))
plt.plot(x_values, y_values)
plt.plot(x_values, gradient)
plt.show()