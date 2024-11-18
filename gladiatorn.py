import os
import random
import time
import colorama

from colorama import Fore, Style

    # Initialize Colorama
colorama.init(autoreset=True)

# Step 2: Define your sentence with colored words
word1 = Fore.RED + 'Motståndaren'
word2 = Fore.MAGENTA + 'Special attack'
word3 = Fore.BLUE + 'sköld'


### VARIABLES FOR HEALTH ###
player_health = 150
enemy_health = 150

### VARIABLES FOR THE ATTACKS ###
player_fist_damage = 25
enemy_fist_damage = 25
player_kick_damage = 40
enemy_kick_damage = 40
player_special_attack_damage = 60
enemy_special_attack_damage = 60

# Turn counters to track special attack usage
player_turns = 0
enemy_turns = 0

# Hit chances
player_fist_hit_chance = 85
enemy_fist_hit_chance = 85
player_kick_hit_chance = 65
enemy_kick_hit_chance = 65
player_special_attack_hit_chance = 100
enemy_special_attack_hit_chance = 100

# Shield variables
player_shield_count = 2
enemy_shield_count = 2
player_shield_used = False
enemy_shield_used = False

# Clear the console
os.system

# Define the menu options
menu = ("1", "2", "3")

def intro():
    print("\nDu är en gladiator i rome och du ska förbereda dig för att slås mot en annan gladiator,\ndu måste vinna den här fighten för att överleva och för att försäkra din frihet.\n")

def vilken_attack():
    print("Det är din tur att attackera, Skriv numret eller namnet av attacken.")
    print("\nDinna tillgängliga attacker:")
    print("1 - Slå")
    print("2 - Kick")
    if player_turns >= 3:
        print(f"3 - {word2}{Style.RESET_ALL}")

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
    

    if player_shield_count > 0:
        while True:
            use_shield = input(f"Vill du använda din {word3}{Style.RESET_ALL}? 1 för ja, 2 för nej: ")
            if use_shield == "1":
                if not player_shield_used:
                    player_shield_used = True
                    player_shield_count -= 1
                    print(f"Du använder din {word3}{Style.RESET_ALL}! Du har {player_shield_count} {word3}{Style.RESET_ALL} kvar.")
                    return True
                else:
                    print(f"Du har redan använt din {word3}{Style.RESET_ALL}.")
                    return False
            elif use_shield == "2":
                print(f"Du valde att inte använda din {word3}{Style.RESET_ALL}.")
                return False
            else:
                print("Ogiltig input! Vänligen välj 1 för ja eller 2 för nej.")
    else:
        print(f"Du har ingen {word3}{Style.RESET_ALL} kvar att använda.")
        return False

