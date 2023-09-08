"""
10 speliu
4 enemies tipius
5 stages
stage 6 bosiukas"""

import math
import random
import magic
import enemies

class Player:
    def __init__(self, name, hp=100, mana=50):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.spell_book = [magic.Firebolt(), magic.ManaRestore()]

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        return self.hp > 0
    
    def add_spell(self, spell):
        self.spell_book.append(spell)


class World:
    pass

wizard = Player(name='The Wizard')