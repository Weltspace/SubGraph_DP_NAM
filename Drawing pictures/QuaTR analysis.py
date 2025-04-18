import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 15,
    'axes.linewidth': 1.5,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5
})

epsilon = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])



y1 = [0.21140148452906496, 0.054941665079607495, 0.021077949349651782, 0.016134161260088552, 0.014819735276527208, 0.014275034452921468, 0.007775881840411571, 0.01016753092042421, 0.005169610276545745, 0.0044099184865913545, 0.004773206360142158, 0.004138654410498542]
y2 = [0.2620567644268626, 0.11752466057453252, 0.034388740357023766, 0.018347006636979, 0.018743559744860465, 0.01759900635623971, 0.013640988204561949, 0.009592213777006597, 0.005950189627406346, 0.00666860663551411, 0.0066147115312724545, 0.006449351826621102]
y3 = [0.457761656043931, 0.16432669018421225, 0.09295260574762824, 0.05238939247673795, 0.045624733605421686, 0.017854212155412556, 0.009891471381204216, 0.01033901332684511, 0.00772995443496728, 0.004742872780485636, 0.006829627475137804, 0.004951819653063784]
y4 = [5.353421076362175, 0.8222630005448358, 0.2572033047609836, 0.2641891524342042, 0.15812851238696632, 0.13177736929020306, 0.11080219762531959, 0.08750260329482937, 0.07717977785343691, 0.06134838081846215, 0.05276765134425879, 0.050276156380735404]


z1 = [0.8870603837360695, 0.2267616956513692, 0.04911131209218775, 0.041570878412825474, 0.01980152297959751, 0.00908158953120776, 0.010538579522456073, 0.008015136088645096, 0.00857519861828422, 0.004566643560187914, 0.003744622013887845, 0.002446161098484683]
z2 = [1.4890224651814732, 0.4155563661652533, 0.0949496637285061, 0.05530500337808162, 0.035294640852794684, 0.022398523277463694, 0.012168203658515907, 0.01179295239577295, 0.0077186767205680885, 0.00790891099282948, 0.006263939138624932, 0.005400339852875349]
z3 = [1.499952167739457, 0.3520760153889495, 0.11684786816898167, 0.09279422701674714, 0.0609295072607019, 0.03600782620760586, 0.01795701294790702, 0.012407216788210062, 0.010864651423793502, 0.00872107902898665, 0.005249206800524046, 0.007892727925268113]
z4 = [47.87125885501267, 7.047162877341507, 1.3645505656051562, 0.8607584773739823, 0.5834782474400931, 0.3489860822334586, 0.3530514400362241, 0.20834558785347657, 0.2065403231094611, 0.15298362389904346, 0.17202798077920045, 0.1243786186651646]


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


ax1.text(0.95, 0.95, 'Facebook/QuaTR', transform=ax1.transAxes,
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


ax2.text(0.95, 0.95, 'CA-AstroPH/QuaTR', transform=ax2.transAxes,
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

plt.savefig('QuaTR analysis.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
plt.show()