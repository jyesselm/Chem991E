import random


class WeaponFactory(object):
    def get_random_weapon(self):
        # returns a random weapons
        pass


class Weapon(object):
    def __init__(self, name, power):
        pass


    def attack(self):
        return random.randint(0, self.power)


class BareHands(Weapon):
    def __init__(self):
        Weapon.__init__(self, "bare hands", 1)


class WoodenStick(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a wooden stick", 3)


class RustySword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a rusty sword", 5)


class RegularSword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a regular sword", 10)


class IronSword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a iron sword", 20)


class MagicSword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "a magic sword", 50)


class Masamune(Weapon):
    def __init__(self):
        Weapon.__init__(self, "Masamune", 100)

