import random
import math
def main():
    p1,p2 = choose_mon()
    first, second = moves_first(p1,p2)

    while True: #p1.hp>0 and p2.hp>0:
        if first == p1:
          print("Player 1's turn: ")
          first_move = choose_move(p1)
          damage = damage_calc(first_move, p1, p2)
          p2.hp = new_health(damage,p2)
          if p2.hp<=0:
            print("Player 1 wins")
            break
          print("Player 2's turn: ")
          second_move = choose_move(p2)
          damage = damage_calc(second_move, p2, p1)
          p1.hp = new_health(damage,p1)
          if p1.hp<=0:
            print("Player 2 wins")
            break
        else:
          print("Player 2's turn: ")
          second_move = choose_move(p2)
          damage = damage_calc(second_move, p2, p1)
          p1.hp = new_health(damage,p1)
          if p1.hp<=0:
            print("Player 2 wins")
            break
          print("Player 1's turn: ")
          first_move = choose_move(p1)
          damage = damage_calc(first_move, p1, p2)
          p2.hp = new_health(damage,p2)
          if p2.hp<=0:
            print("Player 1 wins")
            break







class Move:
    #Class that makes the moves for each pokemon
    def __init__(move, name, power, type, accuracy, attack_type):
        move.power = power
        move.type = type
        move.acc = accuracy
        move.attack = attack_type
        move.name = name
        '''move.special = special_effect'''
        #decided to hold off on special effects for now
dazzling_gleam = Move("dazzling gleam", 80, "Fairy", 100, "special")
mystical_fire = Move("mystical fire", 75, "Fire", 100, "special" )
magical_leaf = Move("magical leaf", 60, "Grass", 100, "special")
psychic = Move("psychic", 90, "Psychic", 100, "special")
stone_edge = Move("stone edge", 100, "Rock", 80, "physical")
earthquake = Move("earthquake", 100, "Ground", 100, "physical")
crunch = Move("crunch", 80, "Dark", 100, "physical")
fire_blast = Move("fire blast", 110, "Fire", 85, "special")
flamethrower = Move("flamethrower", 90, "Fire", 100, "special")
hydro_pump = Move("hydro pump", 110, "Water", 80, "special")
dark_pulse = Move("dark pulse", 80, "Dark", 100, "special")
energy_ball = Move("energy ball", 90, "Grass", 100, "special")
shadow_claw = Move("shadow claw", 70, "Ghost", 100, "physical")
blizzard = Move("blizzard", 110, "Ice", 70, "special")
surf = Move("surf", 90, "water", 100, "special")
shadow_ball = Move("shadow ball", 80, "Ghost", 100, "special")
gunk_shot = Move("gunk shot", 120, "Poison", 80, "physical")
poison_jab = Move("poison jab", 80, "Poison", 100, "physical")
strength = Move("strength", 80, "Normal", 100, "physical")
dragon_claw = Move("dragon claw", 80, "Dragon", 100, "physical")
focus_blast = Move("focus blast", 120, "Fighting", 70, "special")
leaf_storm = Move("leaf storm", 130, "Grass", 90, "special")
thunderbolt = Move("thunderbolt", 90, "Electric", 100, "special")
aura_sphere = Move("aura sphere", 80, "Fighting", 100, "special")
sludge_bomb = Move("sluge bomb", 90, "Poison", 100, "special")

class Pokemon:
    #class that makes the pokemon with their stats typing and moves
  def __init__(mon, name, type1, type2, health, atk, defence, spatk, spdef, spd, move1, move2, move3, move4):
    #'mon' is an abreviation of Pokemon
    mon.type = type1, type2
    mon.type1 = type1
    mon.type2 = type2
    mon.name = name
    mon.hp = health
    mon.atk = atk
    mon.defence = defence
    mon.spatk = spatk
    mon.spdef = spdef
    mon.spd = spd
    mon.move1 = move1
    mon.move2 = move2
    mon.move3 = move3
    mon.move4 = move4
    mon.all = name, type1, type2, health, atk, defence, spatk, spdef, spd
