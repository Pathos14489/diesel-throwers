# The game starts here.
define scoots = Character("Scootaloo")
define echo = Character("Echo")
define wh = Character("Warm Heart")

image start_sun = Image("bgs/start_sun.png")
image start_sun_2 = Image("bgs/start_sun_2.png")

image scoots chill = Image("scootaloo/scoots_smile.png")
image scoots grin = Image("scootaloo/scoots_grin.png")

image wh smile = Image("warmheart/warmheart_smile.png")
image wh chill = Image("warmheart/warmheart_skeptical.png")
image wh curious = Image("warmheart/warmheart_curious.png")
image wh skeptical = Image("warmheart/warmheart_skeptical.png")

label start:

    scene start_sun

    "You wake up as the sun's first light hits you through the open window."

    "A cursory glance at your clock does both the job of reminding you you have school, and that it's in an hour."

    "I sigh, popping my neck and sitting up in bed. I glance over at the clock at try to levitate it with my magic."

    "You twirl it in midair a little, nearly dropping it but keeping it aloft, albeit wobbly."

    scene start_sun_2

    show scoots chill at right

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

    hide scoots grin

    echo "If you beat me up it'd be murder. I might, might have a chance with a newborn foal! Murder, I said!"

    show wh curious at right

    wh "Murder, you say?"

    "She gives you a curious look."

    echo "Murder I said. I said murder."

    wh "I see."

    show wh skeptical

    "She smiles bemusedly."

    wh "If you're talking about that breath of yours, I certainly agree. Make sure to brush up a little extra after breakfast, 'kay?"

    echo "Okay."

    "I shrug, yawning and hopping out of bed."

    show wh curious

    wh "How are you liking it here, by the way? Scootaloo hasn't been too hard on you, has she?"

    "I shrug."

    echo "I mean yeah. And she's cool, she only sometimes threatens to strangle me."

    "She nods."

    wh "Good. I'm glad you're getting along."

    show wh skeptical

    "She smirks."

    wh "I wouldn't get too friendly, though. She'll castrate you."

    return
