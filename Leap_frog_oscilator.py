import numpy as np
import matplotlib.pyplot as plt

# parametry oscilátoru
m = 1
k = 1
omega = np.sqrt(k/m)

# počáteční podmínky a časový krok
x0 = 1
v0 = 0
dt = 1
t_max = 250

# ukládací pole
t_values = np.arange(0.0, t_max, dt)
x_values = np.zeros_like(t_values)
v_values = np.zeros_like(t_values)
E_values = np.zeros_like(t_values)

# počáteční podmínky
x_values[0] = x0
v_values[0] = v0
E_values[0] = 0.5 * m * v0**2 + 0.5 * k * x0**2

for i in range(1, len(t_values)):
    # aktualizace polohy
    x_half = x_values[i-1] + 1/2 * v_values[i-1] *dt
    # vypočet síly
    F = -k * x_half
    # aktualizace rychlosti, polohy a energie
    v_values[i] = v_values[i-1] + (F / m) * dt
    x_values[i] = x_half + 1/2 * v_values[i] * dt
    E_values[i] = 1/2 * m * v_values[i]**2 + 1/2 * k * x_values[i]**2

print(E_values)

# Vykreslení výsledků
plt.figure(figsize=(10, 5))
plt.plot(t_values, x_values, label='Poloha')
plt.plot(t_values, v_values, label='Rychlost')
plt.xlabel('Čas')
plt.ylabel('Hodnota')
plt.title('Poloha a rychlost harmonického oscilátoru')
plt.legend()
plt.grid(True)
plt.show()

# Vykreslení závislosti celkové energie na čase
plt.figure(figsize=(10, 5))
plt.plot(t_values, E_values, label='Celková energie')
plt.xlabel('Čas')
plt.ylabel('Energie')
plt.title('Závislost celkové energie na čase pro krok 1')
plt.ylim(0.47, 0.65)
plt.legend()
plt.grid(True)
plt.show()



