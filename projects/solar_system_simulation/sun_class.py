import turtle

class Sun:
    def __init__(self, x, y, size, color):
        # Store sun data
        self.x = x
        self.y = y
        self.size = size
        self.color = color

        # Create the turtle that visually represents the sun
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.shapesize(size / 10)
        self.turtle.goto(x, y)

    # Accessor method
    def get_position(self):
        return (self.x, self.y)

    # Mutator method
    def set_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.turtle.goto(new_x, new_y)

    # Special string method
    def __str__(self):
        return f"Sun(x={self.x}, y={self.y}, size={self.size}, color={self.color})"