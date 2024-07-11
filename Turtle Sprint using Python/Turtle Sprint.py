import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS=['red', 'blue', 'cyan', 'white', 'black']

def get_number_of_racers():
    # Prompt user the number of turtle for the race
    racers = 0
    
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("The input is not correct. Try again")
            continue
            
        if 2<= racers <=10:
            return racers
        else:
            print("Not in the range 2-10. Try again")
            
def race(colors):
    # Set the speed of the turtle sprint randomly
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
               
def create_turtles(colors):
    # Create the turtles, colors and their starting position
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # Set the position of the turtle
        # Consider negative as it start from the left in a coordinate graph
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
        
    return turtles
                        
def init_turtle():
    # Create the screen to show the turtle race
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Sprint!')
    
    
# Get the number of racers prompt by the user
racers = get_number_of_racers()
init_turtle()

# Set the color of the turtles randomly
random.shuffle(COLORS)
colors = COLORS[:racers]

# Show the winning turtle
winner = race(colors)
print('The winner is turtle '+ winner)
time.sleep(5)


