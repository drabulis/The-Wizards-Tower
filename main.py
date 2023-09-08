"""
10 speliu
4 enamies tipius
5 stages
stage 6 bosiukas"""

import math
import random

class Player:
    hp = 100
    mana = 50

class Enemies:
    def __init__(self, name, attack, hp, ):
        self.name = name
        self.attack = attack
        self.hp = hp
    
    def goblin(self, name, attack, hp, ):
        name = "Goblin"
        attack = ["basic attack", "light punsh", "hevy attack", "critical hit"]
        hp = 100
        action = random.randint(1, 4)
        for action in range(1, 4):
            if action == 1:
                attack[0] == 




    def Raven():
        
    def Puppy():
    
    def dragon():



class Magic:
    pass

class World:
    pass
