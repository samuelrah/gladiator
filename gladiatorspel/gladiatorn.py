import random

### VARIABLES FOR HEALTH ###
player_health = 150
enemy_health = 150

### VARIABLES FOR THE FIST ###
player_fist_damage = 25
enemys_fist_damage = 25
# Hit chance is between 1 and 100 percent. 
player_fist_hit_chance = 70
enemys_fist_hit_chance = 70



print ("Du är en gladiator i rome och du ska förbereda dig för att slås mot en annan gladiator, du måste vinna den här fighten för att överleva och för att försäna din frihet.\n")

#print ("tryck på en tangent för att fortsätta.") 
#m.read_event()
print ("Det är din tur att attackera, du har ett val vill du 1- slå. skriv nummeret eller namnet av attacken.")
spelarens_attack = input().lower()


### SPELAREN ATTACKERAR ###
if (spelarens_attack == "1" or spelarens_attack == "slå"):
    print ("Du gjorde ett slag")
    random_number = random.randint(1, 100)


    if (random_number >= player_fist_hit_chance ):
        print("du missade.")
        
    elif (random_number <= player_fist_hit_chance):
        print("du träffade.")
        enemy_health -= player_fist_damage
        print(f"enemy has now {enemy_health} health.")

### FIENDEN ATTACKERAR ###
print ("Det är motstondarens tur att attackera")
motstondarens_attack = input().lower

if (motstondarens_attack == "1" or motstondarens_attack == "slå"):
    print ("motstondaren gjorde ett slag")
    random_number = random.randint(1, 100)

    if (random_number >= enemys_fist_hit_chance ):
        print("motstondaren missade.")
        
    elif (random_number <= enemys_fist_hit_chance):
        print("motstondaren träffade.")
        player_health -= enemys_fist_damage
        print(f"player has now {player_health} health.")

### SKRIV UT VEM SOM VANN ###