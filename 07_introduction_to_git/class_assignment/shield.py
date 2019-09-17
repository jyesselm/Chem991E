import random


class Shieldactory(object):
    def get_random_shield(self):
        # returns a random shield
        pass


class Shield(object):
    def __init__(self, name, power):
        pass

    def block(self):
        return random.randint(0, self.power)


class BareHands(Shield):
    def __init__(self):
        Shield.__init__(self, "bare hands", 1)


class WoodenShield(Shield):
    def __init__(self):
        Shield.__init__(self, "a wooden shield", 3)


class RustyShield(Shield):
    def __init__(self):
        Shield.__init__(self, "a rusty shield", 5)


class RegularShield(Shield):
    def __init__(self):
        Shield.__init__(self, "a regular shield", 10)


class IronShield(Shield):
    def __init__(self):
        Shield.__init__(self, "iron shield", 20)


class MagicShield(Shield):
    def __init__(self):
        Shield.__init__(self, "magic shield", 50)


class Aegis(Shield):
    def __init__(self):
        Shield.__init__(self, "Aegis", 100)

