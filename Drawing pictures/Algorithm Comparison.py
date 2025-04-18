import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 15,
    'axes.linewidth': 1.5,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5
})

epsilon = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])



y1 = [41.02667468025495, 5.404432936491682, 0.8060625781167093, 0.4615343304540578, 0.18922323313470155, 0.11446419042718224, 0.03494935307154985, 0.021183006658959055, 0.021606281306185977, 0.011734804966020385, 0.0077979950657372545, 0.005070546345407457]
y2 = [39.27714297026486, 6.354366346390754, 0.6888519826404488, 0.4438113426019599, 0.3188945156323091, 0.14109625914632895, 0.042832688283385906, 0.02486943020165193, 0.02334777842134304, 0.011115922987319636, 0.007509613272318978, 0.006715592020278693]
y3 = [0.6925983232038646, 0.22032876377362323, 0.06270279403915402, 0.04772839568821771, 0.03835683591555538, 0.025797867439350735, 0.018452998435271782, 0.012866512550905904, 0.01224895161878983, 0.010982706168431208, 0.008443220286177593, 0.007826083157987117]
y4 = [8.3077904111523, 1.3791321855336736, 0.43972310967984196, 0.2704600687392316, 0.14713299812152766, 0.16908791235441017, 0.05163924571294995, 0.046117767586278016, 0.04703047207177123, 0.039671017838595085, 0.02316829919370835, 0.022163238134907486]
y5 = [16.34537462875001, 2.2623239707164413, 0.3186301809413546, 0.1639417404900138, 0.10960451302027843, 0.04942411718100185, 0.030073881523760324, 0.014353656992799679, 0.011660822875063924, 0.010913225181757092, 0.007931051882959223, 0.007453778502188395]
y6 = [26.72837212618403, 6.470588346330759, 1.3515191070056836, 0.8743342083342086, 0.570408516262151, 0.3900034575689639, 0.2531561217107833, 0.26383381555589946, 0.17730628965824155, 0.22505951686942863, 0.2735298280222546, 0.26224933348854945]


z1 = [461.44958210873034, 77.4119021767254, 9.497015578121959, 5.699433249129026, 2.1874136858127073, 0.8985992541714004, 0.39622173948471096, 0.22917823664117135, 0.20553591980615774, 0.0888082022522053, 0.06703504881812651, 0.04650755521497844]
z3 = [1.7405725918150454, 0.36551218069090236, 0.12051709919072091, 0.09308597989462007, 0.06953752055211689, 0.0440487516230969, 0.03024625756283599, 0.02597101497515445, 0.023231211562288204, 0.016752889084061147, 0.01352788252972033, 0.014416624455146965]
z4 = [7.096417814626663, 2.219483580422614, 0.5008065670505627, 0.4975442469654894, 0.34958108133468985, 0.17318252053485111, 0.048420446611371126, 0.06144564777674471, 0.06131744208130427, 0.04076771189347051, 0.037658457794289904, 0.030455628492390044]
z5 = [116.85352751735546, 11.32929274537777, 1.6504390510641047, 0.9957654902169959, 0.3954800205516201, 0.1714217647271006, 0.09261142020664341, 0.05966010046641545, 0.03204556890208547, 0.02833981838089447, 0.022605563418809933, 0.01704509656049306]
z6 = [685.0767783840929, 87.24885324841085, 7.98164465736573, 3.895832067671515, 2.048133457694161, 1.741893034980261, 1.0365129330391691, 0.48367920675746556, 0.6183179105819426, 0.311479362760543, 0.5251262000468391, 0.391940534342852]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(wspace=0.3, top=0.76)


def auto_log_ticks(data):
    min_val = np.min(data)
    max_val = np.max(data)
    min_exp = np.floor(np.log10(min_val))
    max_exp = np.ceil(np.log10(max_val))
    ticks = 10**np.arange(min_exp, max_exp+1)
    return ticks


y_ticks1 = auto_log_ticks(np.concatenate([y1, y2, y3, y4, y5, y6]))
y_ticks2 = auto_log_ticks(np.concatenate([z1, z3, z4, z5, z6]))


ax1.plot(epsilon, y1, 'ro-', markersize=6, label='TriOR')
ax1.plot(epsilon, y2, 'ro--', markersize=6, label=r'$\text{RR}_{\bigtriangleup}$')
ax1.plot(epsilon, y3, 'go-', markersize=6, label='TriTR')
ax1.plot(epsilon, y4, 'gs--', markersize=6, label=r'$\text{2R-Large}_{\bigtriangleup}$')
ax1.plot(epsilon, y5, 'ko-', markersize=6, label='TriMTR')
ax1.plot(epsilon, y6, 'ks--', markersize=6, label=r'$\text{Wshuffle}_{\bigtriangleup}$')
ax1.set_yscale('log')
ax1.set_xlim(0, 2)
ax1.set_xlabel(r'$\epsilon$', fontsize=20)
ax1.set_ylabel('Relative Error', fontsize=20)


ax1.set_yticks(y_ticks1)
ax1.set_yticklabels([f'$10^{{{int(np.log10(t))}}}$' for t in y_ticks1])
ax1.grid(True, which="major", axis="y", ls="-", alpha=0.3)
ax1.grid(False, which="minor")


ax1.text(0.95, 0.95, 'Facebook', transform=ax1.transAxes,
         fontsize=20, ha='right', va='top',
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

ax2.plot(epsilon, z1, 'ro-', markersize=6, label='TriOR')
ax2.plot(epsilon, z3, 'go-', markersize=6, label='TriTR')
ax2.plot(epsilon, z4, 'gs--', markersize=6, label=r'$\text{2R-Large}_{\bigtriangleup}$')
ax2.plot(epsilon, z5, 'ko-', markersize=6, label='TriMTR')
ax2.plot(epsilon, z6, 'ks--', markersize=6, label=r'$\text{Wshuffle}_{\bigtriangleup}$')
ax2.set_yscale('log')
ax2.set_xlim(0, 2)
ax2.set_xlabel(r'$\epsilon$', fontsize=20)
ax2.set_ylabel('Relative Error', fontsize=20)


ax2.set_yticks(y_ticks2)
ax2.set_yticklabels([f'$10^{{{int(np.log10(t))}}}$' for t in y_ticks2])
ax2.grid(True, which="major", axis="y", ls="-", alpha=0.3)
ax2.grid(False, which="minor")


ax2.text(0.95, 0.95, 'CA-AstroPH', transform=ax2.transAxes,
         fontsize=20, ha='right', va='top',
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))


fig.legend(['TriOR', r'$\text{RR}_{\bigtriangleup}$', 'TriTR', r'$\text{2R-Large}_{\bigtriangleup}$', 'TriMTR', r'$\text{Wshuffle}_{\bigtriangleup}$'],
           fontsize=19,
           loc='upper center',
           bbox_to_anchor=(0.5, 0.95),
           ncol=3,
           frameon=True,
           edgecolor='black')


for ax in [ax1, ax2]:
    ax.set_xticks(np.arange(0, 2.1, 0.2))

plt.savefig('Algorithm Comparison.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
plt.show()