import random
import os

### VARIABLES FOR HEALTH ###
player_health = 150
enemy_health = 150

### VARIABLES FOR THE FIST ###
player_fist_damage = 25
enemy_fist_damage = 25

### VARIABLES FOR THE KICK ###
player_kick_damage = 40
enemy_kick_damage = 40

# Hit chance is between 1 and 100 percent. 
player_fist_hit_chance = 85
enemy_fist_hit_chance = 85
player_kick_hit_chance = 70
enemy_kick_hit_chance = 70

# Shield variables
player_shield_count = 2
enemy_shield_count = 2
player_shield_used = False
enemy_shield_used = False

os.system("cls")
def intro():
    print("Du är en gladiator i rome och du ska förbereda dig för att slås mot en annan gladiator,\n du måste vinna den här fighten för att överleva och för att försäkra din frihet.\n")

def vilken_attack():
    print("Det är din tur att attackera, du har tre val: 1- slå, 2- kick, 3- sköld. Skriv nummeret eller namnet av attacken.")


intro ()
### GAME LOOP ###
while player_health > 0 and enemy_health > 0:
    vilken_attack()
    ### SPELAREN ATTACKERAR ###
    spelarens_attack = input().lower()
    if (spelarens_attack == "1" or spelarens_attack == "slå"):
        print("Du gjorde ett slag")
        random_number = random.randint(1, 100)

        if (random_number >= player_fist_hit_chance):
            print("du missade.")
        else:
            if not enemy_shield_used:
                print("du träffade.")
                enemy_health -= player_fist_damage
                print(f"fienden har nu {enemy_health} hälsa.")
            else:
                print("fienden blockerade din attack med sin sköld!")
                enemy_shield_used = False  # Reset shield status

    elif (spelarens_attack == "2" or spelarens_attack == "kick"):
        print("Du gjorde en spark")
        random_number = random.randint(1, 100)

        if (random_number >= player_kick_hit_chance):
            print("du missade")
        else:
            if not enemy_shield_used:
                print("du träffade.")
                enemy_health -= player_kick_damage
                print(f"fienden har nu {enemy_health} hälsa.")
            else:
                print("fienden blockerade din attack med sin sköld!")
                enemy_shield_used = False  # Reset shield status

    elif (spelarens_attack == "3" or spelarens_attack == "sköld"):
        if player_shield_count > 0 and not player_shield_used:
            print("Du använder din sköld!")
            player_shield_used = True
            player_shield_count -= 1
            print(f"Du har {player_shield_count} sköldar kvar.")
        else:
            if player_shield_used:
                print("Du har redan använt din sköld!")
            else:
                print("Du har inga sköldar kvar!")

    ### FIENDEN ATTACKERAR ###
    print("Det är motståndarens tur att attackera")
    motståndaren_attak = random.choice([1, 2, 3])
    slump_tal = random.randint(1, 100)

    if (motståndaren_attak == 1):
        print("motståndaren försöker slå dig.")
        if (slump_tal <= enemy_fist_hit_chance):
            if not player_shield_used:
                print("och träffar")
                player_health -= enemy_fist_damage
                print(f"du tar {enemy_fist_damage} i skada och du har {player_health} hälsopoäng kvar.")
            else:
                print("Du blockerade attacken med din sköld!")
                player_shield_used = False  # Reset shield status
        else:
            print("och missar")
    elif (motståndaren_attak == 2):
        print("motståndaren försöker sparka dig.")
        if (slump_tal <= enemy_kick_hit_chance):
            if not player_shield_used:
                print("och träffar")
                player_health -= enemy_kick_damage
                print(f"du tar {enemy_kick_damage} i skada och du har {player_health} hälsopoäng kvar.")
            else:
                print("Du blockerade attacken med din sköld!")
                player_shield_used = False  # Reset shield status
        else:
            print("och missar")
    elif (motståndaren_attak == 3):
        if enemy_shield_count > 0 and not enemy_shield_used:
            print("Motståndaren använder sin sköld!")
            enemy_shield_used = True
            enemy_shield_count -= 1
            print(f"Motståndaren har {enemy_shield_count} sköldar kvar.")
        else:
            if enemy_shield_used:
                print("Motståndaren har redan använt sin sköld!")
            else:
                print("Motståndaren har inga sköldar kvar!")

# Output the result of the game after the loop ends
if player_health <= 0:
    print("motståndaren vann.")
elif enemy_health <= 0:
    print("DU VANN. du besegrade din botståndare och du är fri.")