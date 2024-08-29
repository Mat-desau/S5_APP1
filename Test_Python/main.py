import numpy as np
import matplotlib.pyplot as plt

# Paramètres du robot
l1 = 25  # Longueur du bras OB (en cm)
l2 = 25  # Longueur du bras BA (en cm)
omega_OB = 25  # Vitesse angulaire du bras OB en rad/s

# Discrétisation de l'angle theta
theta = np.linspace(0, np.pi/3, 100)  # theta varie de 0 à pi/3

# Calcul de phi à partir de la relation sin(theta) = (l2/l1) * sin(phi)
phi = np.arcsin((l1/l2) * np.sin(theta))

# Calcul des vitesses angulaires
dot_theta = np.full_like(theta, omega_OB)  # omega_OB est constant
dot_phi = np.gradient(phi) / np.gradient(theta) * dot_theta  # dérivée de phi par rapport à theta

# Calcul des vitesses en x
v_xA = -l1 * np.sin(theta) * dot_theta - l2 * np.sin(phi) * dot_phi

# Calcul des accélérations en x
ddot_theta = np.zeros_like(theta)  # Accélération angulaire de OB est 0 car omega_OB est constant
ddot_phi = np.gradient(dot_phi) / np.gradient(theta) * dot_theta

a_xA = -l1 * (ddot_theta * np.sin(theta) + dot_theta**2 * np.cos(theta)) \
       - l2 * (ddot_phi * np.sin(phi) + dot_phi**2 * np.cos(phi))

# Création des graphiques
plt.figure(figsize=(12, 8))

# Graphique de la vitesse
plt.subplot(2, 1, 1)
plt.plot(theta, v_xA, label='v_xA')
plt.title('Vitesse linéaire en fonction de theta')
plt.xlabel('theta (rad)')
plt.ylabel('Vitesse v_xA (cm/s)')
plt.grid(True)
plt.legend()

# Graphique de l'accélération
plt.subplot(2, 1, 2)
plt.plot(theta, a_xA, label='a_xA', color='r')
plt.title('Accélération linéaire en fonction de theta')
plt.xlabel('theta (rad)')
plt.ylabel('Accélération a_xA (cm/s^2)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
