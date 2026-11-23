"""
This program is Colton Barrentine and Xavier Vance's (very basic) version of Whack-A-Mole
Note: AI was used for debugging and structuring SOME functions, but all variables, lists, etc. are original work
"""

import turtle as trtl
import random as rand

#---setup---
wn = trtl.Screen()

mole_shape = "da_mole_resized.gif"

# configures turtle that draws the grid
grid = trtl.Turtle()
grid.speed(9999999)
grid.hideturtle()

# configures "da mole"
mole = trtl.Turtle()
wn.addshape(mole_shape)
mole.shape(mole_shape)
mole.penup()
mole.hideturtle()
mole.speed(99999999999999)

# configures countdown to start game
pen = trtl.Turtle()
pen.hideturtle()
pen.pencolor("red")
count = 3

timer = 60
score = 0

just_clicked = False
game_over = False

# difficulty will impact size of grid, and speed of moles
difficulty = input("Choose your difficulty(Easy, Medium, or Hard): ")

# configures score
score_pen = trtl.Turtle()
score_pen.hideturtle()
score_pen.penup()
if difficulty == "Hard":
  score_pen.goto(-450, 450)
else:
  score_pen.goto(-400, 250)

# configures in game countdownF
timer_pen = trtl.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
if difficulty == "Hard":
  timer_pen.goto(450, 450)
else:
  timer_pen.goto(200, 250)

# spawn locations of moles on easy difficulty
easy_dif_spawns = [(-100, -150), (0, -150), (100, -150), # (bottom row)
                   (-100, -50), (0, -50), (100, -50), # (middle row)
                   (-100, 50), (0, 50), (100, 50)] # (top row)

# spawn locations of moles on medium difficulty
medium_dif_spawns = [(-200, -150), (-100, -150), (0, -150), (100, -150), (200, -150), # (first row)
                     (-200, -50), (-100, -50), (0, -50), (100, -50), (200, -50), # (second row)
                     (-200, 50), (-100, 50), (0, 50), (100, 50), (200, 50), # (third row)
                     (-200, 150), (-100, 150), (0, 150), (100, 150), (200, 150), # (fourth row)
                     (-200, 250), (-100, 250), (0, 250), (100, 250), (200, 250)] # (fifth row)

# spawn locations of moles on hard difficulty
hard_dif_spawns = [(-450, -400), (-350, -400), (-250, -400), (-150, -400), (-50, -400), (50, -400), (150, -400), (250, -400), (350, -400), # (first row)
                   (-450, -300), (-350, -300), (-250, -300), (-150, -300), (-50, -300), (50, -300), (150, -300), (250, -300), (350, -300), # (second row)
                    (-450, -200), (-350, -200), (-250, -200), (-150, -200), (-50, -200), (50, -200), (150, -200), (250, -200), (350, -200), # (third row)
                    (-450, -100), (-350, -100), (-250, -100), (-150, -100), (-50, -100), (50, -100), (150, -100), (250, -100), (350, -100), # (fourth row)
                    (-450, 0), (-350, 0), (-250, 0), (-150, 0), (-50, 0), (50, 0), (150, 0), (250, 0), (350, 0), # (fifth row)
                    (-450, 100), (-350, 100), (-250, 100), (-150, 100), (-50, 100), (50, 100), (150, 100), (250, 100), (350, 100), # (sixth row)
                    (-450, 200), (-350, 200), (-250, 200), (-150, 200), (-50, 200), (50, 200), (150, 200), (250, 200), (350, 200), # (seventh row)
                    (-450, 300), (-350, 300), (-250, 300), (-150, 300), (-50, 300), (50, 300), (150, 300), (250, 300), (350, 300),] # (eighth row)

#---functions---
def draw_square():
  for i in range(4):
    grid.forward(100)
    grid.right(90)

# draws the grid for easy difficulty
def draw_easy_grid():
  # draws the bottom row
  grid.penup()
  grid.goto(-150, -100)
  grid.pendown()
  draw_square()
  for i in range(2):
    grid.forward(100)
    draw_square()
  
  # draws the middle row
  grid.penup()
  grid.goto(-150, 0)
  grid.pendown()
  draw_square()
  for i in range(2):
    grid.forward(100)
    draw_square()
  
  # draws the top row
  grid.penup()
  grid.goto(-150, 100)
  grid.pendown()
  draw_square()
  for i in range(2):
    grid.forward(100)
    draw_square()

