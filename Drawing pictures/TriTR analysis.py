import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 15,
    'axes.linewidth': 1.5,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5
})

epsilon = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])



y1 = [0.035461393367846844, 0.019935376746709844, 0.006947893726277413, 0.006134065765619888, 0.007671273782332046, 0.005674376613579965, 0.0029071194021747407, 0.00347077324956086, 0.0032216648197484874, 0.002850280876246825, 0.0018734701571314744, 0.0015172221404637968]
y2 = [0.04678285814199099, 0.027281847712531962, 0.017069351207299688, 0.009033459939584609, 0.007607093823519357, 0.0058548107751959675, 0.005092915509206319, 0.003785693491336132, 0.0030154628570543867, 0.0031521068974768654, 0.0026655072675246215, 0.00229690715354889]
y3 = [0.1903645101098522, 0.10069981501563746, 0.04228619950293982, 0.0267855825728203, 0.021948516151313404, 0.010602065960788477, 0.005242245005042876, 0.00434310429248292, 0.0035580155393680106, 0.001784283728489987, 0.0025998657254986185, 0.0027407035576486067]
y4 = [0.6925983232038646, 0.22032876377362323, 0.06270279403915402, 0.04772839568821771, 0.03835683591555538, 0.025797867439350735, 0.018452998435271782, 0.012866512550905904, 0.01224895161878983, 0.010982706168431208, 0.008443220286177593, 0.007826083157987117]


z1 = [0.025110986494670764, 0.012515841079254292, 0.0057767985111446775, 0.005002525940233685, 0.004831513079554458, 0.0034845401639657047, 0.0023659648567287543, 0.0015707226540262107, 0.0021212034240057163, 0.001617813707396263, 0.001400146458842957, 0.0012856772111420345]
z2 = [0.029728298436108642, 0.019990149681538356, 0.008213286591200882, 0.006764149696442886, 0.004759679097786938, 0.003328072347342771, 0.004349169682677744, 0.00385938501033303, 0.0019736446445091705, 0.0024495426331971053, 0.0018537436123453365, 0.0017872947312130563]
z3 = [0.19200135256192294, 0.1237060056308053, 0.055037809484523546, 0.03557984133282751, 0.02502363207516218, 0.014512835239771324, 0.007883829219503556, 0.005069013040975303, 0.0029791276737356613, 0.0033820876879448298, 0.002269696038651293, 0.0022957446271585054]
z4 = [1.7405725918150454, 0.36551218069090236, 0.12051709919072091, 0.09308597989462007, 0.06953752055211689, 0.0440487516230969, 0.03024625756283599, 0.02597101497515445, 0.023231211562288204, 0.016752889084061147, 0.01352788252972033, 0.014416624455146965]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(wspace=0.3, top=0.76)


def auto_log_ticks(data):
    min_val = np.min(data)
    max_val = np.max(data)
    min_exp = np.floor(np.log10(min_val))
    max_exp = np.ceil(np.log10(max_val))
    ticks = 10**np.arange(min_exp, max_exp+1)
    return ticks


y_ticks1 = auto_log_ticks(np.concatenate([y1, y2, y3, y4]))
y_ticks2 = auto_log_ticks(np.concatenate([z1, z2, z3, z4]))


ax1.plot(epsilon, y1, 'ro-', markersize=6, label='Stage 1')
ax1.plot(epsilon, y2, 'g^-', markersize=6, label='Stage 2')
ax1.plot(epsilon, y3, 'bs-', markersize=6, label='Stage 3')
ax1.plot(epsilon, y4, 'k*-', markersize=8, label='Stage 4')
ax1.set_yscale('log')
ax1.set_xlim(0, 2)
ax1.set_xlabel(r'$\epsilon$', fontsize=20)
ax1.set_ylabel('Relative Error', fontsize=20)


ax1.set_yticks(y_ticks1)
ax1.set_yticklabels([f'$10^{{{int(np.log10(t))}}}$' for t in y_ticks1])
ax1.grid(True, which="major", axis="y", ls="-", alpha=0.3)
ax1.grid(False, which="minor")


ax1.text(0.95, 0.95, 'Facebook/TriTR', transform=ax1.transAxes,
         fontsize=20, ha='right', va='top',
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

ax2.plot(epsilon, z1, 'ro-', markersize=6, label='Stage 1')
ax2.plot(epsilon, z2, 'g^-', markersize=6, label='Stage 2')
ax2.plot(epsilon, z3, 'bs-', markersize=6, label='Stage 3')
ax2.plot(epsilon, z4, 'k*-', markersize=8, label='Stage 4')
ax2.set_yscale('log')
ax2.set_xlim(0, 2)
ax2.set_xlabel(r'$\epsilon$', fontsize=20)
ax2.set_ylabel('Relative Error', fontsize=20)


ax2.set_yticks(y_ticks2)
ax2.set_yticklabels([f'$10^{{{int(np.log10(t))}}}$' for t in y_ticks2])
ax2.grid(True, which="major", axis="y", ls="-", alpha=0.3)
ax2.grid(False, which="minor")


ax2.text(0.95, 0.95, 'CA-AstroPH/TriTR', transform=ax2.transAxes,
         fontsize=20, ha='right', va='top',
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))


fig.legend(['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4'],
           fontsize=19,
           loc='upper center',
           bbox_to_anchor=(0.5, 0.9),
           ncol=4,
           frameon=True,
           edgecolor='black')


for ax in [ax1, ax2]:
    ax.set_xticks(np.arange(0, 2.1, 0.2))

plt.savefig('TriTR analysis.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
plt.show()