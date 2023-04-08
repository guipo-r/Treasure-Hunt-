print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Hunt!.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
name = input(f"\nIt sounds ridiculous at this point, but I forgot your name, could you refresh my memory? What's your name? ")
print(f"\n Great, {name}! Let's keep going. Where was I? Ah! Here it is: \n\n")
q1 = input(f"\n\nAfter all you've been through, you're almost there. The treasure is near, and you can feel it in the air. You can sense it in your trembling skin. It's getting dark here and the treasure map is practically debris, so this is up to you know. Let's see if you can trust your instincts. In which direction would you continue your quest? Left or right? \n")

if q1 == 'Left' or q1 == 'left':
  print(f"\nWell, that's an encouraging start; you've reached the misty lake, you must cross it to continue your journey.")
  q2 = input(f"Will you swim across it or will you wait for the lake warden's boat at the shore? Type 'swim' or 'boat': \n")
else:
  print(f"\nI have good news and bad news. Let's start with the good news: you've finally reached the end of this seemingly neverending journey. Bad news is this ending turned out to be DEATH BY IMPALEMENT, since after falling for a few seconds down an obscure hole, you found out that there were huge wooden spikes waiting for you at the bottom. Nice instincts, huh! \nG A M E  O V E R")

if q2 == 'swim':
  print(f"\nReally??? You were given the choice to keep your clothes dry and you chose to swim through a misty and unknown lake? Let me tell you that you have truly shitty instincts. No need to tell you that you died full of pain and suffering, devoured by assassin sea otters (it's a salty lake, okay?) equiped with poisonous katanas. And worst of all, you died on WET CLOTHES. So there's that:\nG A M E  O V E R")
elif q2 == 'boat':
  print(f"\n\nAfter a few peaceful minutes admiring darkness from the shore, you heard the sound of the lake warden rowing his boat, whistling some ancient tunes, or maybe it was 'Friday - Rebecca Black.mp3'. He accepted to take you to the other side of the lake, with only one condition: he would choose the playlist. By the time you reached the other shore, you were almost BFFs with the warden, I mean, what were the odds of him being a Swiftie, right?\n")
  print(f"\nThe warden waved goodbye and returned to the lake's dock with his boat. Alone again, happiness is short lived, you know that. Let's focus on what's important again, being wealthy enough to have your own reality show called 'Keeping up with {name}'. So, yep, you've crossed the lake, and you walked inside a lone, suspicious cabin located at the edge of the woods. Inside, instead of what we were all expecting, there are no weird animal head trophies hanging on the wall, nor a wacko waving an axe in the air, what you find is just a warm and comfy room. By now, you can almost smell the treasure; your nose somehow can perceive the smell of gold, how snob of you. In front of you, there are three doors: one red, one blue, and a third yellow door. Your smell is not THAT developed, so you'll have to choose randomly which door to open.")
  q3 = input(f"\n Which door do you think will lead you to the Treasure you came all this way to find? Type 'red', 'blue', or 'yellow' to choose: \n")
else:
  print(f"Dude, instructions were quite easy, you've chosen an invalid option, and now you'll suffer the consequences! Not really, at this point I'm running short on imagination. So you just died of a sudden massive heart stroke.\nG A M E  O V E R\n")

if q3 == 'red':
  print(f"Red! Nice color! So you slowly approach to the door, a lot of memories flash through your exhausted eyes. After all, you've spent three uninterrupted weeks on this quest. Well, I hate to be the one that tells you this, but although red is a reeeaaally nice color, on the other side of the door there actually was a wacko aggressively waving his axe in the air, and yes, he was MAD. How would you feel if some random person trespassed your private property? You would probably feel the urge to trespass that invader's skull with an axe; and somehow this is exactly what happened next. With your last breath, you heard that wacko whispering to what was left of your ear:\nG A M E  O V E R, {name}")
elif q3 == 'blue':
  print(f"Blue! Well, as you may know, programming all this interactive thing is quiet exhausting, so no. Blue was not the right choice. Imagine what would be the most undignified death you could suffer. Yes, that's how you died when you went through this beautiful blue door.\nG A M E  O V E R\n")
elif q3 == 'yellow':
  print(f"\nYELLOW! YES! THE COLOR OF GOLD! THIS MUST BE IT! So you approach the chosen door, your hands are sweating. Something tells you that your choice was right. You grab the doorknob, twist it to the side and gently (a bit out of fear) push the door open. Everything is darker in there, but if you squint your eyes a bit, you can see back there a golden shining. You suddenly forget your fatigue and run as fast as you can towards it. And YES! PILES AND PILES OF GOLDEN COINS AND JEWELS INSIDE THAT BIG WOODEN CHEST! YOU DID IT! YOU FOUND THE TREASURE! YOU ARE NOW OFFICIALLY RICH! Normally that chest would weigh a lot, but adrenaline kicked in already, so when you try to lift it to take it back home, it feels as it was filled with feathers. You rapidly come out of the cabin holding your newest possession.\n\n\nAfter a few days, you're almost home. Yet, good luck trying to explain to your local tax office your brand new acquisition. I'll leave you to that, {name}.")
else:
  print(f"I'm afraid that was not an option. Or maybe you typed it incorrectly. Anyway, you are now officially DEAD. Who would have thought that a simple typo would mean the end of your existence.\nG A M E  O V E R\n")