def start_game():
    global player_health, enemy_health, player_turns, enemy_turns, player_shield_used, enemy_shield_count
    
    player_health = 150
    enemy_health = 150
    player_turns = 0
    enemy_turns = 0
    player_shield_used = False
    enemy_shield_used = False

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
                    print(f"{word1}{Style.RESET_ALL} har nu {enemy_health} hälsa.\n Det är {word1}s{Style.RESET_ALL} tur att attackera.")
                else:
                    print(f"{word1}{Style.RESET_ALL} blockerade din attack med sin sköld!")
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
                    print(f"{word1}{Style.RESET_ALL} har nu {enemy_health} hälsa.")
                else:
                    print(f"{word1}{Style.RESET_ALL} blockerade din attack med sin sköld!")
                    enemy_shield_used = False  # Reset shield status

        elif (spelarens_attack == "3" or spelarens_attack == "special attack"):
            print(f"Du använder din {word2}{Style.RESET_ALL}!")
            enemy_health -= player_special_attack_damage
            print(f"Du träffade med din {word2}{Style.RESET_ALL}! {word1}{Style.RESET_ALL} har nu {enemy_health} hälsa.")

        # Increment player's turn count
        player_turns += 1
        if player_turns > 3 and spelarens_attack == "3":
            player_turns = 0 # Reset turn counter after using special attack
        
        ### Ask to use shield before enemy attacks ###
        ask_use_shield()

        ### FIENDEN ATTACKERAR ###
        print(f"Det är {word1}s{Style.RESET_ALL} tur att attackera")
        motståndaren_attak = random.choice([1, 2, 3] if enemy_turns >= 3 else [1, 2])
        slump_tal = random.randint(1, 100)

        if (motståndaren_attak == 1):
            print(f"{word1}{Style.RESET_ALL} försöker slå dig.")
            if (slump_tal <= enemy_fist_hit_chance):
                if not player_shield_used:
                    print("och träffar")
                    player_health -= enemy_fist_damage
                    print(f"Du tar {enemy_fist_damage} i skada och du har {player_health} hälsopoäng kvar.")
                else:
                    print(f"Du blockerade attacken med din {word3}{Style.RESET_ALL}!")
                    player_shield_used = False
            else:
                print("och missar")
        
        elif (motståndaren_attak == 2):
            print(f"{word1}{Style.RESET_ALL} försöker sparka dig.")
            if (slump_tal <= enemy_kick_hit_chance):
                if not player_shield_used:
                    print("och träffar")
                    player_health -= enemy_kick_damage
                    print(f"Du tar {enemy_kick_damage} i skada och du har {player_health} hälsopoäng kvar.")
                else:
                    print(f"Du blockerade attacken med din {word3}{Style.RESET_ALL}!")
                    player_shield_used = False
            else:
                print("och missar")
        
        elif (motståndaren_attak == 3 and enemy_turns >= 3):
            print(f"{word1}{Style.RESET_ALL} använder sin {word2}{Style.RESET_ALL}.")
            if (slump_tal <= enemy_special_attack_hit_chance):
                print("och träffar")
                player_health -= enemy_special_attack_damage
                print(f"Du tar {enemy_special_attack_damage} i skada och du har {player_health} hälsopoäng kvar.")
                break
            # Enemy uses shield with a 50% chance
            if enemy_shield_count > 0 and not enemy_shield_used:
                if random.random() < 0.5:  # 50% chance to use shield
                    print(f"{word1}{Style.RESET_ALL} använder sin sköld!")
                    enemy_shield_used = True
                    enemy_shield_count -= 1
                    print(f"{word1}{Style.RESET_ALL} har {enemy_shield_count} sköldar kvar.")
                else:
                    print(f"{word1}{Style.RESET_ALL} valde att inte använda sin sköld.")
      
        # Increment enemy's turn counter after each attack
        enemy_turns += 1

        if player_health < 0 and enemy_health < 0:
            break

    # Output the result of the game after the loop ends
    if player_health <= 0:
        print(f"\n{word1} vann.")
    elif enemy_health <= 0:
        print("\nDU VANN. du besegrade din motståndare och du är fri.")
    elif player_health <= 0 and enemy_health <= 0:
        print("Det blev oavgjort.")

# Start the menu loop
while True:
    print("\nMENY\n")
    print("1- Starta spelet")
    print("2- Regler")
    print("3- Credits")

    # Prompt user input
    user_input = input("Skriv numret av ett av valen: ")

    # Check if the input is valid
    if user_input in menu:
        if user_input == "1":
            time.sleep(1)
            start_game()  # Call the game start function
            break  # Exit the menu loop
        elif user_input == "2":
            print("\nDu är en gladiator i antika rom och du ska strax slås mot en annan gladiator.\nDet kan bara vara en vinnare, så ni kommer att slås till döds.\nGenom att vinna den hära kampen så kommer att du belönas med din frihet.\nBåde du och din motståndare kommer att ha 150 hälsopoäng.\nI det hära spelet så har du tre attacket, slå - där du använder dinna händer för att slå.\nKick - där du använder dinna fötter för att slå. Och sist din special attack.\nAlla dessa attacker har olika mycket skada och olika mycket träff chans.")
            print()
            print ("Attackernas skada och träff chans:\nslå - 25    85% \nKick - 40    65% \nSpecial attack - 60    100%")
            print()
            print("Det är viktigt att observera att du kan bara använda din special attack en gång per tre rundor\ndu och din motståndare har slagit varandra. Du och din motståndare kommer även att ha en sköld.\nSkölden kan bara användas två gånger och kommer att aktiveras efter att du har slagit ditt slag\nför att blockera motståndarens inkommande attack.")
        elif user_input == "3":
            print("\nCredits: Samuel Rahsepar.")
    else:
        print("Ogiltigt val! Försök igen.")


