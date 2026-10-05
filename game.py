import random

player_hp = 50
atk_dmg = 10

print( )
print("You woke up in a field of an unknown planet, you cant remember who you are or")
print("where you came from all you know is that you are definitly injured with a huge")
print("gash on your arm. you assume you were a space traveller as there is a crashed")
print("ship behind you.")
print( )

while player_hp > 0:

    print(f"HP:({player_hp})")
    print(f"ATK DMG:{atk_dmg}")
    print( )
    print("you have to fix your arm what should you do, should you:")
    print( )
    print("A. Use a bandage from the ship to stop the bleeding")
    print("B. wrap your arm with a alien leaf dripping green sap")
    print("C. eat a glowing red mushroom that has unkown effects")
    print( )

    option1 = str(input("which do you choose? "))

    print( )

    while option1 != "A" and option1 != "a" and option1 != "B" and option1 != "b" and option1 != "C" and option1 != "c":
        option1 = str(input("please select a valid option (A, B, OR C) "))
        print( )
        
    if option1 == "a" or option1 == "A":
        print ("solid choice you stopped the bleeding and patched the wound (+25 hp)")
        player_hp = player_hp + 25

    elif option1 == "b" or option1 == "B":
        print ("you probably shouldnt press alien sap into an open wound, lucky for you however the sap has a healing effect that magically healed your wound instanly and your arm feels better than ever (+50 hp)")
        player_hp = player_hp + 50

    elif option1 == "c" or option1 == "C":

        effect = random.randint(1,50)
        if effect >= 10:
            print ("you should never eat an unknown mushroom, your throat closed up and you suffocated to death ")
            player_hp = player_hp - 5000

        else:
            print ("you should never eat an unknown mushroom, lucky for you this mushroom had a amazing effect, you feel powerfull (+75 hp +50 atk dmg)")
            player_hp = player_hp + 75
            atk_dmg = atk_dmg + 50

    print( )

    if player_hp > 0 :
        print( )
        print(f"HP:{player_hp}")
        print(f"ATK DMG:{atk_dmg}")
        print( )
        print("now that you handled your wound you should probably find shelter")
        print( )
        print("A. go to the forest and build a shelter with the alien wood")
        print("B. camp in the cave you spot in the distance, but you have to cross a swamp to get to it")
        print("c. stay in the destoyed ship, it no longer flys but should work as a shelter for now")
        print( )

        option2 = str(input("where do you stay? "))
        print( )

        while option2 != "A" and option2 != "a" and option2 != "B" and option2 != "b" and option2 != "C" and option2 != "c":
            option2 = str(input("please select a valid option (A, B, OR C) "))
            print( )
        
        if option2 == "A" or option2 == "a":
            print ("you cut down a tree, you come to find out the sap is toxic and burns your skin (-10 hp) you head to the ship instead")
            player_hp = player_hp - 10

        elif option2 == "B" or option2 == "b":

            danger = random.randint(1,50)

            if danger >= 5:
                print ("you cross the swamp saftly and enter the cave, you find out the cave has a alien village in it")

            else:
                print ("you were bit by a alien fish (-10 hp) you enter the cave and find out the cave has a alien village in it")
                player_hp = player_hp - 10

            print( )
            option3 = str(input("the aliens greet you, they dont have mouths however, they offer you a bowl of alien stew, do you take it? "))
            print( )
            if option3 == "yes":
                print ("you ate the stew, it is very bitter but not bad, you become tired and signal to them you need a place to sleep, they take you to a empty hut and lead you to the bed to sleep. ")
            elif option3 == "no":
                print ("they take great offense to you refusing their food, they start attacking you and you run out of the cave, youj got hit by a few darts and stabbed by a spear (-50 hp) you stay in the ship instead.")
                player_hp = player_hp - 50

        elif option2 == "C" or option2 == "c":
            print ("you decide to stay in your ship.")
            
    if player_hp >= 0:
        
        print( )
        print("You sleep through the night safetly. ")
        print( )
        print("you should probably gather food so you can eat")
        print( )
        print("A. go to the pond in the distance and fish with the rod you found on the ship")
        print("B. use you pistol to hunt the alien animals in the prarie")
        print("C. scavange the forest")
        print( )
        option4 = str(input("where do you go to get food? "))

        if option4 == "A" or option4 == "a":
            
            print("you head to the pond")
            print( )
            fish = str(input("do you fish? "))
            
            while fish == "yes" or player_hp <= 250:

                fish_chance = random.randint(1,8000)
                print( )

                if fish_chance < 8000 and fish_chance > 5000:
                    print("you caught a small normal looking fish, you eat the fish, you ate the tiny fish                                     (+0.5 hp)")
                    player_hp = player_hp + 0.5
                    
                elif fish_chance < 5001 and fish_chance > 2500:
                    print("you caught a medium sized fish, it has glowing blue eyes, you ate the weird fish                                    (+1 hp)")
                    player_hp = player_hp + 1
                    
                elif fish_chance < 2501 and fish_chance > 1500:
                    print("you caught q large fish with, it is glowing red, you ate the ruby fish                                              (+2 hp) ")
                    player_hp = player_hp + 2
                    
                elif fish_chance < 1501 and fish_chance > 750:
                    print("you caught a very large fish that is glowing a bright purple, you ate the void fish                                 (+3 hp)")
                    player_hp = player_hp + 3
                    
                elif fish_chance < 751 and fish_chance > 250:
                    print("you caught a huge fish that has golden shimmering scales, you ate the golden fish                                   (+5 hp)")
                    player_hp = player_hp + 5
                    
                elif fish_chance < 251 and fish_chance > 100:
                    print("you caught a giant fish, it has many fins and is glowing green, you ate the mutated fish                            (+10 hp)")
                    player_hp = player_hp + 10
                    
                elif fish_chance < 101 and fish_chance > 50:
                    print("you caught a massive fish that is a iredecent blue you ate the blue shimmer fish                                    (+20 hp)")
                    player_hp = player_hp + 20
                    
                elif fish_chance < 51 and fish_chance > 25:
                    print("you caught a colossal fish, it has three glowing white eyes, you ate the all seeing fish                            (+30 hp)")
                    player_hp = player_hp + 30
                    
                elif fish_chance < 26 and fish_chance > 10:
                    print("you caught a giant shark that has 8 glowing eyes and glowing fins, you ate the spider shark                         (+40 hp)")
                    player_hp = player_hp + 40
                    
                elif fish_chance < 11 and fish_chance > 5:
                    print("you caught a rainbow iredecent narwall that has a glowing rainbow tusk, you ate the rainbow narwall                 (+50 hp)")
                    player_hp = player_hp + 50
                    
                elif fish_chance < 6 and fish_chance > 3:
                    print("you caught a fish wearing a golden crown, he is magnificant like a king, you ate the king fish                      (+75 hp)")
                    player_hp = player_hp + 75
                  
                elif fish_chance < 4 and fish_chance > 1:
                    print("you caught a dark blue beluga with a crown that is translucent, you ate the abyss king beluga.                      (+100 hp)")
                    player_hp = player_hp + 100
                   
                else:
                    print("YOU CAUGHT AN ANGEL FISH, IT HAS GLOWING WHITE WINGS AND A HALO! you dont eat it but it blesses you with some perks (+500 hp) (+250 atk dmg)")
                    player_hp = player_hp + 500
                    atk_dmg = atk_dmg + 250
                print( )
                fish = str(input("fish again? (click enter to fish again, type no to stop) "))

        if option4 == "B" or option4 == "b":
            print ("you shot at an animal")
            print ("unfortunately for you they have strong armour and the bullet richocheted off of its skin.")
            print ("the animal charged at you and and you dodged out of the way of its attack")
            print ("you find a ancient sword in the shrub that is rusted but should work (+50 atk dmg)")
            print ("")

                
if player_hp <= 0:
    print( )
    print("GAME OVER")