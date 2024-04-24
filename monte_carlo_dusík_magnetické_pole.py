import numpy as np
import matplotlib.pyplot as plt
import math

# Konstanty
T = 300  # teplota v K
g = 9.81  # gravitační zrychlení v m/s^2
Delta_z = 30 * 1000  # zkušební pohyb v metrech
iterations_mixing = 20  # počet kroků míchání
iterations_measurement = 10000  # počet kroků měření
z_initial = 0  # počáteční výška


# Funkce pro výpočet potenciálu
def potential_energy(z):
    if z < 0:
        return np.inf
    else:
        return g * z


# Inicializace
z = z_initial
accepted_configurations = 0
height_counts = {'low': 0, 'high': 0}

# Míchání
for i in range(iterations_mixing):

    z_trial = z + potential_energy(np.random.uniform(-1, 1)) * Delta_z
    if not math.isinf(z_trial):
        delta_E = potential_energy(z_trial) - potential_energy(z)
        print(delta_E)

        if delta_E <= 0 or np.exp(-delta_E / (T * 1.38e-23)) > np.random.rand():
            z = z_trial
    else:
        continue

# Měření
for i in range(iterations_measurement):
    z_trial = z + potential_energy(np.random.uniform(-1, 1)) * Delta_z

    if not math.isinf(z_trial):
        delta_E = potential_energy(z_trial) - potential_energy(z)
        if delta_E <= 0 or np.exp(-delta_E / (T * 1.38e-23)) > np.random.rand():
            z = z_trial
            accepted_configurations += 1

            if 8850 <= z < 8950:
                height_counts['high'] += 1
            elif 0 <= z < 100:
                height_counts['low'] += 1
    else:
        continue

# Výpočet tlaku
if height_counts['low'] == 0:
    pressure = float('inf')
else:
    pressure = height_counts['high'] / height_counts['low']

print(f"Tlak ve výšce 8850 m je {pressure} bar.")
print(f"Zlomek přijatých konfigurací je {accepted_configurations / iterations_measurement:.2f}.")
