#import keyboard
helth = 150


print ("Du är en gladiator i rome och du ska förbereda dig för att slås mot en annan gladiator, du måste vinna den här fighten för att överleva och för att försäna din frihet.\n")

#print ("tryck på en tangent för att fortsätta.") 
#m.read_event()

print ("Det är din tur att attackera, du har tre val vill du 1- slå, 2- sparka, 3- special attack. skriv nummeret eller namnet av attacken.")
spelarens_attack = input().lower()

if (spelarens_attack == "1" or spelarens_attack == "slå"):
    print ("Du gorde ett slag")

elif (spelarens_attack == "2" or spelarens_attack == "sparka"):
    print ("Du gorde en spark")

elif (spelarens_attack == "3" or spelarens_attack == "special attack"):
    print ("Du gorde en special attack")



