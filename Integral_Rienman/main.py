import matplotlib.pyplot as plt
import math 

a , b ,  = 1 , 5 
number_of_points = 40
step = (b-a) / number_of_points

x_values , y_values  = [] , []

def f(x) :
    return math.exp(3*x)

for index_step in range(0 , number_of_points + 1):
    x_values.append(a + index_step*step)
    y_values.append(f(a + index_step*step))

somme_rienman = sum(y_values)
somme_rienman = somme_rienman * step 

print(somme_rienman)

plt.figure(figsize=(10 , 10)) # Taille de la fenêtre
plt.plot(x_values , y_values , "x") # On récupère les donées des listes
plt.plot(somme_rienman)
plt.show() # Afficher le graphe