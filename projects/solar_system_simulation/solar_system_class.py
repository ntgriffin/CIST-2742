import turtle

class SolarSystem:
    def __init__(self, sun):
        # Store the sun object
        self.sun = sun

        # Create an empty list for planet objects
        self.planets = []

        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.setup(width=900, height=900)
        self.screen.bgcolor("white")
        self.screen.title("Solar System Simulation")

    def add_planet(self, planet):
        # Add a planet to the solar system
        self.planets.append(planet)

    def draw_orbits(self):
        # Create a turtle used only to draw orbit paths
        orbit_drawer = turtle.Turtle()
        orbit_drawer.hideturtle()
        orbit_drawer.speed(0)
        orbit_drawer.color("black")
        orbit_drawer.penup()

        # Draw one orbit for each planet
        for planet in self.planets:
            orbit_drawer.goto(0, -planet.get_orbit_radius())
            orbit_drawer.pendown()
            orbit_drawer.circle(planet.get_orbit_radius())
            orbit_drawer.penup()

    def show_data(self):
        # Print the sun
        print(self.sun)

        # Print each planet
        for planet in self.planets:
            print(planet)

    def animate(self):
        # Turn off automatic updates for smoother animation
        self.screen.tracer(0)

        # Run the animation forever
        while True:
            for planet in self.planets:
                planet.move()

            self.screen.update()

    def __str__(self):
        return f"SolarSystem with {len(self.planets)} planets"