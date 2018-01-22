# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

image start_sun = Image("start_sun.png")
define scoots = Character("Scootaloo")
image scoots chill = Image("scoots_smile.png")
define echo = Character("Echo")
image scoots grin = Image("scoots_grin.png")

label start:

    scene start_sun

    "You wake up as the sun's first light hits you through the open window."

    "A cursory glance at your clock does both the job of reminding you you have school, and that it's in an hour."

    "I sigh, popping my neck and sitting up in bed. I glance over at the clock at try to levitate it with my magic."

    "You twirl it in midair a little, nearly dropping it but keeping it aloft, albeit wobbly."

    show scoots chill

    scoots "Wow. You've gotten better."

    "I grin, happy with the results while glancing over to the voice."

    echo "Yah think?"

    show scoots grin

    "Your room partner, an orange pegasus with purpley hair - you think you remember her name, Scootaloo? - smiles back with a tired grin."

    scoots "That's good. If anypony tries to beat you up, at least you won't die in the first round."

    show scoots chill

    "She yawns again."

    scoots "Well, I'm gonna grab the first shower. Don't go hunting for any panties while I'm out. Just because this was the only open room doesn't mean you can do whatever you want."

    echo "...Okay. So. Lets say I did do this. What would happen?"

    show scoots grin

    "She grins in an unsettling way."

    scoots "You know, there's a reason Ms. Heart was okay with you being in a filly's room. I've beat up more colts than anypony here."

    "She begins to walk out the door, but pauses."
    
    scoots "Unicorns, too."

    "She walks out."

    return
