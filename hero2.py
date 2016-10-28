hero_choice = raw_input("Soon after you begin your journey, you come across a precipice. From below you hear a low grumble. The ground begins to shake and a dragon emerges from the deep. He towers above you. What do you do? RUN or FIGHT?")
if hero_choice.upper() != "RUN" and hero_choice.upper() != "FIGHT": #still does not work!
    print hero_choice
    exit_choice = raw_input("You can always just quit and escape your problems by not making a choice. Type EXIT to quit")
    if (exit_choice == "EXIT"):
        print("Too bad, goodbye")
        sys.exit()
        #need to make another option