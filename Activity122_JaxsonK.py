#-----import statements--
import turtle as trtl
import random as rand
import leaderboard as lb
score_writer =  trtl.Turtle()
tr = trtl.Turtle()
trtl.hideturtle()
wn = trtl.Screen()
wn.bgpic("ghost.gif")
tr.penup()
tr.forward(15)
tr.left(90)
tr.forward(50)
#-----game configuration-
spotColor = "pink"
spotShape = "circle"
spotSize = 2
#-----initialize turtle--
spot = trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
#-----game functions-----
font_setup = ("Arial", 20, "normal")
score = 0
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list= ""
leader_scores_list = ""
player_name = input("what is your name")
#-----import statements-----
import turtle as trtl

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  trtl.Turtle()
counter.penup()
counter.goto(-25,-200)
counter.pendown()
#-----score writer-----
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-50,200)
#-----game functions-----
# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def score_update():
  global score
  if timer <= 0:
    print(score)
  else:
    score_writer.clear()
    score_writer.write("Score: " + str(score), font=font_setup)
    score += 1

def spot_clicked(x,y):
  change_position()
  score_update()
  
def change_position():
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  spot.hideturtle()
  spot.goto(new_xpos,new_ypos)
  spot.showturtle()
  


#-----events-------------
countdown()
spot.penup()
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()