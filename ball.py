from turtle import Turtle
class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Ball movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    # Module 5: Detect collion with wall and bounce_y
    def bounce_y(self):
        self.y_move *= -1
    # Module 5: Detect collion with wall and bounce_x
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, -200)
        self.move_speed = 0.1
        self.bounce_y()
