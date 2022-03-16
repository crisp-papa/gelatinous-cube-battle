########################

import random
import math
import os

#################################
# Starting Values of New Player #
#################################

player = {
    'name' : 'Wizard',
    'class' : 'Wizard',
    'ac' : 10,
    'max hp' : 20,
    'current hp' : 20,
    'to hit' : 10,
    'level' : 1,
    'damage' : 9,
    'weapon' : 'Longsword',
    'chest armor' : 'Rags',
    'leg armor' : 'Rags',
    'foot armor' : 'Cloth Sandals'
}

player_2 = {
    'name' : 'Rogue',
    'class' : 'Rogue',
    'ac' : 10,
    'max hp' : 20,
    'current hp' : 20,
    'to hit' : 10,
    'level' : 1,
    'damage' : 9,
    'weapon' : "Dagger",
    'chest armor' : 'Leather',
    'leg armor' : 'Rags',
    'foot armor' : 'Cloth Sandals'
}
######################
# Enemy Dictionaries #
###################### 

enemies = {
    1 : 'Gremlin',
    2 : 'Underlings',
    3 : 'Rogue Group',
    4 : 'Dark Knight'
}

gremlin = {
    'name' : 'Gremlin',
    'ac' : 7,
    'current hp' : 10,
    'to hit' : 8,
    'level' : 1,
    'weapon' : 'claws'
}

underlings = {
    'name' : 'The Underlings',
    'ac' : 9,
    'current hp' : 15,
    'to hit' : 11,
    'level' : 2,
    'weapon' : 'tainted limbs'
}

rogue = {
    'name' : 'Rogue Group',
    'ac' : 12,
    'current hp' : 20,
    'to hit' : 13,
    'level' : 3,
    'weapon' : 'Blackened Knives',
}

dark_knight = {
    'name' : 'Dark Knight',
    'ac' : 14,
    'current hp' : 30,
    'to hit' : 15,
    'level' : 4,
    'weapon' : 'Morningstar',
}

enemy_weapons = {
    'claws' : 5,
    'tainted limbs' : 7,
    'Blackened Knives' : 9,
    'Morningstar' : 11
}

######################################
# Starting Values of Gelatinous Cube #
######################################

enemy = {
    'name' : 'Gelatinous Cube',
    'ac' : 10,
    'current hp' : 20,
    'to hit' : 10,
    'level' : 1,
    'weapon' : 'gooey body'
}

###############################################
# Various Weaponry for use in game eventually #
###############################################

weapon = {
    'War Axe' : 12,
    'Bush Hook' : 11,
    'Longsword' : 10,
    "Hunter's Fall" : 9,
    'Mace' : 8,
    'Sickle' : 7,    
    'Short Sword' : 6,
    'Dagger' : 5,
    'Fists' : 4,
}
   
############################
# Current Player Inventory #
############################

inventory = {
    'weapon' : player['weapon']
    }

##############################################
# Displays Current and Max Health for Player #
##############################################

def health():
    print("%i/%i HP" % (player['current hp'], player['max hp']))

##########################################################
# Displays character name and class, haven't used it yet #
##########################################################

def inventory():    
    print("Chest Armour: \t%s" % player['chest armor'])
    print("Leg Armour:   \t%s" % player['leg armor'])
    print("Foot Armour:  \t%s" % player['foot armor'])
    input()
    os.system('cls')


def status():
    print("%s the %s" % (player['name'], player['class']))

###############################################################
# Die Roller. Passing inputs creates the max die size. Handy. #
###############################################################

def die_roll(max_die):
    x = random.randint(1, max_die)
    return x

def start():
    print("A battle emerges.")
    battle()

def battle():
    if enemy['current hp'] >= 1 and player['current hp'] >= 1:
        versus()
    elif enemy['current hp'] <= 0:
        triumph()
    elif player['current hp'] <= 0:
        death()
    
def strike():
    print("You attack with your %s." % player['weapon'])
    roll = die_roll(20)
    if roll >= 20:
        print("SMMMMMAAAASSSSSH!!")
        hit_critical()
    elif roll >= enemy['ac']:
        hit_success()
    else:
        hit_miss(),

def destruct():
    print("You await your chance...")
    enemy_turn()
    if player['current hp'] > 0:
        print("You release destructive power!!")
        destructive_damage = die_roll(13)
        enemy['current hp'] -= destructive_damage 
        if destructive_damage <= 5:
            print(("Unfortunately, Revenge has wrought only %i damage.")
                % destructive_damage)
        elif destructive_damage <= 9 and destructive_damage >5:
            print("Revenge has wrought %i damage!" % destructive_damage)
        elif destructive_damage >= 10:
            print("Revenge has wrought %i damage!!" % destructive_damage)
    
    
def hit_critical():
    hit_damage = die_roll(10) * 2
    print("You critically hit %s for %i damage!!!" % (enemy['name'], hit_damage))
    enemy_hp = enemy['current hp']
    enemy_hp -= hit_damage
    enemy['current hp'] = enemy_hp
    enemy_turn()

def hit_success():
    hit_damage = die_roll(player['damage'])
    print("You hit %s for %i damage." % (enemy['name'], hit_damage))
    enemy_hp = enemy['current hp']
    enemy_hp -= hit_damage
    enemy['current hp'] = enemy_hp
    enemy_turn()

def hit_miss():
    print("You miss!!!")
    enemy_turn()

def enemy_turn():
    print("The %s lunges at you!!" % enemy['name'])
    roll = die_roll(20)
    if roll >= 20:
        print("Look out!!")
        enemy_critical_hit()
    elif roll >= player['ac']:
        print(("The %s strikes you with it's %s!" % 
            (enemy['name'], enemy['weapon'])))
        hit_damage = die_roll(enemy['to hit'])
        player['current hp'] -= hit_damage
        print("You are hit for %s damage!!" % hit_damage)
    else:
        print("You deftly avoid the attack!")

def enemy_critical_hit():
    print(("The %s comes down on you with the entire weight of it's body!" % enemy['name']))
    hit_damage = die_roll(10) * 2
    print("It crushes you for %i damage!!" % hit_damage)
    player['current hp'] -= hit_damage

def death():
    print("You've succumbed to your gooey death.")
 
def triumph():
    print("Congratulations, you've defeated the gelatinous beast.")

def versus():
    while enemy['current hp'] >= 1 and player['current hp'] >= 1:
        print("What do?")
        print("(S)trike with HONOR")
        print("(D)estruct with REVENGE")
        print("(I)nventory")
        health()
        choice = input(">")
        if (choice == "S" or choice == 's'):
            strike()
        elif (choice == "D" or choice == 'd'):
            destruct()
        elif (choice == "I" or choice == "i"):
            inventory()
        battle()

def endgame():
    end = 0
    while (end == 0):
        choice = input("Play again? Y/N\n\a>")
        if (choice == 'Y') or (choice == 'y'):
            os.system('cls')
            player['current hp'] = 20
            enemy['current hp'] = 20
            start()
        elif (choice == 'N') or (choice == 'n'):
            print("Be seeing you...")
            end = 1
        else:
            print("Try again.")
 
start()
endgame()
