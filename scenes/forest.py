"""
Forest Scene for Mystic Quest
=============================
The enchanted forest path with magical encounters and choices.
"""

import time
import random


class ForestScene:
    """The enchanted forest scene with multiple paths and encounters."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        
    def play(self):
        """Play the forest scene and return the result."""
        self.game.clear_screen()
        
        # Display forest ASCII art
        self.game.ascii_art.display_forest()
        
        print()
        self.game.print_border('~', 60)
        
        # Forest story
        forest_story = f"""
{self.game.player_name}, you step into the Enchanted Forest, where ancient 
oaks tower above you like cathedral pillars. Shafts of golden sunlight 
pierce through the emerald canopy, creating a mystical atmosphere.

As you walk deeper into the forest, you hear the gentle babbling of a 
hidden stream and the melodic songs of unseen birds. The air is thick 
with magic and possibility.

Suddenly, you come upon a clearing where three paths diverge...
        """
        
        self.game.print_with_delay(forest_story, 0.02)
        
        print()
        self.game.print_border('~', 60)
        print()
        
        # Present forest choices
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                 THE FOREST CROSSROADS                   │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🦋 Follow the butterfly to the Fairy Glade         │")
        print("│     (Colorful wings flutter toward hidden magic)        │")
        print("│                                                         │")
        print("│  2. 🐺 Track the wolf prints to the Ancient Grove      │")
        print("│     (Mysterious paw prints lead into darkness)         │")
        print("│                                                         │")
        print("│  3. 🌸 Pick flowers by the babbling brook              │")
        print("│     (Beautiful blooms call for peaceful gathering)     │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        # Get player choice
        while True:
            try:
                choice = input("Which path through the forest calls to you? (1-3): ").strip()
                
                if choice == '1':
                    return self.fairy_glade_encounter()
                elif choice == '2':
                    return self.ancient_grove_encounter()
                elif choice == '3':
                    return self.peaceful_brook_encounter()
                else:
                    print("Please enter 1, 2, or 3 to choose your forest path.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def fairy_glade_encounter(self):
        """Handle the fairy glade encounter."""
        self.game.clear_screen()
        
        fairy_story = f"""
🦋 THE FAIRY GLADE 🦋

{self.game.player_name}, you follow the shimmering butterfly deeper into 
the forest. The creature's wings catch the light like stained glass as it 
leads you to a hidden glade.

In the center of the clearing, you discover a circle of mushrooms glowing 
with soft, ethereal light. Tiny fairies dance around the ring, their 
laughter like silver bells in the wind.

The fairy queen approaches you, her voice like a gentle breeze:

"Mortal, you have found our sacred circle. We offer you a choice - 
accept our blessing of nature's magic, or continue your quest with 
the wisdom we can share."

As she speaks, you notice something glinting behind an ancient oak tree...
        """
        
        self.game.print_with_delay(fairy_story, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                  THE FAIRY'S OFFER                      │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. ✨ Accept the fairy blessing (Gain magical power)   │")
        print("│  2. 🧠 Ask for wisdom about your quest                 │")
        print("│  3. 🔍 Investigate the glinting object behind the tree │")
        print("│  4. 🙏 Politely decline and continue your journey      │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What is your response to the fairy queen? (1-4): ").strip()
                
                if choice == '1':
                    self.game.player_inventory.append("Fairy Blessing")
                    self.game.game_state["has_fairy_blessing"] = True
                    print(f"\n✨ The fairies surround {self.game.player_name} with sparkling light!")
                    print("You feel magical energy flowing through your veins...")
                    time.sleep(2)
                    return "boss"  # Leads to boss encounter
                    
                elif choice == '2':
                    self.game.game_state["has_fairy_wisdom"] = True
                    print(f"\n🧠 The fairy queen whispers ancient secrets to {self.game.player_name}...")
                    print("'Beware the Shadow Guardian, but remember - not all battles")
                    print("are won with strength alone. Sometimes, understanding is key.'")
                    time.sleep(3)
                    return "boss"  # Leads to boss encounter with wisdom
                    
                elif choice == '3':
                    return self.discover_hidden_entrance()
                    
                elif choice == '4':
                    print(f"\n🙏 {self.game.player_name} bows respectfully to the fairy queen.")
                    print("'Your respect honors us, mortal. May fortune smile upon your path.'")
                    time.sleep(2)
                    return "peaceful"  # Peaceful ending
                    
                else:
                    print("Please enter 1, 2, 3, or 4 to respond to the fairy queen.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, 3, or 4).")
                continue
                
    def discover_hidden_entrance(self):
        """Handle discovery of the hidden treasure room entrance."""
        from .treasure import TreasureScene
        
        discovery_text = f"""
