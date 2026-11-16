import fastf1
import matplotlib.pyplot as plt

# Load the 2024 Silverstone Qualifying session
session = fastf1.get_session(2024, 'Silverstone', 'Q')
session.load()

# Pick the fastest qualifying laps for Lando Norris and Max Verstappen
norris_lap = session.laps.pick_driver('NOR').pick_fastest()
verstappen_lap = session.laps.pick_driver('VER').pick_fastest()

# Extract telemetry (Speed vs Distance around the track)
norris_tel = norris_lap.get_car_data().add_distance()
verstappen_tel = verstappen_lap.get_car_data().add_distance()

# Plot the speed comparison
plt.figure(figsize=(10, 5))
plt.plot(norris_tel['Distance'], norris_tel['Speed'], label='Norris (McLaren)', color='#FF8000')
plt.plot(verstappen_tel['Distance'], verstappen_tel['Speed'], label='Verstappen (Red Bull)', color='#0600EF')

plt.title('2024 British GP Qualifying - Fastest Lap Speed Comparison')
plt.xlabel('Track Distance (meters)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.show()
