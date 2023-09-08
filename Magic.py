import random

class Spell:
    def __init__(self, name, min_damage=0, max_damage=0, mana_cost=0, lifesteal=False) -> None:
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.mana_cost = mana_cost
        self.lifesteal = lifesteal

    def __str__(self) -> str:
        return f'{self.name} {self.min_damage}-{self.max_damage} {self.mana_cost}'
    
    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)


class Firebolt(Spell):
    def __init__(self, name='Firebolt', min_damage=3, max_damage=6, mana_cost=2, **kwargs) -> None:
        super().__init__(name, min_damage, max_damage, mana_cost, **kwargs)

class ManeRestroe(Spell):
    def __init__(self, name='Firebolt', min_damage=0, max_damage=0, mana_cost=10, **kwargs) -> None:
        super().__init__(name, min_damage, max_damage, mana_cost, **kwargs)

class NecroticBlast(Spell):
    def __init__(self, name='Necroticblast', min_damage=3, max_damage=6, mana_cost=4, lifesteal=True, **kwargs) -> None:
        super().__init__(name, min_damage, max_damage, mana_cost, lifesteal, **kwargs)

class Frostbolt(Spell):
    def __init__(self, name='Frostbolt', min_damage=4, max_damage=8, mana_cost=2, **kwargs) -> None:
        super().__init__(name, min_damage, max_damage, mana_cost, **kwargs)

class Fireball(Spell):
    def __init__(self, name='Fireball', min_damage=10, max_damage=20, mana_cost=10, **kwargs) -> None:
        super().__init__(name, min_damage, max_damage, mana_cost, **kwargs)

class Icespear(Spell):
    def __init__(self, name='Icespear', min_damage=8, max_damage=16, mana_cost=5, **kwargs) -> None:
        super().__init__(name, min_damage, max_damage, mana_cost, **kwargs)

class Lightingstrike(Spell):
    def __init__(self, name='Firebolt', min_damage=10, max_damage=11, mana_cost=6, **kwargs) -> None:
        super().__init__(name, min_damage, max_damage, mana_cost, **kwargs)
