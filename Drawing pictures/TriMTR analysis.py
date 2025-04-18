import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 15,
    'axes.linewidth': 1.5,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5
})

epsilon = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])



y1 = [0.48253999983983153, 0.08682147440732502, 0.025037871723741816, 0.02269763175100236, 0.012592967858113816, 0.006424730125293041, 0.007722203279488778, 0.005830568839693831, 0.003958155770877306, 0.005823269227835795, 0.004595661409946579, 0.0032246437923602734]
y2 = [0.2698017145430361, 0.11025683219434437, 0.03354576768177591, 0.025191184601605607, 0.01977051843000073, 0.014270328808709144, 0.011059897628606834, 0.009902327575370299, 0.0071422593182060646, 0.007550668210391919, 0.005731561761873969, 0.0036938263756543664]
y3 = [0.5705311646433477, 0.1570256291646492, 0.08243960872421158, 0.04617899983901896, 0.03245827897140294, 0.02461181141937979, 0.015586935968527034, 0.01007574948641496, 0.009333194841728131, 0.0047438891302155235, 0.0055517637845860345, 0.00377031158978697]
y4 = [16.34537462875001, 2.2623239707164413, 0.3186301809413546, 0.1639417404900138, 0.10960451302027843, 0.04942411718100185, 0.030073881523760324, 0.014353656992799679, 0.011660822875063924, 0.010913225181757092, 0.007931051882959223, 0.007453778502188395]


z1 = [1.1518263112141414, 0.2777544761639902, 0.08338590296720806, 0.044715360812867075, 0.03386438020594997, 0.015197746082634632, 0.012966212427179543, 0.010992082712019298, 0.006600085989556322, 0.004791644839702876, 0.004970818276844354, 0.0034609009500990366]
z2 = [2.071302469176185, 0.42582884247517855, 0.10431776361075673, 0.06787958757566678, 0.05307113858987587, 0.020527347271368068, 0.016988479529752704, 0.015231688489899331, 0.01064229898260923, 0.0072861249830198545, 0.005852860285274122, 0.005404118783895983]
z3 = [1.6089884252202074, 0.4926258950762711, 0.12368201338150696, 0.09070306154798936, 0.06749880958143994, 0.03301339391874207, 0.021039885287207544, 0.017358517112095562, 0.00819726914113119, 0.008760100814240519, 0.007466298879401354, 0.004747892913599095]
z4 = [116.85352751735546, 11.32929274537777, 1.6504390510641047, 0.9957654902169959, 0.3954800205516201, 0.1714217647271006, 0.09261142020664341, 0.05966010046641545, 0.03204556890208547, 0.02833981838089447, 0.022605563418809933, 0.01704509656049306]


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


ax1.text(0.95, 0.95, 'Facebook/TriMTR', transform=ax1.transAxes,
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


ax2.text(0.95, 0.95, 'CA-AstroPH/TriMTR', transform=ax2.transAxes,
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

plt.savefig('TriMTR analysis.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
plt.show()