🔍 A MYSTERIOUS DISCOVERY 🔍

{self.game.player_name}, your curiosity leads you to investigate the 
glinting object behind the ancient oak. As you approach, you realize 
it's not just a random sparkle - it's a crystalline key embedded in 
the tree's bark!

The fairy queen gasps in amazement: "By the ancient magic! You have 
found the Lost Key of Treasures! That key has been hidden for over 
a thousand years, waiting for a worthy soul to discover it."

She points to a shimmering outline that appears in the air nearby:
"The key reveals the entrance to the legendary Hidden Treasure Chamber. 
Few mortals have ever been deemed worthy to find it. This is a great 
honor, brave {self.game.player_name}!"
        """
        
        self.game.print_with_delay(discovery_text, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                THE HIDDEN ENTRANCE                      │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🗝️ Use the key to enter the treasure chamber       │")
        print("│  2. 🎁 Give the key to the fairy queen as a gift       │")
        print("│  3. 💎 Keep the key but continue your original quest   │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What do you do with the mysterious key? (1-3): ").strip()
                
                if choice == '1':
                    print(f"\n🗝️ {self.game.player_name} uses the crystal key...")
                    print("The air shimmers and a doorway of pure light appears!")
                    time.sleep(2)
                    
                    # Enter treasure room
                    treasure_scene = TreasureScene(self.game)
                    treasure_result = treasure_scene.play()
                    
                    # After treasure room, continue to boss or ending based on result
                    if treasure_result in ["treasure_master", "partial_treasure", "ancient_knowledge"]:
                        return "boss"  # Enhanced for boss fight
                    else:
                        return treasure_result
                        
                elif choice == '2':
                    self.game.game_state["gave_key_to_fairy"] = True
                    self.game.player_inventory.append("Fairy Queen's Eternal Gratitude")
                    print(f"\n🎁 {self.game.player_name} offers the key to the fairy queen...")
                    print("Her eyes fill with tears of joy: 'Such selflessness! You have")
                    print("given me the power to restore our ancient sanctuary. Take this")
                    print("blessing - it will serve you better than any treasure!'")
                    time.sleep(3)
                    return "boss"  # Special fairy blessing for boss
                    
                elif choice == '3':
                    self.game.player_inventory.append("Crystal Key of Treasures")
                    self.game.game_state["has_treasure_key"] = True
                    print(f"\n💎 {self.game.player_name} carefully pockets the crystal key...")
                    print("'A wise choice,' the fairy queen nods. 'Some treasures are")
                    print("best saved for the right moment. The key will serve you well.'")
                    time.sleep(2)
                    return "boss"  # Key might be useful later
                    
                else:
                    print("Please enter 1, 2, or 3 to choose what to do with the key.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def ancient_grove_encounter(self):
        """Handle the ancient grove encounter."""
        self.game.clear_screen()
        
        grove_story = f"""
🐺 THE ANCIENT GROVE 🐺

{self.game.player_name}, you follow the wolf tracks deeper into the forest's 
heart. The trees grow older and more twisted here, their bark scarred by 
centuries of storms and seasons.

You emerge into a grove where massive stone pillars covered in ancient 
runes stand in a perfect circle. At the center lies a wolf, but not an 
ordinary one - its fur shimmers with starlight, and its eyes hold the 
wisdom of ages.

The spirit wolf speaks directly to your mind:

