import random

import shield
import weapon

class FighterFactory(object):
    def __init__(self):
        self.names = "Squire Artur,Admiral Anselmus,Earl Rotgerius,Lady Ariana,Countess Ninette,Empress Mariel".split(",")

    def get_random_fighter(self):
        # returns random fighter with random name, random weapon and random shield
        pass

class Fighter(object):
    def __init__(self, name, weapon, shield):
        self.name = name
        self.health = 100
        pass

    def get_name(self):
        # returns name of the fighter
        pass

    def get_weapon_name(self):
        # returns name of the weapon
        pass

    def get_shield_name(self):
        # returns name of the shield
        pass

    def attack(self, other_fighter):
        attack_strength = self.weapon.attack()
        block_strength = other_fighter.block()

        if attack_strength > block_strength:
            damage_diff = attack_strength - block_strength
            print(self.name + " scores a brutal attack on "+other_fighter.get_name()+ " for " + str(damage_diff))
            other_fighter.takes_damage(attack_strength - block_strength)
        else:
            print(other_fighter.get_name() + " has blocked " + self.name + " puny attack!")

    def block(self):
        return self.shield.block()


    def takes_damage(self, damage):
        # substracts damage from health
        pass


    def is_defeated(self):
        # returns True if health is less then or equal to 0
        pass


    def status(self):
        return self.name + " has " + str(self.health) + " health remaining"