alcremie = Pokemon("Alcremie", "Fairy","none", 240, 125, 155, 225, 247, 133, dazzling_gleam, mystical_fire, magical_leaf, psychic)
tyranitar = Pokemon("Tyranitar", "Rock", "Dark", 310, 273, 225, 195, 205, 127, stone_edge, earthquake, crunch, fire_blast)
vulpix = Pokemon("Vulpix", "Fire", "none", 186, 87, 85, 105, 135, 135, flamethrower, fire_blast, dark_pulse, energy_ball)
psyduck = Pokemon("Psyduck", "Water","none", 210, 109, 101, 135, 105, 115, psychic, hydro_pump, shadow_claw, blizzard)
vaporeon = Pokemon("Vaporeon", "Water", "none", 370, 135, 125, 225, 195, 135, hydro_pump, blizzard, surf, shadow_ball)
grimer = Pokemon("Grimer", "Poison", "none", 270, 165, 105, 85, 105, 55, gunk_shot, poison_jab, strength, fire_blast)
salamence = Pokemon("Salamence", "Dragon", "Flying", 300, 275, 165, 225, 165, 205, dragon_claw, crunch, earthquake, flamethrower)
jynx = Pokemon("Jynx", "Ice","Psychic", 240, 105, 75, 235, 195, 195, blizzard, psychic, focus_blast, shadow_ball)
rotom_mow = Pokemon("Rotom Mow", "Electric", "Grass", 210, 135, 219, 215, 219, 177, leaf_storm, thunderbolt, shadow_ball, dark_pulse)
lucario = Pokemon("Lucario", "Steel","Fighting", 250, 225, 145, 235, 145, 185, aura_sphere, stone_edge, earthquake, shadow_claw)
gengar = Pokemon("Gengar", "Ghost","Poison",230, 135, 125,265, 155,225, sludge_bomb, shadow_ball, dark_pulse, thunderbolt)
#pokemon to add: 
list_of_mons = [alcremie, tyranitar,vulpix, psyduck, vaporeon, grimer, salamence, jynx, rotom_mow, lucario, gengar]

def poke_display(list):
    for mon in list:
        if mon.type2 == "none":
            print("Pokemon: {0} Type: {1}".format(mon.name, mon.type1))
        else:
            print("Pokemon: {0} Type: {1} {2}".format(mon.name, mon.type1,mon.type2))
        print("Moves: {0}, {1}, {2}, {3}\n".format(mon.move1.name,mon.move2.name,mon.move3.name,mon.move4.name))

def choose_mon():
    poke_display(list_of_mons)
    p1 = input("player 1: choose your Pokemon: ")
    p2 = input("player 2: choose your Pokemon: ")
    p3 = p1.lower()
    p4 = p2.lower()
    #print(p1.lower(),p2.lower())
    for mon in list_of_mons:
        if p3 == mon.name.lower():
            p1 = mon
        if p4 == mon.name.lower():
            p2 = mon

    return(p1,p2)

def moves_first(mon1, mon2):
    if mon1.spd>mon2.spd:
        print("Player 1 goes first")
        return(mon1,mon2)
    else:
        print("player 2 goes first")
        return(mon2,mon1)

def damage_roll():
    num = random.randint(85,100)
    num = num/100
    return(num)

def critical():
    num = random.randint(1,24)
    
    if num == 24:
        crit = 1.5
    else:
        crit = 1.0
    
    return(crit)