"Young seeker, you have found the Grove of Trials. Here, courage is tested 
and destiny is forged. Will you prove yourself worthy of the ancient power 
that sleeps within these stones?"
        """
        
        self.game.print_with_delay(grove_story, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                   THE WOLF'S TRIAL                      │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. ⚔️  Accept the trial of courage                     │")
        print("│  2. 🤝 Offer to help the spirit wolf instead           │")
        print("│  3. 🚶 Leave the grove respectfully                    │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("How do you respond to the spirit wolf? (1-3): ").strip()
                
                if choice == '1':
                    # Random trial outcome
                    trial_success = random.choice([True, False])
                    if trial_success:
                        self.game.player_inventory.append("Ancient Strength")
                        self.game.game_state["passed_wolf_trial"] = True
                        print(f"\n⚔️ {self.game.player_name} faces the trial with unwavering courage!")
                        print("The ancient stones glow, and you feel incredible strength flow through you!")
                        time.sleep(2)
                        return "boss"  # Strong for boss fight
                    else:
                        self.game.player_health -= 20
                        print(f"\n💔 The trial tests {self.game.player_name} harshly...")
                        print("You emerge wounded but wiser. Sometimes failure teaches us most.")
                        time.sleep(2)
                        return "boss"  # Weakened but still continues
                        
                elif choice == '2':
                    self.game.game_state["helped_spirit_wolf"] = True
                    self.game.player_inventory.append("Wolf's Gratitude")
                    print(f"\n🤝 {self.game.player_name} offers kindness instead of seeking power...")
                    print("The spirit wolf's eyes shine with gratitude. 'Your heart is pure.")
                    print("Take this blessing - it will serve you when darkness comes.'")
                    time.sleep(3)
                    return "boss"  # Special advantage in boss fight
                    
                elif choice == '3':
                    print(f"\n🚶 {self.game.player_name} bows to the spirit wolf and departs.")
                    print("'Wisdom knows when to seek power and when to walk away.'")
                    time.sleep(2)
                    return "peaceful"  # Peaceful ending
                    
                else:
                    print("Please enter 1, 2, or 3 to respond to the spirit wolf.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def peaceful_brook_encounter(self):
        """Handle the peaceful brook encounter."""
        self.game.clear_screen()
        
        brook_story = f"""
🌸 THE BABBLING BROOK 🌸

{self.game.player_name}, you choose the gentlest path, following the sound 
of flowing water to a crystal-clear brook. Wildflowers of every color 
imaginable carpet the banks, their sweet fragrance filling the air.

As you kneel by the water's edge to gather flowers, you notice something 
magical - each bloom you touch seems to whisper a secret of the forest. 
The brook itself begins to speak in a voice like liquid music:

"Gentle soul, you have chosen the path of peace and beauty. In a world 
full of conflict, you seek harmony. This is a rare and precious gift."

The water shows you visions of possible futures...
        """
        
        self.game.print_with_delay(brook_story, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                  THE BROOK'S WISDOM                     │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🔮 Look deeper into the visions of the future      │")
        print("│  2. 🌺 Gather healing flowers for your journey         │")
        print("│  3. 💧 Drink from the brook to gain inner peace        │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What do you choose to do by the brook? (1-3): ").strip()
                
                if choice == '1':
                    self.game.game_state["saw_future_visions"] = True
                    print(f"\n🔮 {self.game.player_name} gazes into the mystical waters...")
                    print("You see glimpses of a great shadow that threatens the land,")
                    print("but also the light that can banish it. Knowledge is power.")
                    time.sleep(3)
                    return "boss"  # Goes to boss with foresight
                    
                elif choice == '2':
                    self.game.player_inventory.append("Healing Flowers")
                    self.game.player_health = min(100, self.game.player_health + 30)
                    print(f"\n🌺 {self.game.player_name} carefully gathers the magical blooms...")
                    print("The flowers pulse with healing energy. You feel refreshed and renewed!")
                    time.sleep(2)
                    return "boss"  # Goes to boss with healing items
                    
                elif choice == '3':
                    self.game.game_state["inner_peace"] = True
                    print(f"\n💧 {self.game.player_name} drinks from the sacred brook...")
                    print("A profound sense of peace fills your soul. You understand that")
                    print("true strength comes from harmony, not conflict.")
                    time.sleep(3)
                    return "peaceful"  # Achieves peaceful ending
                    
                else:
                    print("Please enter 1, 2, or 3 to choose your action by the brook.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
