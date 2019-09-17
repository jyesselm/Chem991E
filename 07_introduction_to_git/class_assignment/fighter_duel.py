import fighter

def welcome_fighter_to_arena(fighter):
    msg  = "Welcome " + fighter.get_name() + " to the arena! "
    msg += fighter.get_name() + " is equiped with weapon: " + fighter.get_weapon_name()
    msg += " and shield: " + fighter.get_shield_name()
    print(msg)

"""

ff = fighter.FighterFactory()
fighter_1 = ff.get_random_fighter()

while 1:
    fighter_2 = ff.get_random_fighter()
    if fighter_1.get_name() != fighter_2.get_name():
        break

welcome_fighter_to_arena(fighter_1)
welcome_fighter_to_arena(fighter_2)

round_count = 1
while 1:
    print("Round " + str(round_count ) + ", Fight!")
    fighter_1.attack(fighter_2)
    if fighter_2.is_defeated():
        print(fighter_2.get_name() + " has been defeated!")
        exit()
    fighter_2.attack(fighter_1)
    if fighter_1.is_defeated():
        print(fighter_1.get_name() + " has been defeated!")
        exit()
    round_count += 1
    print fighter_1.status() + ", " + fighter_2.status()
    print ("\n")
    
"""