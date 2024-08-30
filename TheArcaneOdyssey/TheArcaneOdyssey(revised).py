import sys
import random
import playsound

team = []
good_guys = ['Grand Master Wizard', 'Ice Dragon', 'Battle Beast', 'King Cobra', 'WraithBlade', 'Zane', 'Dragon of Souls']
enemies = ['Dragon of darkness', 'Necromancer', 'Bakura', 'Goliath', 'Valak', 'Death Knight', 'The Grim Reaper']

def get_input(prompt, valid_responses=None):
    while True:
        response = input(prompt)
        if valid_responses is None or response.lower() in valid_responses:
            return response
        print("Invalid response, my warrior.")

def choose_option(options):
    for index, option in enumerate(options):
        print(f"{index}. {option}")
    choice = get_input("Choose an option: ", [str(i) for i in range(len(options))])
    return int(choice)

def encounter_enemy(enemy, options, fail_indices, success_message, fail_messages):
    print(f"You are face to face with {enemy}.")
    choice = choose_option(options)
    print(f"You chose to: {options[choice]}")
    if choice in fail_indices:
        print(fail_messages[choice])
        print("Game over")
        sys.exit()
    else:
        print(success_message)

def main():
    global team, good_guys, enemies

    name = input("What's your name?: ")
    good_guys.insert(0, name)
    print(f"Welcome, Young Warrior {name}, to the Arcane Odyssey.")

    input("You are face to face with Death Knight. He craves your life, and he will do anything to get it. What will you do? (press Enter to continue)")
    
    options = ['Draw your sword and fight!', 'Run away like a coward', 'Call backup']
    fail_messages = [
        "You almost had it, but you couldn't defeat the Death Knight alone.",
        "The Death Knight preyed on your weakness and kills you brutally."
    ]
    encounter_enemy('Death Knight', options, [0, 1], 
                    "You called the Grand Master Wizard to help you! You use your sword and he uses his Magical Staff to conquer that bastard.", 
                    fail_messages)

    print("\nYou have successfully made it past the Death Knight. Phew, that was very close.\n")
    print("If it wasn't for the Grand Master Wizard, who knows what would've happened.\n")

    while True:
        team_up = get_input("Would you like to ask the Grand Master Wizard to join your team? (type yes or no): ", ['yes', 'no'])
        if team_up.lower() == 'yes':
            print("\nThe Grand Master Wizard has decided to take pity on you and join.")
            team += good_guys[:2]
            break
        elif team_up.lower() == 'no':
            print("\nFoolish, but very well.")
            team += good_guys[:1]
            break

    print(f"Your team is... {team}\n")
    print("Your adventure continues...\n")

    input(f"You are leaving the Castle of the Death Knight. Things are looking up. The sun is back out and the darkness has lifted.\nThe journey is nowhere near over. Now it's on to the ruthless Necromancer. It's a long road. He lives in a cabin in the middle of the woods in Necromancia.\nHe's no ordinary Necromancer. He is unhinged, ruthless, and pure chaos.\nAs you're making your way to Necromancia, you get ambushed by the first wave of the Necromancer's army. \n*****BOOOOOM***** Three brain-controlled mage apprentices appear, looking to take out {team}. \nWhat is your next move? (press Enter to continue)")

    options = ['Attack!', 'Ignore them']
    fail_messages = [
        "You overlooked the mages and they obliterated you..."
    ]
    encounter_enemy('Three brain-controlled mage apprentices', options, [1], 
                    "Easy peasy, the mages were defeated.", 
                    fail_messages)

    print("That was a relief. Those mages came out of nowhere, and boy were they strong. I can only imagine how strong the Necromancer himself is...\nI hear that WraithBlade is on the way to Necromancia. Maybe he can help us!\n")
    print(good_guys[5] + "is the best swordsman in the whole odyssey. You'd think he's a bad guy but he's just misunderstood.\nHe is extremely powerful and lucky for us, he already hates the Necromancer for attacking his royal knight family. He killed his nephew...\nHe must be willing to help us. Let's go find him in the Poison Path.\n")

    while True:
        direction = get_input("We're approaching a split road...\nWhich way was Poison Path again? (Will you go left or right?) ", ['left', 'right'])
        if direction.lower() == 'right':
            print("\nYeah, we're going the right way. I see Poison Path in the distance!")
            break
        elif direction.lower() == 'left':
            print("\nDammit, this is the wrong way. Now we gotta fight these damn microraptors.")
            print("Let's finish these guys off and get to the right path real quick.")
            break

    print("\nMan I've heard crazy stories about WraithBlade.")
    print("I heard he cut someone's head off with his eyes blindfolded and in one swipe.\n")
    print("... don't wanna look at him the wrong way.\n")
    print("Man, it feels like we've been walking forever, we defeated the first wave of the Necromancer's army all the way back there, is it really gonna be this easy??")
    print("\nI think we're almost at Poison Path. Wait, what's that noise in the bushes? Let's get a little closer.\n*****BAM***** A Giant Boa Constrictor jumps out at you.")
    print(f"Boa: You must have a good reason to show face. What brings you here? Answer or I won't take it easy on you... {name}")

    options = ['Explain to Boa calmly', 'Ignore Boa']
    fail_messages = [
        "Boa: You dare ignore me? feel my wrath!"
    ]
    encounter_enemy('Boa', options, [1], 
                    "Boa: Ah, I see. You may pass and enter Poison Path.", 
                    fail_messages)

    print("Let's enter WraithBlades chamber.\n")

    print(f"WraithBlade: What do you peasants want {team}?\n")
    print("...\nI see, you'd like my help with the Necromancer. Very well.\nBut first, prove your worth to me by defeating me in battle!")

    options = ['Fight him straight on', 'Run', 'get his sword out of his possession', 'Convince him']
    fail_messages = [
        "That's not how you defeat a Legendary swordsman, rip young warrior",
        "You're a loser, go rot",
        "bruh.."
    ]
    encounter_enemy('WraithBlade', options, [0, 1, 3], 
                    "Smart, don't kill him though we need him.", 
                    fail_messages)

    print("WraithBlade: Very well, Young warrior. I will join your team.")
    team.append(good_guys[5])
    print(f"\nThe team is now {team}\n")
    print("...\nLet's go get that Necromancer! :)\n")

    input("Alright everyone... after 10 more dreadful miles. we've finally made it to Necromancia, let's do this. (press Enter to continue)")
    input("In order to take down the Necromacer I heard you have to have at least two people with you. And you also have two battle simutaneously.\nFlanks don't work.(press Enter to continue)")

    input("you are face to face with the Necromancer. What will you do?(press Enter to continue)")
    options = ['Battle together with all your might', 'Try to hit a flank']
    choice = choose_option(options)
    
    if choice == 0:
        if len(team) < 2:
            print("You don't have enough members in your team to defeat the Necromancer. You are overpowered and lose the battle.")
            print("Game over")
            sys.exit()
        else:
            print("HELL YEAH. You and your team fight valiantly and defeat the Necromancer!")
    else:
        print("That's not how you defeat the Necromancer, should've paid attention. RIP, young warrior.")
        print("Game over")
        sys.exit()

    print("\nWe did it.. Two down and 5 to go and we will finally restore light to the land. These guys have been causing chaos beyond comprehension for far too long.")
    print("\nAlthough we got rid of the Death Knight and the Necromancer, it only gets more difficult from here.")
    print("\nNow we must prepare for the Goliath.")

    summary_request = input("Would you like a summary of the Goliath? ").lower()
    if summary_request == 'yes':
        print("This beast is not just a mindless brute; it possesses a cruel intelligence, evident in the way it methodically destroys everything in its path, leaving nothing but ruin in its wake.\nVillages are razed, fields are scorched, and rivers are diverted by its wrath.\nThe Goliath is a force of nature, an unstoppable terror that leaves nothing but despair in its wake, a living nightmare that haunts the land and its people.")
    else:
        print("No summary provided.")

    print("\nThis beast is going to take a lot of manpower. I don't think we can win if we don't have at least 3 people on the team.")
    print("So far we have " + str(team))





















if __name__ == "__main__":
    main()