# draws the grid for medium difficulty
def draw_medium_grid():
  # draws the bottom row
  grid.penup()
  grid.goto(-250, -100)
  grid.pendown()
  draw_square()
  for i in range(4):
    grid.forward(100)
    draw_square()
  
  # draws the first middle row
  grid.penup()
  grid.goto(-250, 0)
  grid.pendown()
  draw_square()
  for i in range(4):
    grid.forward(100)
    draw_square()
  
  # draws the second middle row
  grid.penup()
  grid.goto(-250, 100)
  grid.pendown()
  draw_square()
  for i in range(4):
    grid.forward(100)
    draw_square()
  
  # draws the third middle row
  grid.penup()
  grid.goto(-250, 200)
  grid.pendown()
  draw_square()
  for i in range(4):
    grid.forward(100)
    draw_square()
  
  # draws the top row
  grid.penup()
  grid.goto(-250, 300)
  grid.pendown()
  draw_square()
  for i in range(4):
    grid.forward(100)
    draw_square()

# draws the grid for hard difficulty
def draw_hard_grid():
  # draws first row
  grid.penup()
  grid.goto(-500, -350)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()
  
  # draws second row
  grid.penup()
  grid.goto(-500, -250)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()
  
  # draws third row
  grid.penup()
  grid.goto(-500, -150)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()
  
  # draws fourth row
  grid.penup()
  grid.goto(-500, -50)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()
  
  # draws fifth row
  grid.penup()
  grid.goto(-500, 50)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()
  
  # draws sixth row
  grid.penup()
  grid.goto(-500, 150)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()
  
  # draws seventh row
  grid.penup()
  grid.goto(-500, 250)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()
  
  # draws eigth row
  grid.penup()
  grid.goto(-500, 350)
  grid.pendown()
  draw_square()
  for i in range(9):
    grid.forward(100)
    draw_square()

# counts down from 3 to 0, then starts the game
def countdown():
  global count
  if count > 0:
    pen.clear()
    pen.write(count, align="center", font=("Arial", 40, "bold"))
    count -= 1
    wn.ontimer(countdown, 1000)
  else: # if the count is not greater than 0, a mole will be spawn in at a random location depending on the difficulty
    pen.clear()
    print("Game started!")
    countdown_game()
    if difficulty == "Easy":
      spawn_mole_easy()
    elif difficulty == "Medium":
      spawn_mole_medium()
    else:
      spawn_mole_hard()

# displays a 60 second timer in the top right, game ends when timer reaches 0
def countdown_game():
  global timer, game_over
  if game_over:
    return

  if timer > 0:
    timer_pen.clear()
    timer_pen.write("Time: " + str(timer), font=("Arial", 16, "bold"))
    timer -= 1
    wn.ontimer(countdown_game, 1000)
  else: # ends the game when the timer reaches 0
    game_over = True
    timer_pen.clear()
    timer_pen.write("Game Over", align="center", font=("Arial", 40, "bold"))
    mole.hideturtle()

# spawns a mole at a random easy coordinate
def spawn_mole_easy():
    global game_over
    if game_over: # if game_over is true mole doesn't spawn
      return
    x, y = rand.choice(easy_dif_spawns)
    mole.goto(x, y)
    mole.showturtle()
    wn.ontimer(hide_mole, 2000)

# spawns a mole at a random medium coordinate
def spawn_mole_medium():
  global game_over
  if game_over: # if game over is true mole doesn't spawn
    return
  x, y = rand.choice(medium_dif_spawns)
  mole.goto(x, y)
  mole.showturtle()
  wn.ontimer(hide_mole, 1200)

# spawns a mole at a random hard coordinate
def spawn_mole_hard():
  global game_over
  if game_over: # if game over is true mole doesn't spawn
    return
  x, y = rand.choice(hard_dif_spawns)
  mole.goto(x, y)
  mole.showturtle()
  wn.ontimer(hide_mole, 700)

# hides mole if mole is clicked and adds 5 to the players score
def whacked(x, y):
  global score, just_clicked
  mole.hideturtle()
  score += 5
  just_clicked = True
  update_score()

def hide_mole():
  global score, just_clicked
  if just_clicked: # if a mole is clicked a new mole will be added after 1 second
    just_clicked = False
    if difficulty == "Easy":
      wn.ontimer(spawn_mole_easy, 1000)
    elif difficulty == "Medium":
      wn.ontimer(spawn_mole_medium, 1000)
    else:
      wn.ontimer(spawn_mole_hard, 1000)
    return

  # removes 5 points from the players score if the mole was not clicked within the time limit, then spawns a new mole after 1 second
  mole.hideturtle()
  score -= 5
  update_score()
  if difficulty == "Easy":
    wn.ontimer(spawn_mole_easy, 1000)
  elif difficulty == "Medium":
    wn.ontimer(spawn_mole_medium, 1000)
  else:
    wn.ontimer(spawn_mole_hard, 1000)

def update_score():
  score_pen.clear()
  score_pen.write("Score: " + str(score), align="left", font=("Arial", 20, "bold"))

#---run---
pen.penup()
pen.goto(0, 0)

if difficulty == "Easy":
  draw_easy_grid()
  
elif difficulty == "Medium":
  draw_medium_grid()
  
else:
  draw_hard_grid()

mole.onclick(whacked)

countdown()

#---end---
wn.mainloop()