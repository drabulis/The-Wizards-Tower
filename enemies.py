import random
from main import Player

class NPC:
    def __init__(self, name, hp=0, ):
        self.name = name
        self.hp = hp

    def receive_damage(self):
        player = Player()
        self.hp -= player.damage() #reikia player funkcijos
        if self.hp <= 0:
            return f"{self.name} has been defeated."
        else:
            return f"{self.name} has {self.hp} HP remaining."

class Goblin(NPC):
    def __init__(self, name="Goblin", hp=50):
        super().__init__(name, hp)  

    def attack(self):
        attack_types = ["basic attack", "light attack",  "heavy attack", "critical hit"]
        selected_attack = random.choice(attack_types)
        if selected_attack == "basic attack":
            damage = random.randint(1, 3)
        elif selected_attack == "light attack":
            damage = random.randint(3, 6)
        elif selected_attack == "heavy attack":
            damage = random.randint(6, 12)
        elif selected_attack == "critical attack":
            damage = random.randint(12, 24)
        return damage
        
class Ddragon(NPC):
    def __init__(self, name, hp=100):
        super().__init__(name, hp)

    def attack(self):
        attack_types = ["fire attack", "Tail smack",  "fire burst attack", "critical hit"]
        selected_attack = random.choice(attack_types)
        if selected_attack == "fire attack":
            damage = random.randint(3, 9)
        elif selected_attack == "tail smack":
            damage = random.randint(10, 15)
        elif selected_attack == "heavy attack":
            damage = random.randint(15, 25)
        elif selected_attack == "critical attack":
            damage = random.randint(20, 35)
        return damage