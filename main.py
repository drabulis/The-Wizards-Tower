"""
10 speliu
4 enemies tipius
5 stages
stage 6 bosiukas"""

import math
import random

class Player:
    def __init__(self, name, hp=100, mana=50, spell_book=[]):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.spell_book = spell_book

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0
    
    def add_spell(self, spell):
        self.spell_book.append(spell)
   
   
class World:
    pass