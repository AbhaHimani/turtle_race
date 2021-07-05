import turtle
import random
from turtle import Turtle,Screen
tim= Turtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which colour will win the race? Enter a colour:")
y_positions = [-70, -40, -10, 20,50,80]
colors=["red","orange", "violet", "pink","blue","green"]
all_turtles = []
for turtle_index in range(0,6):
  tim=Turtle(shape="turtle")
  tim.color(colors[turtle_index])
  tim.penup()
  tim.goto(x=-230, y = y_positions[turtle_index])
  all_turtles.append(tim)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor()>230:
      is_race_on=False
      winning_color= turtle.pencolor()
      if winning_color==user_bet:
         print(f"You won! {winning_color} won!")
         break
      #we used pencolour because turtle.color will give the colour twice 1.pencolour 2.fillcolour
      else:
        print(f"You lose! {winning_color} won! ")

    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)




screen.exitonclick()








screen.exitonclick()



