# FSPD Nile Simulator - Egypt vs Ethiopia vs Sudan
# Creator: [Your Name] | Cairo, Nov 11 2025
import numpy as np
import matplotlib.pyplot as plt

# import numpy as np
import matplotlib.pyplot as plt

agents = ['Egypt', 'Ethiopia', 'Sudan']
R = np.array([100.0, 70.0, 50.0])
C = np.array([0.3, 0.1, 0.4])
rho = np.array([0.7, 0.4, 0.6])
S = np.zeros(3); M = np.zeros(3)
history = []
coalition = {0, 2}

for t in np.arange(0, 50, 0.1):
    payoff = np.zeros(3)
    if len(coalition) > 1:
        members = list(coalition)
        contrib = sum(C[i]*R[i] for i in members)
        for i in members:
            payoff[i] = (1.8 * contrib) / len(members) - 0.05 * R[i]
    S[1] = 0.15 * R[1]; M[0] = 0.1 * R[0]
    rho = 0.9*rho + 0.1*np.clip(C, 0, 1)
    if rho[0] > 0.65: C[0] = min(C[0] + 0.02, 1.0)
    if R[1] > 80: C[1] = max(C[1] - 0.03, 0.0)
    dR = payoff - 1.0*C*R - 2.0*S - 1.5*M
    R = np.maximum(R + dR*0.1, 1.0)
    history.append([t, *R, *C, *rho])

data = np.array(history)
plt.figure(figsize=(10,6))
plt.subplot(2,1,1); plt.plot(data[:,0], data[:,1:4]); plt.legend(agents); plt.title('Resources')
plt.subplot(2,1,2); plt.plot(data[:,0], data[:,7:10]); plt.legend(agents); plt.title('Reputation')
plt.tight_layout(); plt.show()

# Print final results
print(f"Egypt: {R[0]:.1f} | Ethiopia: {R[1]:.1f} | Sudan: {R[2]:.1f}")
