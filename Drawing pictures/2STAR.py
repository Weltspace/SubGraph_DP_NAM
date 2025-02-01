import matplotlib.pyplot as plt
import numpy as np


epsilon = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])




y1 = [1.5220438042969995, 0.30833633186841475, 0.05930647035403707, 0.03129857774210597, 0.019392324783411786, 0.010509196232353957, 0.005250801549201745, 0.00411672246169948, 0.004722592042479089, 0.00417871168674358, 0.0032485101079292975, 0.0020073202280945306]


fig, axs = plt.subplots(1, 2, figsize=(12, 5))


axs[0].plot(epsilon, y1, 'r-', label=r'2STAR:$\epsilon_0=0.1\epsilon$')
axs[0].set_yscale('log')
axs[0].set_title('Facebook',fontsize=20)
axs[0].set_xlabel('ε',fontsize=20)
axs[0].set_ylabel('Relative Error',fontsize=20)
axs[0].legend(ncol=1, fontsize=16)
for spine in axs[0].spines.values():
    spine.set_linewidth(3)
    spine.set_edgecolor('black')







z1 =  [6.242834707248765, 1.3536167193282371, 0.278934719327519, 0.16908913167253017, 0.10658730583183215, 0.05022884351784727, 0.032174403565358944, 0.018219322820032594, 0.014959425163071922, 0.008207948612493035, 0.006658758028942389, 0.005834514425591896]




axs[1].plot(epsilon, z1, 'r-', label=r'2STAR:$\epsilon_0=0.1\epsilon$')
axs[1].set_yscale('log')
axs[1].set_title('ASTRO-PH',fontsize=20)
axs[1].set_xlabel('ε',fontsize=20)
axs[1].set_ylabel('Relative Error',fontsize=20)
axs[1].legend(ncol=1, fontsize=16)
for spine in axs[1].spines.values():
    spine.set_linewidth(3)
    spine.set_edgecolor('black')






plt.tight_layout()
plt.savefig('2STAR.png')
plt.show()



