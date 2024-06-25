import random
import matplotlib.pyplot as plt

tableau1 = list(range(1, 1001))
random.shuffle(tableau1)

def tri_par_bulle(tableau):
    n = len(tableau)
    for i in range(n - 1):
        echange_effectue = False
        for j in range(n - 1 - i):
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
                echange_effectue = True
        if not echange_effectue:
            break

tableau1_avant = tableau1.copy()

print("Tableau mélangé:", tableau1_avant)

tri_par_bulle(tableau1)

print("Tableau trié:", tableau1)

tableau2 = list(range(1, 1001))

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(tableau1_avant, label='Tableau mélangé avant tri', color='blue')
plt.title("Tableau mélangé avant tri")
plt.xlabel("Index")
plt.ylabel("Valeur")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(tableau1, label='Tableau mélangé après tri', color='blue')
plt.plot(tableau2, label='Tableau déjà trié', color='green')
plt.title("Tableaux après tri")
plt.xlabel("Index")
plt.ylabel("Valeur")
plt.legend()

plt.tight_layout()
plt.show()



