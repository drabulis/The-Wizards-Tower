"""
10 speliu
4 enemies tipius
5 stages
stage 6 bosiukas"""

import math
import random

class Player:
    def __init__(self, name, hp=100, mana=50):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.spell_book = [firebolt, restore]

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0
    
    def add_spell(self, spell):
        self.spell_book.append(spell)
    
    F
   

zmogus = Player("zmogus", 100, 50)
zmogus.add_spell(Firebolt)


class Enemies:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0

class Magic:
    def __init__(self, name, damage, mana):
        self.name = name
        self.damage = damage
        self.mana = mana

firebolt = Magic("Firebolt", random.randint(3, 6), 2)
restore = Magic("Lightning", 20)



class World:
    def cast(self, target):
    enemy.take_damage(self.damage)
