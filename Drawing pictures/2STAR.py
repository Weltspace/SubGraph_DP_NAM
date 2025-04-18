import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 15,
    'axes.linewidth': 1.5,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5
})

epsilon = np.array([0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])



y1 = np.array([0.005948673725640162, 0.002727359557115937, 0.0010317772861268277, 0.001130629621674564, 0.0008514572370265355, 0.0007860296149560711, 0.0005410121154157654, 0.0004573320020221564, 0.0002935955786948851, 0.00028566538642757326, 0.00030961710775331456, 0.00028051626098461735])
y2 = np.array([0.041598522493796836, 0.017312598969569888, 0.009618772286213844, 0.009311979141757, 0.006532346319994737, 0.004452576695129457, 0.0035563981517551975, 0.002672415382235792, 0.0020654156260286457, 0.0021429792102271522, 0.0032284954845291204, 0.00182619010267031])


z1 = np.array([0.03312606675554367, 0.005099425582972832, 0.001352408043372988, 0.0009435100776297925, 0.0006227580745354685, 0.0006034265883678476, 0.00044184573904950525, 0.00037832467781635115, 0.0002881437907838731, 0.00032613325050485063, 0.00020302880941195994, 0.00017754360453990035])
z2 = np.array([0.03203209133660939, 0.013932578680902209, 0.008891899462009821, 0.005423882735648683, 0.0045673964426653545, 0.003486426910009517, 0.0036326698017710127, 0.002063395835670815, 0.002237818438536267, 0.001268061129114848, 0.0019745715345095326, 0.0015949818456295452])


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
plt.subplots_adjust(wspace=0.3, top=0.85)


def auto_log_ticks(data):
    min_val = np.min(data)
    max_val = np.max(data)
    min_exp = np.floor(np.log10(min_val))
    max_exp = np.ceil(np.log10(max_val))
    ticks = 10**np.arange(min_exp, max_exp+1)
    return ticks


y_ticks = auto_log_ticks(np.concatenate([y1, y2, z1, z2]))


ax1.plot(epsilon, y1, 'ro-', markersize=6, label='2STAR')
ax1.plot(epsilon, y2, 'gs--', markersize=6, label=r'$\text{LocalLap}_{2\star}$')
ax1.set_yscale('log')
ax1.set_xlim(0, 2)
ax1.set_xlabel(r'$\epsilon$', fontsize=15)
ax1.set_ylabel('Relative Error', fontsize=15)


ax1.set_yticks(y_ticks)
ax1.set_yticklabels([f'$10^{{{int(np.log10(t))}}}$' for t in y_ticks])
ax1.grid(True, which="major", axis="y", ls="-", alpha=0.3)
ax1.grid(False, which="minor")


ax1.text(0.95, 0.95, 'Facebook', transform=ax1.transAxes,
         fontsize=20, ha='right', va='top',
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))


ax2.plot(epsilon, z1, 'ro-', markersize=6, label='2STAR')
ax2.plot(epsilon, z2, 'gs--', markersize=6, label=r'$\text{LocalLap}_{2\star}$')
ax2.set_yscale('log')
ax2.set_xlim(0, 2)
ax2.set_xlabel(r'$\epsilon$', fontsize=15)
ax2.set_ylabel('Relative Error', fontsize=15)


ax2.set_yticks(y_ticks)
ax2.set_yticklabels([f'$10^{{{int(np.log10(t))}}}$' for t in y_ticks])
ax2.grid(True, which="major", axis="y", ls="-", alpha=0.3)
ax2.grid(False, which="minor")


ax2.text(0.95, 0.95, 'CA-AstroPH', transform=ax2.transAxes,
         fontsize=20, ha='right', va='top',
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))


fig.legend(['2STAR', r'$\text{LocalLap}_{2\star}$'], fontsize=19,
           loc='upper center', bbox_to_anchor=(0.5, 1.0),
           ncol=2, frameon=True, edgecolor='black')


for ax in [ax1, ax2]:
    ax.set_xticks(np.arange(0, 2.1, 0.2))

plt.savefig('2STAR.png', dpi=300, bbox_inches='tight')
plt.show()