def damage_calc(move, attacking_mon, defending_mon):
    super_effective_dict = {
    'Normal':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':0.5, 'Ghost':0.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
    'Fire': {'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 2.0, 'Water': 0.5, 'Electric':1.0, 'Ice':2.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':2.0, 'Rock':0.5, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':2.0,'Fairy':1.0}, 
    'Water': {'none':1.0,'Normal':1.0, 'Fire': 2.0, 'Grass': 0.5, 'Water': 0.5, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':2.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':2.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':1.0,'Fairy':1.0}, 
    'Grass': {'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 0.5, 'Water': 2.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':0.5, 'Ground':2.0, 'Flying':0.5, 'Psychic':1.0, 'Bug':0.5, 'Rock':2.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
    'Electric':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 0.5, 'Water': 2.0, 'Electric':0.5, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':0.0, 'Flying':2.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':1.0, 'Steel':1.0,'Fairy':1.0},
    'Ice':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 2.0, 'Water': 0.5, 'Electric':1.0, 'Ice':0.5, 'Fighting':1.0,'Poison':1.0, 'Ground':2.0, 'Flying':2.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':2.0, 'Ghost':1.0, 'Dragon':2.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
    'Fighting':{'none':1.0,'Normal':2.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':2.0, 'Fighting':1.0,'Poison':0.5, 'Ground':1.0, 'Flying':0.5, 'Psychic':0.5, 'Bug':0.5, 'Rock':2.0, 'Ghost':0.0, 'Dragon':0.5, 'Dark':2.0, 'Steel':2.0,'Fairy':0.5},
    'Poison':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 2.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':0.5, 'Ground':0.5, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':0.5, 'Ghost':0.5, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.0,'Fairy':2.0},
    'Ground':{'none':1.0,'Normal':1.0, 'Fire': 2.0, 'Grass': 0.5, 'Water': 1.0, 'Electric':2.0, 'Ice':1.0, 'Fighting':1.0,'Poison':2.0, 'Ground':1.0, 'Flying':0.0, 'Psychic':1.0, 'Bug':0.5, 'Rock':2.0, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':2.0,'Fairy':1.0},
    'Flying':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 2.0, 'Water': 1.0, 'Electric':0.5, 'Ice':1.0, 'Fighting':2.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':2.0, 'Rock':0.5, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
    'Psychic':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':2.0,'Poison':2.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':0.5, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':0.5, 'Dark':0.0, 'Steel':0.5,'Fairy':1.0},
    'Bug':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 2.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':0.5,'Poison':0.5, 'Ground':1.0, 'Flying':0.5, 'Psychic':2.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':0.5, 'Dragon':1.0, 'Dark':2.0, 'Steel':0.5,'Fairy':0.5},
    'Rock':{'none':1.0,'Normal':1.0, 'Fire': 2.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':2.0, 'Fighting':0.5,'Poison':1.0, 'Ground':0.5, 'Flying':2.0, 'Psychic':1.0, 'Bug':2.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':1.0},
    'Ghost':{'none':1.0,'Normal':0.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':2.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':2.0, 'Dragon':1.0, 'Dark':0.5, 'Steel':1.0,'Fairy':1.0},
    'Dragon':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':2.0, 'Dark':1.0, 'Steel':0.5,'Fairy':0.0},
    'Dark':{'none':1.0,'Normal':1.0, 'Fire': 1.0, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':0.5,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':2.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':2.0, 'Dragon':1.0, 'Dark':0.5, 'Steel':1.0,'Fairy':0.5},
    'Steel':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 0.5, 'Water': 0.5, 'Electric':1.0, 'Ice':2.0, 'Fighting':1.0,'Poison':1.0, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':2.0, 'Ghost':1.0, 'Dragon':1.0, 'Dark':1.0, 'Steel':0.5,'Fairy':2.0},
    'Fairy':{'none':1.0,'Normal':1.0, 'Fire': 0.5, 'Grass': 1.0, 'Water': 1.0, 'Electric':1.0, 'Ice':1.0, 'Fighting':2.0,'Poison':0.5, 'Ground':1.0, 'Flying':1.0, 'Psychic':1.0, 'Bug':1.0, 'Rock':1.0, 'Ghost':1.0, 'Dragon':2.0, 'Dark':2.0, 'Steel':0.5,'Fairy':1.0},}
    power = move.power
    move_type = move.type
    attack_type = move.attack
    attacking_type1 = attacking_mon.type1
    attacking_type2 = attacking_mon.type2
    defending_type1 = defending_mon.type1
    defending_type2 = defending_mon.type2
    super_effective = super_effective_dict[move.type][defending_type1]*super_effective_dict[move.type][defending_type2] #checks if the move will do extra damage based on type weaknesses
    atk = attacking_mon.atk
    spatk = attacking_mon.spatk
    defence = defending_mon.defence
    spdef = defending_mon.spdef
    if move.type == attacking_type1 or move.type == attacking_type2: #if the move type and pokemon type are the same it does 1.5x damage
        stab = 1.5
    else:
        stab = 1
    rand = damage_roll() #random number between .85 and 1
    crit = critical() #1 in 24 chance to deal 1.5x damage
    dodge = dodge_chance(move)

    if attack_type == "special":
        damage = (((42*power*(spatk/spdef))/50)+2)*super_effective*stab*crit*rand*dodge #the actual calculation
    else:
        damage = (((42*power*(atk/defence))/50)+2)*super_effective*stab*crit*rand*dodge #the actual calculation
    if dodge == 0:
      print("The attack missed")
    else:
      if crit == 1.5:
        print("Its a Critical Hit! ")
      if super_effective>1:
        print("It's Super Effective")
      elif super_effective <1:
        print("It's Not Very Effective")
      print("It did {0} damage".format(math.trunc(damage)))
    return(math.trunc(damage))

def choose_move(attacking_mon):
    move1 = attacking_mon.move1
    move2 = attacking_mon.move2
    move3 = attacking_mon.move3
    move4 = attacking_mon.move4
    list_of_moves = [move1,move2,move3,move4]
    print("{0}, {1}, {2}, {3}".format(move1.name, move2.name, move3.name, move4.name))
    choice = input("what move do you want to use? ")
    choice = choice.lower()
    for move in list_of_moves:
        if choice == move.name:
            choice = move
    return(choice)
    
def new_health(damage, recieveing_mon):
    remaining = recieveing_mon.hp-damage
    if remaining<0:
        remaining = 0
    print("{0} has {1} health remaining".format(recieveing_mon.name,remaining))
    return(remaining)

def dodge_chance(move):
    hit_chance = move.acc
    rand = random.randint(1,100)
    if rand>hit_chance:
        hit = 0
    else:
        hit = 1
    return(hit)

#damage_calc(fire_blast, vulpix, rotom_mow)

#choose_move(alcremie)


main()