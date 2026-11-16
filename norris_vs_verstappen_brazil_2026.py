import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt

# Setup FastF1 dark theme without deprecation warnings
fastf1.plotting.setup_mpl(color_scheme='fastf1')

# Load the cached 2026 São Paulo Grand Prix Race
race = fastf1.get_session(2026, 'Brazil', 'R')
race.load()

# Get non-pit-lane laps for Norris (McLaren) and Verstappen (Red Bull)
norris_laps = race.laps.pick_drivers('NOR').pick_wo_box()
verstappen_laps = race.laps.pick_drivers('VER').pick_wo_box()

fig, ax = plt.subplots(figsize=(13, 6))

# Plot Lando Norris (McLaren Orange line + circles)
ax.plot(norris_laps['LapNumber'], norris_laps['LapTime'].dt.total_seconds(),
        color='#FF8000', marker='o', markersize=4, linewidth=1.5, label='Lando Norris (McLaren)')

# Plot Max Verstappen (Red Bull Blue line + triangles)
ax.plot(verstappen_laps['LapNumber'], verstappen_laps['LapTime'].dt.total_seconds(),
        color='#3671C6', marker='^', markersize=4, linewidth=1.5, linestyle='--', label='Max Verstappen (Red Bull)')

# Highlight Norris's pit-in laps with vertical dashed orange lines
norris_pits = race.laps.pick_drivers('NOR').dropna(subset=['PitInTime'])['LapNumber']
for idx, pit_lap in enumerate(norris_pits):
    ax.axvline(x=pit_lap, color='#FF8000', linestyle=':', alpha=0.6,
               label='Norris Pit Stop' if idx == 0 else "")

# Highlight Verstappen's pit-in laps with vertical dashed blue lines
ver_pits = race.laps.pick_drivers('VER').dropna(subset=['PitInTime'])['LapNumber']
for idx, pit_lap in enumerate(ver_pits):
    ax.axvline(x=pit_lap, color='#3671C6', linestyle='-.', alpha=0.6,
               label='Verstappen Pit Stop' if idx == 0 else "")

ax.set_title('2026 Brazilian GP Strategy Battle: Norris (McLaren) vs Verstappen (Red Bull)')
ax.set_xlabel('Lap Number (71 Laps Total)')
ax.set_ylabel('Lap Time (Seconds)')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('norris_vs_verstappen_brazil_2026.png', dpi=300)
plt.show()
