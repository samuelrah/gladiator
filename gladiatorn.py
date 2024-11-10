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

### VARIABLES FOR SPECIAL ATTACK ###
player_special_attack_damage = 60
enemy_special_attack_damage = 60

# Turn counters to track special attack usage
player_turns = 0
enemy_turns = 0

# Hit chance is between 1 and 100 percent. 
player_fist_hit_chance = 85
enemy_fist_hit_chance = 85
player_kick_hit_chance = 70
enemy_kick_hit_chance = 70
player_special_attack_hit_chance = 100
enemy_special_attack_hit_chance = 100

# Shield variables
player_shield_count = 2
enemy_shield_count = 2
player_shield_used = False
enemy_shield_used = False

os.system("cls")

def intro():
    print("Du är en gladiator i rome och du ska förbereda dig för att slås mot en annan gladiator,\n du måste vinna den här fighten för att överleva och för att försäkra din frihet.\n")

def vilken_attack():
    print("Det är din tur att attackera, Skriv numret eller namnet av attacken.")
    print("\nDinna tillgängliga attacker:")
    print("1 - Slå")
    print("2 - Kick")
    if player_turns >= 3:
        print("3 - Special attack")

def validate_attack_input():
    valid_attacks = ["1", "slå", "2", "kick"]
    if player_turns >= 3:
        valid_attacks.append("3")
        valid_attacks.append("special attack")
    
    while True:
        spelarens_attack = input().lower()
        if spelarens_attack in valid_attacks:
            return spelarens_attack
        else:
            print("Ogiltig input! Vänligen välj 1, 2, 3, eller skriv motsvarande attacknamn.")

def ask_use_shield():
    global player_shield_used
    global player_shield_count
    valid = ["1", "2"]
    
    if player_shield_count > 0:
        while True:
            use_shield = input("Vill du använda din sköld? 1 för ja, 2 för nej: ")
            if use_shield == "1" and not player_shield_used:
                player_shield_used = True
                player_shield_count -= 1
                print(f"Du använder din sköld! Du har {player_shield_count} sköldar kvar.")
                return              
            elif use_shield == "2":
                print("Du valde att inte använda din sköld.")
                return
            else:    
                print("Ogiltig input! Vänligen välj 1 för ja eller 2 för nej.")
    else:
        print("Du har inga sköldar kvar att använda.")

intro()
### GAME LOOP ###
while player_health > 0 and enemy_health > 0:
    vilken_attack()
    spelarens_attack = validate_attack_input()  # Use the validation function

    ### SPELAREN ATTACKERAR ###
    if (spelarens_attack == "1" or spelarens_attack == "slå"):
        print("Du gjorde ett slag")
        random_number = random.randint(1, 100)

        if (random_number >= player_fist_hit_chance):
            print("du missade.")
        else:
            if not enemy_shield_used:
                print("du träffade.")
                enemy_health -= player_fist_damage
                print(f"fienden har nu {enemy_health} hälsa.\n Det är motståndaren tur att attackera.")
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

    elif (spelarens_attack == "3" or spelarens_attack == "special attack"):
        print("Du använder din special attack!")
        enemy_health -= player_special_attack_damage
        print(f"Du träffade med din special attack! Fienden har nu {enemy_health} hälsa.")

    # Increment player's turn count
    player_turns += 1
    if player_turns > 3 and spelarens_attack == 3:
        player_turns = 0  # Reset turn counter after using special attack
    
    ### Ask to use shield before enemy attacks ###
    ask_use_shield()

    ### FIENDEN ATTACKERAR ### 
    print("Det är motståndarens tur att attackera")
    motståndaren_attak = random.choice([1, 2, 3,])
    slump_tal = random.randint(1, 100)

    if (motståndaren_attak == 1):
        print("Motståndaren försöker slå dig.")
        if (slump_tal <= enemy_fist_hit_chance):
            if not player_shield_used:
                print("och träffar")
                player_health -= enemy_fist_damage
                print(f"Du tar {enemy_fist_damage} i skada och du har {player_health} hälsopoäng kvar.")
            else:
                print("Du blockerade attacken med din sköld!")
                player_shield_used = False  # Reset shield status
        else:
            print("och missar")
    
    elif (motståndaren_attak == 2):
        print("Motståndaren försöker sparka dig.")
        if (slump_tal <= enemy_kick_hit_chance):
            if not player_shield_used:
                print("och träffar")
                player_health -= enemy_kick_damage
                print(f"Du tar {enemy_kick_damage} i skada och du har {player_health} hälsopoäng kvar.")
            else:
                print("Du blockerade attacken med din sköld!")
                player_shield_used = False  # Reset shield status
        else:
            print("och missar")
    
    elif (motståndaren_attak == 3 and player_turns == 3):
        print("Motståndaren använder sin special attack.")
        if (slump_tal <= enemy_special_attack_hit_chance):
            print("och träffar")
            player_health -= enemy_special_attack_damage
            print(f"Du tar {enemy_special_attack_damage} i skada och du har {player_health} hälsopoäng kvar.")
        else:
            print("och missar sin special attack!")

        # Enemy uses shield with a 50% chance
        if enemy_shield_count > 0 and not enemy_shield_used:
            if random.random() < 0.5:  # 50% chance to use shield
                print("Motståndaren använder sin sköld!")
                enemy_shield_used = True
                enemy_shield_count -= 1
                print(f"Motståndaren har {enemy_shield_count} sköldar kvar.")
            else:
                print("Motståndaren valde att inte använda sin sköld.")
                
    if player_health < 0 and enemy_health < 0:
        break

# Output the result of the game after the loop ends
if player_health <= 0:
    print("\nMotståndaren vann.")
elif enemy_health <= 0:
    print("\nDU VANN. du besegrade din motståndare och du är fri.")
