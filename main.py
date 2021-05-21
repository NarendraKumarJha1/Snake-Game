import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")

s.bgpic("snake.gif")
s.title("Snake Game")
s.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
s.listen()
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
game_is_on = True


while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
s.exitonclick()