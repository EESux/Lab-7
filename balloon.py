
"""
Created on Sat Apr 22 22:24:55 2023

@author: Jeff
"""

from random import randint
import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint

WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon")
balloon.pos = 400, 300

bird = Actor("bird-up")
bird.pos = randint(800, 1600), randint(10,200)

house = Actor("house")
house.pos = randint(800,1600), 460

tree = Actor("tree")
tree.pos = randint(800,1600), 450

bird_up = True 
up = False
game_over = False
score = 0 
lives = 5
number_of_updates = 0

scores = []

def update_high_scores(): 
    global score, scores 
    filename = "high-score.txt"
    scores = []
    with open(filename, "r") as file: 
        line = file.readline()
        high_scores_list = line.split()
        for high_score_str in high_scores_list:
            high_score_int = int(high_score_str)
            if(score > high_score_int): 
                scores.append(str(score) + " ")
                score = high_score_int
            else: 
                scores.append(str(high_score_int) + " ")
        with open(filename, "w") as file: 
            for high_score in scores: 
                file.write(high_score)


def display_high_scores():
    screen.draw.text("HIGH SCORES", (350,150), color ="black")
    y = 175
    position = 1
    for high_score in scores: 
        screen.draw.text(str(position) + ". " + high_score, (350,y), color = "black")
        y += 25 
        position += 1

def check_collision():
    global lives
    if balloon.colliderect(bird) or balloon.colliderect(house) or balloon.colliderect(tree):
        lives -= 1
        reset_obstacle(bird)
        reset_obstacle(house)
        reset_obstacle(tree)


def reset_obstacle(obstacle):
    min_distance = 300  # Set a minimum distance between the house and tree
    max_attempts = 10  # Set a limit for the number of attempts
    
    if obstacle == bird:
        obstacle.pos = randint(1200, 1600), randint(10, 200)
    elif obstacle == house:
        obstacle.pos = randint(1200, 1600), 460
    elif obstacle == tree:
        attempts = 0
        obstacle.pos = randint(1200, 1600), 450
        while abs(tree.x - house.x) < min_distance and attempts < max_attempts:
            tree.pos = randint(1200, 1600), 450
            attempts += 1




        
def draw(): 
    screen.blit("background", (0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700,5), color="black")
        screen.draw.text("Lives: " + str(lives), (700,30), color="black")
    else:
        display_high_scores()
def on_mouse_down(): 
    global up 
    up = True 
    balloon.y -=50 
    
    
def on_mouse_up(): 
    global up 
    up = False

def flap ():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else: 
        bird.image ="bird-up"
        bird_up = True
    
def update(): 
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            balloon.y += 1
            
        for obstacle in [bird, house, tree]:
            if obstacle.right > 0:
                if obstacle == bird:
                    obstacle.x -= 6
                    if number_of_updates == 9: 
                        flap()
                        number_of_updates = 0
                    else: 
                        number_of_updates +=1 
                else:
                    obstacle.x -= 2
            else:
                reset_obstacle(obstacle)
                if obstacle == bird:
                    score += 1

        check_collision()

        if lives <= 0:
            game_over = True
            update_high_scores()

                

pgzrun.go()
