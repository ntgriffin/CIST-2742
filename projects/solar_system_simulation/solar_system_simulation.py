from planet_class import Planet
from sun_class import Sun
from solar_system_class import SolarSystem

def main():
    # Create the sun
    sun = Sun(0, 0, 14, "yellow")

    # Create the solar system
    solar_system = SolarSystem(sun)

    # Create planet objects
    mercury = Planet("Mercury", 70, 6, "gray", 0, 2.8)
    venus = Planet("Venus", 120, 7, "orange", 90, 2.0)
    earth = Planet("Earth", 180, 8, "blue", 180, 1.4)
    mars = Planet("Mars", 240, 7, "red", 270, 1.0)

    # Add planets to the solar system
    solar_system.add_planet(mercury)
    solar_system.add_planet(venus)
    solar_system.add_planet(earth)
    solar_system.add_planet(mars)

    # Demonstrate __str__
    print(sun)
    print(earth)

    # Demonstrate accessor and mutator
    print("Earth speed before change:", earth.get_speed())
    earth.set_speed(2.2)
    print("Earth speed after change:", earth.get_speed())

    # Print all system data
    solar_system.show_data()

    # Draw orbit paths
    solar_system.draw_orbits()

    # Start animation
    solar_system.animate()


if __name__ == "__main__":
    main()