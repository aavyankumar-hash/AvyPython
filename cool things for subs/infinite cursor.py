import turtle 
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.tracer(1)

running = True

turtle.hideturtle()

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        super().__init__(shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.move_speed = 1
    def move(self):
        self.fd(self.move_speed)
        # wrap-around when leaving screen bounds
        x, y = self.position()
        half_w = screen.window_width() / 2
        half_h = screen.window_height() / 2
        if x > half_w:
            self.setx(-half_w)
        elif x < -half_w:
            self.setx(half_w)
        if y > half_h:
            self.sety(-half_h)
        elif y < -half_h:
            self.sety(half_h)

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        super().__init__(spriteshape, color, startx, starty)
        self.move_speed = 4
        self.lives = 3

    def turn_left(self):
        self.left(45)

    def turn_right(self):
        self.right(45)

    def accelerate(self):
        self.move_speed += 1

    def brake(self):
        self.move_speed -= 1

player = Player("triangle", "white", 0, 0)

def game_loop():
    if running:
        player.move()
        screen.ontimer(game_loop, 20)

def quit_game():
    global running
    running = False
    screen.bye()

screen.onkey(quit_game, "q")
screen.onkey(quit_game, "Escape")
screen.onkey(player.turn_right, "Right")
screen.onkey(player.turn_left, "Left")
screen.onkey(player.accelerate, "Up")
screen.onkey(player.brake, "Down")
screen.listen()

game_loop()
screen.mainloop()





