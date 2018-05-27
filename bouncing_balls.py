#!/usr/bin/env python3
##
## EPITECH PROJECT, 2018
## arcade
## File description:
## main
##

"""
Simple program to try arcade library
"""

import sys
import arcade
import random

class Ball:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.size = 20
        self.color = (0, 0, 0)
        self.x_speed = 1
        self.y_speed = 1



class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "floating")
        self.balls = []
        self.balls.append(gen_ball())


    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)

    def update(self, delta_time):
        for ball in self.balls:
            ball.x += ball.x_speed
            ball.y += ball.y_speed
            if ball.x >= WIDTH or ball.x <= 0:
                ball.x_speed *= -1
            if ball.y >= HEIGHT or ball.y <= 0:
                ball.y_speed *= -1

    def on_mouse_press(self, x, y, button, modifier):
        self.balls.append(gen_ball())


def gen_ball():
    ball = Ball()

    ball.size = random.randrange(10, 40)
    ball.x = random.randrange(0, WIDTH)
    ball.y = random.randrange(0, HEIGHT)
    ball.x_speed = random.randrange(1, 10)
    ball.y_speed = random.randrange(1, 10)
    ball.color = (random.randrange(256), random.randrange(256), random.randrange(256))

    return ball

def main():
    """
    Main function
    """
    game = Game()
    arcade.run()
    return SUCCESS


if __name__ == '__main__':
    SUCCESS = 0
    ERROR = 84
    WIDTH = 600
    HEIGHT = 600
    sys.exit(main())
