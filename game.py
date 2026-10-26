import random

end = 1
player_hp = 50
atk_dmg = 10

print( )

print("=========================")
print("  ...THE LOST PLANET...  ")
print("=========================")

print( )

print("You woke up in a field of an unknown planet, you cant remember who you are or")
print("where you came from all you know is that you are definitly injured with a huge")
print("gash on your arm. you assume you were a space traveller as there is a crashed")
print("ship behind you.")

print( )


"""
===============================
First question sequence
asks user what they want to use 
to fix their wound then adds 
health and runs the next
sequence
===============================
"""

while player_hp > 0 or end == 1: 

    print(f"HP: {player_hp}")
    print(f"ATK DMG: {atk_dmg}")

    print( )

    print("you have to fix your arm what should you do, should you:")

    print( )

    print("A. Use a bandage from the ship to stop the bleeding")
    print("B. wrap your arm with a alien leaf dripping green sap")
    print("C. eat a glowing red mushroom that has unkown effects")

    print( )

    option1 = str(input("which do you choose? "))

    print( )
    

    while option1 != "A" and option1 != "a" and option1 != "B" and option1 != "b" and option1 != "C" and option1 != "c": # fail safe to force user to select a valid option
        option1 = str(input("please select a valid option (A, B, OR C) "))

        print( )


    
    if option1 == "a" or option1 == "A":    # user chose bandage to patch wound

        print ("solid choice you stopped the bleeding and patched the wound (+25 hp)")

        player_hp = player_hp + 25

    elif option1 == "b" or option1 == "B": # user chose alien leaf to heal wound

        print ("you probably shouldnt press alien sap into an open wound, lucky for you however the sap has a healing") 
        print ("effect that magically healed your wound instanly and your arm feels better than ever (+50 hp)")

        player_hp = player_hp + 50

    elif option1 == "c" or option1 == "C": # user chose mushroom with a igh chance to die and low chance to live and obtain powerful powers

        effect = random.randint(1,50)
        if effect >= 10:
            print ("you should never eat an unknown mushroom, your throat closed up and you suffocated to death ")

            player_hp = 0

        else:
            print ("you should never eat an unknown mushroom, lucky for you this mushroom had a amazing effect, you")
            print ("feel powerfull (+75 hp +50 atk dmg)")

            player_hp = player_hp + 75
            atk_dmg = atk_dmg + 50

    print( )

    """
    ===============================
    Second question sequence
    asks user where they're gonna 
    go to find shelter
    ===============================
    """

    if player_hp > 0 :

        print( )

        print(f"HP: {player_hp}")
        print(f"DMG: {atk_dmg}")

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
        
        if option2 == "A" or option2 == "a": # user uses cuts down tree and gets burned by the sap

            print ("you cut down a tree, you come to find out the sap is toxic and burns your skin (-10 hp) you head to the ship instead")

            player_hp = player_hp - 10

        elif option2 == "B" or option2 == "b": # user crosses swamp to get to the cave with a low chance to get bit by a fish

            danger = random.randint(1,50)

            if danger >= 5:
                print ("you cross the swamp saftly and enter the cave, you find out the cave has a alien village in it")

            else:
                print ("you were bit by a alien fish (-10 hp) you enter the cave and find out the cave has a alien village in it")

                player_hp = player_hp - 10

            print( )

            option3 = str(input("the aliens greet you, they dont have mouths however, they offer you a bowl of alien stew, do you take it? "))

            print( )

            """
            ===============================
            user chooses if they take the 
            stew or not
            ===============================
            """
            
            if option3 == "yes": # user ate the stew and stole a magic sword

                print ("you ate the stew, it is very bitter but not bad, you become tired and signal to them you need a")
                print ("place to sleep, they take you to a empty hut and lead you to the bed to sleep. ")
                print ("inside the hut is a magic sword that is glowing green, you steal it. (+ 50 atk dmg)")

                atk_dmg = atk_dmg + 50  

            elif option3 == "no": # user refuses the stew and was attacked

                print ("they take great offense to you refusing their food, they start attacking you and you") 
                print ("run out of the cave, youj got hit by a few darts and stabbed by a spear (-50 hp) you stay in the ship instead.")

                player_hp = player_hp - 50

        elif option2 == "C" or option2 == "c": # user stays in ship

            print ("you decide to stay in your ship.")

        print ( )
    

    """
    ===========================
    third question sequence
    asks user wher the want to 
    go to find food, then runs 
    one of the adventures
    depending on their 
    choice
    =========================== 
    """

    if player_hp >= 0:
        print(F"HP: {player_hp}")
        print(f"ATK DMG: {atk_dmg} ")

        print( )

        print("You sleep through the night safetly. ")

        print( )

        print("you should probably gather food so you can eat")

        print( )

        print("A. go to the pond in the distance and fish with the rod you found on the ship")
        print("B. use your pistol to hunt the alien animals in the prarie")
        print("C. scavange the forest")

        print( )

        option4 = str(input("where do you go to get food? "))

        print( )

        while option4 != "A" and option4 != "a" and option4 != "B" and option4 != "b" and option4 != "C" and option4 != "c": # fail safe to force user to select a valid option
            option4 = str(input("please select a valid option (A, B, OR C) "))

            print ( )

        """
        ===========================
        runs the fishing minigame
        has a random chance to 
        catch a different fish 
        each fish adding differnt
        amounts of health
        ===========================
        """

        if option4 == "A" or option4 == "a":
            
            print("you head to the pond")

            print( )

            fish = str(input("do you fish? "))
            
            while fish == "yes" or player_hp <= 250:

                fish_chance = random.randint(1,8000)

                print( )

                print(F"HP: {player_hp}")
                print(f"DMG: {atk_dmg} ")

                print ( )

                if fish_chance <= 8000 and fish_chance > 5000:
                    print("you caught a small normal looking fish, you eat the fish, you ate the tiny fish                      (+0.5 hp)")
                    player_hp = player_hp + 0.5
                    
                elif fish_chance < 5001 and fish_chance > 2500:
                    print("you caught a medium sized fish, it has glowing blue eyes, you ate the weird fish                     (+1 hp)")

                    player_hp = player_hp + 1
                    
                elif fish_chance < 2501 and fish_chance > 1500:
                    print("you caught q large fish with, it is glowing red, you ate the ruby fish                               (+2 hp) ")

                    player_hp = player_hp + 2
                    
                elif fish_chance < 1501 and fish_chance > 750:
                    print("you caught a very large fish that is glowing a bright purple, you ate the void fish                  (+3 hp)")

                    player_hp = player_hp + 3
                    
                elif fish_chance < 751 and fish_chance > 250:
                    print("you caught a huge fish that has golden shimmering scales, you ate the golden fish                    (+5 hp)")

                    player_hp = player_hp + 5
                    
                elif fish_chance < 251 and fish_chance > 100:
                    print("you caught a giant fish, it has many fins and is glowing green, you ate the mutated fish             (+10 hp)")

                    player_hp = player_hp + 10
                    
                elif fish_chance < 101 and fish_chance > 50:
                    print("you caught a massive fish that is a iredecent blue you ate the blue shimmer fish                     (+20 hp)")

                    player_hp = player_hp + 20
                    
                elif fish_chance < 51 and fish_chance > 25:
                    print("you caught a colossal fish, it has three glowing white eyes, you ate the all seeing fish             (+30 hp)")

                    player_hp = player_hp + 30
                    
                elif fish_chance < 26 and fish_chance > 10:
                    print("you caught a giant shark that has 8 glowing eyes and glowing fins, you ate the spider shark          (+40 hp)")
                    
                    
                elif fish_chance < 11 and fish_chance > 5:
                    print("you caught a rainbow iredecent narwall that has a glowing rainbow tusk, you ate the rainbow narwall  (+50 hp)")

                    player_hp = player_hp + 50
                    
                elif fish_chance < 6 and fish_chance > 3:
                    print("you caught a fish wearing a golden crown, he is magnificant like a king, you ate the king fish       (+75 hp)")

                    player_hp = player_hp + 75
                  
                elif fish_chance < 4 and fish_chance > 1:
                    print("you caught a dark blue beluga with a crown that is translucent, you ate the abyss king beluga.       (+100 hp)")

                    player_hp = player_hp + 100
                   
                else:
                    print("YOU CAUGHT AN ANGEL FISH, IT HAS GLOWING WHITE WINGS AND A HALO! you dont")
                    print("eat it but it blesses you with some perks                                                            (+500 hp) (+250 atk dmg)")

                    player_hp = player_hp + 500
                    atk_dmg = atk_dmg + 250

                print( )
                
                if player_hp < 250:
                    fish = str(input("fish again? (click enter to fish again, type no to stop) "))
            
            if player_hp > 250: # stops user from over healing

                print ("you are very full and can not eat any more fish")
        
            """
            ===============================
            user chose to hunt and it goes
            badly causing the animal to 
            attack, user has to fight 
            the animal, this runs the 
            fight minigame
            ===============================
            """

        elif option4 == "B" or option4 == "b":
            print(f"HP: {player_hp}")
            print(f"DMG: {atk_dmg} ")

            print ("you shot at an animal")
            print ("unfortunately for you they have strong skin with large scales and the bullet richocheted off of its skin.")
            print ("the animal charged at you and and you dodged out of the way of its attack")
            print ("you find a ancient sword in the shrub that is rusted but should work (+50 atk dmg)")
            
            atk_dmg = atk_dmg + 50

            print ("you must fight the animal")
            print ( )

            beast_hp = 500

            beast_stam = 100

            charge = 0
            
            while beast_hp > 0 or player_hp > 0:

                print ("SCALED BEAST")

                print ( )

                print (f"HP: {beast_hp}")
                print (f"STAM: {beast_stam}")

                print ( )

                print (f"HP: {player_hp}")
                print (f"DMG: {atk_dmg}")
                print (F"CHARGE: {charge}")

                print ( )

                """
                ===============================
                user chooses their move
                ===============================
                """

                print ("A. stab  (quick attack the does 1x damage)")
                print ("B. slash (slow attack that does 1.5x damage)")
                print ("C. dodge (evade enemy attack which may tire out opponent)")
                print ("D. heal  (+30 hp)")
                print ("E. SUPER ATTACK (requires 100 charge)")

                print ( )

                duel = str(input("which do you choose? "))

                print ( )

                while duel != "A" and duel != "a" and duel != "B" and duel != "b" and duel != "C" and duel != "c" and duel != "D" and duel != "d" and duel != "E" and duel != "e": # fail safe to force user to select a valid option
                    duel = str(input("please select a valid option (A, B, C, OR D) "))
                    print( )

                if duel == "A" or duel == "a": # user chose quick light attack

                    print (f"you stabbed the beast (-{atk_dmg} HP)")

                    print( )

                    beast_hp = beast_hp - atk_dmg

                    charge = charge + 5

                elif duel == "B" or duel == "b": # user chose slow heavy attack

                    if beast_stam > 50: # beast reacts quickly and blocks attack

                        print ("it blocked your attack,")

                        print( )
                        
                    else: # beast is tired and cant block the attack

                        print(f"you slashed the animal, CRITICAL HIT (-{atk_dmg} x1.5)")   

                        beast_hp = beast_hp - (atk_dmg * 1.5)
                        beast_stam = 100  

                        charge = charge + 25

                        print( )

                elif duel == "C" or duel == "c": # user dodges attack tiring the beast

                    print ("you dodged making the beast tired (-25 stamina)")    

                    beast_stam = beast_stam - 25

                    print( )

                elif duel == "D" or duel == "d": # user healed

                    if player_hp >= 250:
                        print ("you are max HP")

                    else:
                        print ("you healed (+30 HP)")

                        player_hp = player_hp + 30

                        print ( )

                elif duel == "E" or duel == "e": # user chose super attack

                    if charge < 100: # attack not charged

                        print("not charged anough")

                    elif charge >= 100: # attack charged does extreme damage

                        print ("SUPER ATTACK (250 damage)")

                        beast_hp = beast_hp - 250
                        charge = 0

                        print( )

                if beast_hp >= 0:
                    print ("the animal attacked (-15 hp)")

                    player_hp = player_hp - 15

                    print ( )

            if beast_hp <= 0: # beast was killed, user eats to heal

                print ("you slaughtered the beast and now have food, you eat some to regain your power. (+ 100 hp)")
                
                player_hp = player_hp + 100

                print ( )

            """
            ===============================
            user chose to scavenge the 
            forest, user finds a tmeple
            and enter
            runs temple puzzle minigame
            ===============================
            """

        elif option4 == "C" or option4 == "c":
            print(F"HP: {player_hp}")
            print(f"DMG: {atk_dmg} ")

            print ("you walk into the forest and there is a temple with a 5 digit code locked door, you look around")
            print ("and see a sign that reads 'C063 15 8!', you have to decypher the text to get the code. ")

            code = 40320
            guess = ""

            while guess != code: # user has to guess the combination

                guess = int(input("enter the combination: "))

                print( )

                if guess != code: # user guessed wrong

                    print ("TRY AGAIN.")

                    print ( )

                else: # user guessed right

                    print ("CORRECT! ")

                    print ( )

                    print ("a large stone door lifts into the ceiling revealing another puzzle ")
                    print ("the puzzle reads '4 9R15M 5H1N35 7H15 W17H L16H7' ")
                    print ("there is a random list of letters which are: ")
                    print ("'A L P B R U O I Y H B N V G'")
                    print ("it also says '0N1Y 53V3N 13773R5 4R3 94R7 0F 7H3 C063'")

                    code2 = "roygbiv"
                    guess2 = ""

                    while guess2 != code2: # user has to guess the code

                        guess2 = str(input("enter the code: ")).lower()

                        print( )

                        if guess2 != code2: # user guessed wrong

                            print ("TRY AGAIN.")

                            print ( )

                        else: # user guessed right

                            print ("CORRECT! ")

                            print ( )
                            
                            """
                            ===============================
                            runs the falling section 
                            minigame, user has to choose 
                            between three sections 8 times
                            ===============================
                            """

                            print ("the floor lowers like an elevator descending ")
                            print ("you into a large cavern with glowing statues lighting up a path ")
                            print ("to a podium, you hit the bottom and start walking ")
                            print ("to the podium, except there is a bridge three sections wide and ")
                            print ("and 8 sections long, each section has a number on it, the first three are")

                            print ( )

                            print ("1 9 6")

                            print ( )

                            print ("there is a glowing word on the floor that reads 'F180N4CC1' ")

                            print ( )

                            guess3_1 = int(input("which do you jump on? "))

                            print ( )
                            
                            if guess3_1 == 1: # user guessed right
                                print ("1 2 5")
                                print ( )

                                guess3_2 = int(input("which do you jump on? "))

                                print ( )

                                if guess3_2 == 1: # user guessed right
                                    print ("7 2 9")

                                    print ( )

                                    guess3_3 = int(input("which do you jump on? "))

                                    print ( )

                                    if guess3_3 == 2: # user guessed right
                                        print ("4 3 8")

                                        print ( )

                                        guess3_4 = int(input("which do you jump on? "))

                                        print ( )

                                        if guess3_4 == 3: # user guessed right
                                            print ("5 6 7")

                                            print ( )

                                            guess3_5 = int(input("which do you jump on? "))

                                            print ( )

                                            if guess3_5 == 5: # user guessed right
                                                print ("9 8 7")

                                                print ( )

                                                guess3_6 = int(input("which do you jump on? "))

                                                print ( )

                                                if guess3_6 == 8: # user guessed right
                                                    print ("13 14 15")

                                                    print ( )

                                                    guess3_7 = int(input("which do you jump on? "))

                                                    print ( )

                                                    if guess3_7 == 13: # user guessed right
                                                        print ("21 24 27")

                                                        print ( )

                                                        guess3_8 = int(input("which do you jump on? "))

                                                        print ( )

                                                        if guess3_8 == 21: # user guessed right
                                                            print ("you reached the end and on the podium was a glowing white sword ")
                                                            print ("and a suit of metal armour")

                                                            print ( )

                                                            print ("you grab the sword and put on the armour (+100 ATK DMG +150 HP)")

                                                            atk_dmg = atk_dmg + 100
                                                            player_hp = player_hp + 150

                                                            print ( )

                                                            print ("you then leave the temple through the way you came ")

                                                        else: # user guessed wrong
                                                            print ("you chose wrong and fell into a spike pit")

                                                            player_hp = 0
                                                    else: # user guessed wrong
                                                        print ("you chose wrong and fell into a spike pit")

                                                        player_hp = 0
                                                else: # user guessed wrong
                                                    print ("you chose wrong and fell into a spike pit")

                                                    player_hp = 0
                                            else: # user guessed wrong
                                                print ("you chose wrong and fell into a spike pit")

                                                player_hp = 0
                                        else: # user guessed wrong
                                            print ("you chose wrong and fell into a spike pit")

                                            player_hp = 0
                                    else: # user guessed wrong
                                        print ("you chose wrong and fell into a spike pit")

                                        player_hp = 0

                                else: # user guessed wrong
                                    print ("you chose wrong and fell into a spike pit")

                                    player_hp = 0

                            else: # user guessed wrong
                                print ("you chose wrong and fell into a spike pit")

                                player_hp = 0

        print ( )

        print (F"HP: {player_hp}")
        print (f"DMG: {atk_dmg} ")

        print ( )

        print ("you head back to the ship to rest after your mini adventure")
        print ("but you come to find out your ship is not where you left it")
        print ("there is a note with coordinates on it. you head to the ")
        print ("coordinates and there is a giant alien building")
        print ("you head inside and you see many aliens working on your ship")
        print ("they are fixing you ship for you but it is not done yet")

        print ( )

        print ("3 HOURS LATER")

        print ( )

        print ("they finish the ship and walk up to you, they hold their hand")
        print ("out and you signal that you have nothing. they hold up a card")
        print ("that has the number '1500' on it, you signal again that you")
        print ("have nothing and they think for a second before handing you a")
        print ("a screen with a text box in it, they signal for you to type in it")
        print ("so you do so, you type 'i dont have any money' ")
        print ("it translates it to a alien language and it reads it out to them")
        print ("they grab the screen and type in it, the screen then reads")
        print ("'complete favour for us as payment. big thing eating our kind")
        print ("slay thing for us ship yours'")
        print ("you accept then ask where it is")
        print ("they give you a card with coordinates on it, they also hold out a slim body")
        print ("suit with a built in exo skeleton in it")
        print ("you put it on and it heavily increases your strength as it is made of a durable fabric")

        print ( )

        print ("(+100 HP +200 ATK DMG) you then head to the coordinates")

        player_hp = player_hp + 100
        atk_dmg = atk_dmg + 200

        print ( )

        print ("you near the coordinates and find a large mountain with a opening on the side")
        print ("you slowly enter the opening and there is a large door ")
        print ("you open the door and sneak in, you see a giant dragon like creature")
        print (" at the end of the hall, you try sneaking but it wakes up")
        print ("it instantly sees you and it trys attacking you with its large tail and you dodge out of the way")

        boss_hp = 5000
        boss_stam = 250

        charge = 0

        print ( )

        """
        ===============================
        runs final boss fight minigame
        ===============================
        """

        while boss_hp > 0 or player_hp > 0:
                print ("DRAGON BOSS")

                print ( )

                print (f"BOSS HP: {boss_hp}")
                print (f"BOSS STAM: {boss_stam}")

                print ( )

                print (f"HP: {player_hp}")
                print (f"DMG: {atk_dmg}")
                print (f"CHARGE: {charge}")

                print ( )

                """
                ===============================
                user chooses their move
                ===============================
                """

                print ("A. stab  (quick attack the does 1x damage)")
                print ("B. slash (slow attack that does 1.5x damage)")
                print ("C. dodge (evade enemy attack which may tire out opponent)")
                print ("D. heal  (+30 hp)")
                print ("E. SUPER ATTACK (requires 100 charge)")

                print ( )

                duel2 = str(input("which do you choose? "))

                print ( )

                while duel2 != "A" and duel2 != "a" and duel2 != "B" and duel2 != "b" and duel2!= "C" and duel2 != "c" and duel2 != "D" and duel2 != "d" and duel2 != "E" and duel2 != "e": # fail safe to force user to select a valid option
                    duel2 = str(input("please select a valid option (A, B, C, OR D) "))
                    print( )

                if duel2 == "A" or duel2 == "a": # user chose quick light attack

                    print (f"you stabbed the dragon (-{atk_dmg} HP)")

                    print( )

                    boss_hp = boss_hp - atk_dmg
                    charge = charge + 5

                elif duel2 == "B" or duel2 == "b": # user chose slow heavy attack
                    
                    if boss_stam > 50: # dragon reacts fast and blocks attack

                        print ("it blocked your attack,")

                        print( )
                        
                    else: # dragon is too tired to block attack

                        print(f"you slashed the dragon, CRITICAL HIT (-{atk_dmg} x1.5)")   

                        boss_hp = boss_hp - (atk_dmg * 1.5)
                        boss_stam = 250  

                        charge = charge + 25

                        print( )

                elif duel2 == "C" or duel2 == "c": # user chose to dodge

                    print ("you dodged making the dragon tired (-25 stamina)")    

                    boss_stam = boss_stam - 25

                    print( )

                elif duel2 == "D" or duel2 == "d": # user chose to heal

                    if player_hp >= 500:
                        print ("you are max HP")

                    else:
                        print ("you healed (+30 HP)")

                        player_hp = player_hp + 30
                    print ( )

                
                elif duel2 == "E" or duel2 == "e": # user chose super attack

                    if charge < 100: # attack not charged
                        
                        print ("not enough charge ")

                    elif charge > 99: # attack charged, it deals extreme damage

                        print ("SUPER ATTACK (250 damage)")

                        boss_hp = boss_hp - 250
                        charge = 0

                        print( )

                if boss_hp >= 0 and duel2 != "c": # dragon attacks with one of three outcomes
                    
                    boss_atk = random.randint(1,10)
                    
                    if boss_atk <= 10 and boss_atk > 3: # tail attack

                        print ("the dragon attacked with its tail (-25 hp)")

                        player_hp = player_hp - 25

                        print ( )

                    elif boss_atk == 1: # dragon misses tail attak=ck tiring itself out

                        print ("the dragon attacked with its tail but it missed (-50 stam)")

                        boss_stam = boss_stam - 50

                        print ( )
                    
                    elif boss_atk < 4 and boss_atk > 1: # dragon uses fire breath attack

                        print ("the dragon attacked with its fire breath (-60 hp)")

                        player_hp = player_hp - 60

                        print ( )
                    

if player_hp <= 0: # ends game when user dies
    print( )
    print("GAME OVER")
