import turtle
import math

class Planet:
    def __init__(self, name, orbit_radius, size, color, angle, speed):
        # Store basic planet data
        self.name = name
        self.orbit_radius = orbit_radius
        self.size = size
        self.color = color
        self.angle = angle
        self.speed = speed

        # Create the turtle that visually represents the planet
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.shapesize(size / 10)

    # Accessor methods
    def get_name(self):
        return self.name

    def get_orbit_radius(self):
        return self.orbit_radius

    def get_speed(self):
        return self.speed

    # Mutator methods
    def set_orbit_radius(self, new_radius):
        self.orbit_radius = new_radius

    def set_speed(self, new_speed):
        self.speed = new_speed

    # Movement behavior
    def move(self):
        # Calculate the x and y position using circular motion
        x = self.orbit_radius * math.cos(math.radians(self.angle))
        y = self.orbit_radius * math.sin(math.radians(self.angle))

        # Move the turtle to the new position
        self.turtle.goto(x, y)

        # Increase the angle to keep the planet moving
        self.angle += self.speed

    # Special string method
    def __str__(self):
        return f"Planet(name={self.name}, orbit_radius={self.orbit_radius}, size={self.size}, color={self.color}, angle={self.angle}, speed={self.speed})"