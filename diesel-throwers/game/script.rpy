# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

image start_sun = Image("start_sun.png")
define scoots = Character("Scootaloo")
image scoots chill = Image("scoots_smile.png")

label start:

    scene start_sun

    "You wake up as the sun's first light hits you through the open window."

    "A cursory glance at your clock does both the job of reminding you you have school, and that it's in an hour."

    "I sigh, popping my neck and sitting up in bed. I glance over at the clock at try to levitate it with my magic."

    "You twirl it in midair a little, nearly dropping it but keeping it aloft, albeit wobbly."

    show scoots chill

    scoots "Wow. You've gotten better."

    return
