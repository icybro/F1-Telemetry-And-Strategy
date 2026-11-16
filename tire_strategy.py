import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt

# Enable FastF1's official tire compound colors (Green = Inter, Blue = Wet, Red/Yellow/White = Slicks)
fastf1.plotting.setup_mpl(color_scheme='fastf1')

# Load the 2026 São Paulo (Brazil) Grand Prix Race ('R')
race = fastf1.get_session(2026, 'Brazil', 'R')
race.load()

# Pick Lando Norris's race laps (we keep all laps except slow pit-in/out laps so you can see weather changes)
norris_laps = race.laps.pick_drivers('NOR').pick_wo_box()

# Plot lap time vs lap number colored by tire compound
fig, ax = plt.subplots(figsize=(12, 6))

for compound in norris_laps['Compound'].unique():
    stint_data = norris_laps[norris_laps['Compound'] == compound]
    color = fastf1.plotting.get_compound_color(compound, session=race)
    ax.scatter(stint_data['LapNumber'], stint_data['LapTime'].dt.total_seconds(),
               label=compound, color=color, s=55, edgecolors='black', linewidth=0.5)

ax.set_title('2026 Brazilian GP Race Strategy: Lando Norris Lap Times & Weather Crossover')
ax.set_xlabel('Lap Number (71 Laps Total)')
ax.set_ylabel('Lap Time (Seconds)')
ax.legend(title='Tire Compound')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('norris_brazil_2026_strategy.png', dpi=300)
plt.show()
