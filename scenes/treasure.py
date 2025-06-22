"""
Hidden Treasure Room Scene for Mystic Quest
==========================================
A secret chamber with riddles, puzzles, and ancient treasures.
"""

import time
import random


class TreasureScene:
    """The hidden treasure room with riddles and ancient puzzles."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        self.riddles_solved = 0
        self.max_riddles = 3
        
    def play(self):
        """Play the treasure room scene and return the result."""
        self.game.clear_screen()
        
        # Display treasure room discovery
        self.game.ascii_art.display_treasure()
        
        print()
        self.game.print_border('*', 60)
        
        # Treasure room story
        treasure_story = f"""
🗝️ THE HIDDEN TREASURE CHAMBER 🗝️

{self.game.player_name}, as you explore deeper into the mystical realm, 
you notice a peculiar shimmer in the air near an ancient wall. Running 
your hand along the stone, you discover a hidden mechanism!

The wall slides away with a grinding sound, revealing a secret chamber 
that hasn't been opened for centuries. Golden light spills out, and you 
step into a magnificent treasure room filled with glittering gems, 
ancient artifacts, and mysterious scrolls.

At the center of the room stands an ornate pedestal holding three 
crystalline orbs, each pulsing with different colored light. Ancient 
runes glow on the walls, and a melodious voice echoes through the chamber:

"Welcome, seeker of wisdom and fortune. To claim the treasures within, 
you must prove your wit through the Trial of Three Riddles. Answer 
correctly, and great rewards await. Choose poorly, and leave empty-handed."
        """
        
        self.game.print_with_delay(treasure_story, 0.02)
        
        print()
        self.game.print_border('*', 60)
        print()
        
        # Present initial choices
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                THE TREASURE CHAMBER                     │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🧩 Accept the Trial of Three Riddles               │")
        print("│  2. 🔍 Examine the treasure room more carefully        │")
        print("│  3. 💎 Try to take treasures without solving riddles   │")
        print("│  4. 🚪 Leave the chamber and continue your journey     │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What do you choose to do in the treasure chamber? (1-4): ").strip()
                
                if choice == '1':
                    return self.riddle_trial()
                elif choice == '2':
                    return self.examine_chamber()
                elif choice == '3':
                    return self.attempt_theft()
                elif choice == '4':
                    return self.leave_chamber()
                else:
                    print("Please enter 1, 2, 3, or 4 to choose your action.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, 3, or 4).")
                continue
                
    def riddle_trial(self):
        """Handle the riddle trial challenge."""
        self.game.clear_screen()
        
        trial_intro = f"""
🧩 THE TRIAL OF THREE RIDDLES 🧩

{self.game.player_name}, you step forward to accept the challenge. 
The three crystalline orbs begin to glow brighter, and ancient magic 
fills the air. The voice speaks again:

"Very well, brave soul. Answer all three riddles correctly, and the 
greatest treasures shall be yours. Fail, and you may try again, but 
with each failure, the rewards diminish. Choose your answers wisely..."

The first orb pulses with blue light, ready to present its riddle.
        """
        
        self.game.print_with_delay(trial_intro, 0.02)
        
        # Define riddles with multiple choice answers
        riddles = [
            {
                "question": """
🔵 RIDDLE OF WISDOM 🔵

"I have cities, but no houses dwell within.
I have mountains, but no trees therein.
I have water, but no fish swim free.
I have roads, but no travelers you'll see.
What am I?"
                """,
                "options": ["1. A painting", "2. A map", "3. A dream", "4. A book"],
                "correct": 2,
                "explanation": "A map shows cities, mountains, water, and roads, but contains none of the living things themselves!"
            },
            {
                "question": """
🟡 RIDDLE OF COURAGE 🟡

"The more you take away from me,
The bigger and deeper I will be.
I can be round, I can be square,
But I'm always empty, that I declare.
What am I?"
                """,
                "options": ["1. A hole", "2. A shadow", "3. A secret", "4. A wound"],
                "correct": 1,
                "explanation": "A hole gets bigger the more you dig out of it, and it's always empty space!"
            },
            {
                "question": """
🔴 RIDDLE OF MYSTERY 🔴

"I speak without a mouth and hear without ears.
I have no body, but come alive with fears.
In mountains I boom, in caves I hide,
By your voice I'm multiplied.
What am I?"
                """,
                "options": ["1. A ghost", "2. An echo", "3. The wind", "4. A memory"],
                "correct": 2,
                "explanation": "An echo repeats your voice without having a mouth, and grows stronger in mountains and caves!"
            }
        ]
        
        # Present each riddle
        for i, riddle in enumerate(riddles):
            if not self.present_riddle(riddle, i + 1):
                # Failed riddle - offer consolation prize
                return self.partial_reward()
            else:
                self.riddles_solved += 1
                
        # All riddles solved successfully
        return self.complete_victory()
        
    def present_riddle(self, riddle, riddle_number):
        """Present a single riddle and get the player's answer."""
        print()
        self.game.print_border('-', 60)
        print(riddle["question"])
        print()
        
        for option in riddle["options"]:
            print(f"  {option}")
        print()
        
        attempts = 2  # Give player 2 attempts per riddle
        
        for attempt in range(attempts):
            try:
                answer = input(f"Your answer for riddle {riddle_number} (1-4): ").strip()
                
                if answer in ['1', '2', '3', '4']:
                    if int(answer) == riddle["correct"]:
                        print(f"\n✅ Correct! {riddle['explanation']}")
                        print(f"The orb glows brilliantly and {self.game.player_name} feels wiser!")
                        time.sleep(2)
                        return True
                    else:
                        if attempt < attempts - 1:
                            print(f"\n❌ Not quite right. You have {attempts - attempt - 1} attempt remaining.")
                            print("Think carefully about the riddle's clues...")
                        else:
                            print(f"\n❌ Incorrect. The answer was {riddle['correct']}: {riddle['explanation']}")
                            time.sleep(2)
                            return False
                else:
                    print("Please enter 1, 2, 3, or 4.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, 3, or 4).")
                continue
                
        return False
        
    def complete_victory(self):
        """Handle complete riddle victory."""
        self.game.clear_screen()
        
        victory_text = f"""
🏆 MASTER OF RIDDLES 🏆

{self.game.player_name}, you have solved all three riddles with wisdom 
and insight! The treasure chamber erupts in brilliant light as ancient 
magic recognizes your intellectual prowess.

The three orbs float toward you and merge into a single, magnificent 
crystal that pulses with rainbow light. As you grasp it, knowledge 
and power flow through you like a river of starlight.

TREASURES GAINED:
💎 The Orb of Infinite Wisdom - Grants perfect insight
🗝️ The Master Key - Opens any lock in the realm
📜 The Scroll of Ancient Secrets - Contains forgotten spells
💰 A chest of 1000 golden coins
⚡ Enhanced magical abilities
🧠 Permanent wisdom boost

The chamber's voice speaks one final time:
"You have proven yourself worthy of the greatest treasures. Use them 
wisely, for with great power comes great responsibility."
        """
        
        self.game.print_with_delay(victory_text, 0.02)
        
        # Add items to inventory and boost stats
        self.game.player_inventory.extend([
            "Orb of Infinite Wisdom",
            "Master Key", 
            "Scroll of Ancient Secrets",
            "1000 Gold Coins"
        ])
        self.game.player_health = min(100, self.game.player_health + 50)
        self.game.game_state["treasure_master"] = True
        self.game.game_state["has_master_key"] = True
        self.game.game_state["infinite_wisdom"] = True
        
        time.sleep(3)
        return "treasure_master"
        
    def partial_reward(self):
        """Handle partial success in riddles."""
        self.game.clear_screen()
        
        partial_text = f"""
💰 PARTIAL SUCCESS 💰

{self.game.player_name}, though you didn't solve all the riddles, 
your effort and courage have not gone unnoticed. The chamber's 
magic recognizes your attempt and grants you a consolation reward.

TREASURES GAINED:
💎 A bag of precious gems
🗝️ A silver key (opens some doors)
📜 A scroll with helpful hints
💰 A pouch of 200 gold coins

"Wisdom comes through both success and failure," the voice intones. 
"You have learned much today, and that knowledge is treasure itself."
        """
        
        self.game.print_with_delay(partial_text, 0.02)
        
        # Add lesser items to inventory
        self.game.player_inventory.extend([
            "Precious Gems",
            "Silver Key",
            "Hint Scroll",
            "200 Gold Coins"
        ])
        self.game.player_health = min(100, self.game.player_health + 20)
        self.game.game_state["found_treasure"] = True
        
        time.sleep(2)
        return "partial_treasure"
        
    def examine_chamber(self):
        """Handle careful examination of the chamber."""
        self.game.clear_screen()
        
        examine_text = f"""
🔍 THE CAREFUL OBSERVER 🔍

{self.game.player_name}, you decide to examine the treasure chamber 
more carefully before making any hasty decisions. Your cautious 
approach reveals hidden details that others might miss.

As you study the walls, you notice:
• Ancient murals depicting the history of the realm
• Hidden compartments containing rare artifacts
• A secret passage leading to an underground garden
• Inscriptions that reveal the true purpose of this place

Your careful observation is rewarded! You discover:
        """
        
        self.game.print_with_delay(examine_text, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                 HIDDEN DISCOVERIES                      │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🌸 Enter the secret underground garden              │")
        print("│  2. 📚 Study the ancient murals for knowledge          │")
        print("│  3. 🗝️ Search the hidden compartments for artifacts    │")
        print("│  4. 🧩 Now attempt the riddle trial with more insight  │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What hidden discovery interests you most? (1-4): ").strip()
                
                if choice == '1':
                    return self.secret_garden()
                elif choice == '2':
                    return self.study_murals()
                elif choice == '3':
                    return self.search_compartments()
                elif choice == '4':
                    # Give advantage in riddle trial
                    self.game.game_state["examined_chamber"] = True
                    return self.riddle_trial()
                else:
                    print("Please enter 1, 2, 3, or 4 to choose your discovery.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, 3, or 4).")
                continue
                
    def secret_garden(self):
        """Handle the secret underground garden discovery."""
        garden_text = f"""
🌸 THE UNDERGROUND GARDEN 🌸

{self.game.player_name}, you follow the secret passage and emerge into 
a breathtaking underground garden. Luminescent flowers bloom in impossible 
colors, and a crystal spring bubbles with water that sparkles like liquid 
diamonds.

This hidden sanctuary has been untouched for centuries. As you drink 
from the crystal spring and breathe the pure air, you feel completely 
restored and enlightened.

GARDEN BLESSINGS RECEIVED:
🌺 Perfect health restoration
🧘 Inner peace and clarity
🌿 Nature's protection blessing
💧 Crystal spring water (healing potion)
        """
        
        self.game.print_with_delay(garden_text, 0.02)
        
        # Restore health and add blessing
        self.game.player_health = 100
        self.game.player_inventory.extend(["Crystal Spring Water", "Nature's Blessing"])
        self.game.game_state["found_secret_garden"] = True
        self.game.game_state["inner_peace"] = True
        
        time.sleep(2)
        return "secret_garden"
        
    def study_murals(self):
        """Handle studying the ancient murals."""
        mural_text = f"""
📚 THE ANCIENT MURALS 📚

{self.game.player_name}, you spend time carefully studying the intricate 
murals that cover the chamber walls. These ancient paintings tell the 
complete history of the mystical realm, revealing secrets that have been 
lost for millennia.

You learn about:
• The true origin of the Shadow Guardian
• Hidden paths through the realm
• The location of other secret chambers
• Ancient spells of protection and healing
• The prophecy of a chosen hero (which might be you!)

KNOWLEDGE GAINED:
🧠 Complete realm history
🗺️ Secret path knowledge  
📜 Ancient protection spells
🔮 Prophecy understanding
        """
        
        self.game.print_with_delay(mural_text, 0.02)
        
        # Add knowledge items
        self.game.player_inventory.extend(["Ancient History", "Secret Paths Map", "Protection Spells"])
        self.game.game_state["knows_complete_history"] = True
        self.game.game_state["knows_secret_paths"] = True
        self.game.game_state["knows_prophecy"] = True
        
        time.sleep(2)
        return "ancient_knowledge"
        
    def search_compartments(self):
        """Handle searching hidden compartments."""
        compartment_text = f"""
🗝️ THE HIDDEN COMPARTMENTS 🗝️

{self.game.player_name}, your careful search reveals several hidden 
compartments built into the chamber walls. Each contains artifacts 
left by previous adventurers who discovered this secret room.

You find:
• A set of masterwork lockpicks
• A cloak that grants stealth abilities
• A compass that always points to treasure
• A ring that translates any language
• A small bag of enchanted coins

ARTIFACTS ACQUIRED:
🔓 Master Lockpicks
👤 Cloak of Stealth
🧭 Treasure Compass
💍 Ring of Languages
💰 Enchanted Coins
        """
        
        self.game.print_with_delay(compartment_text, 0.02)
        
        # Add artifacts to inventory
        self.game.player_inventory.extend([
            "Master Lockpicks",
            "Cloak of Stealth", 
            "Treasure Compass",
            "Ring of Languages",
            "Enchanted Coins"
        ])
        self.game.game_state["has_artifacts"] = True
        self.game.game_state["can_pick_locks"] = True
        self.game.game_state["has_stealth"] = True
        
        time.sleep(2)
        return "hidden_artifacts"
        
    def attempt_theft(self):
        """Handle attempting to take treasures without solving riddles."""
        self.game.clear_screen()
        
        theft_text = f"""
💎 THE TEMPTATION OF GREED 💎

{self.game.player_name}, you decide to try taking some treasures 
without solving the riddles. As you reach for a glittering gem, 
the chamber's magic responds to your intentions...
        """
        
        self.game.print_with_delay(theft_text, 0.02)
        
        # Random outcome for theft attempt
        theft_outcome = random.choice(["caught", "partial_success", "curse"])
        
        if theft_outcome == "caught":
            caught_text = f"""
⚡ MAGICAL PROTECTION ⚡

The moment your fingers touch the treasure, magical barriers spring 
to life! Lightning crackles around you, but it doesn't harm - instead, 
it gently pushes you back.

The chamber's voice speaks with disappointment:
"Greed without wisdom leads only to emptiness. The treasures here 
are earned through merit, not taken through cunning."

You are unharmed but leave empty-handed, having learned a valuable 
lesson about the nature of true treasure.
            """
            
            self.game.print_with_delay(caught_text, 0.02)
            self.game.game_state["attempted_theft"] = True
            time.sleep(2)
            return "theft_failed"
            
        elif theft_outcome == "partial_success":
            partial_text = f"""
🤏 MINOR SUCCESS 🤏

You manage to grab a small handful of coins before the magical 
protections activate. The chamber seems to allow this minor 
transgression, perhaps understanding that curiosity sometimes 
overcomes wisdom.

"A small lesson in both temptation and consequence," the voice 
notes with what might be amusement.

GAINED: A few gold coins and a lesson in restraint.
            """
            
            self.game.print_with_delay(partial_text, 0.02)
            self.game.player_inventory.append("Handful of Gold")
            self.game.game_state["minor_theft"] = True
            time.sleep(2)
            return "minor_theft"
            
        else:  # curse
            curse_text = f"""
💀 THE CURSE OF GREED 💀

As you grasp the treasure, dark magic swirls around you! A curse 
settles upon your shoulders - not harmful, but humbling. For the 
rest of your adventure, you'll find that true treasures seem to 
slip away from greedy hands.

"Let this be a lesson," the voice intones solemnly. "The greatest 
treasures cannot be stolen, only earned."

You feel the weight of the curse, but also the wisdom it brings.
            """
            
            self.game.print_with_delay(curse_text, 0.02)
            self.game.player_health -= 10
            self.game.game_state["cursed_by_greed"] = True
            time.sleep(2)
            return "cursed"
            
    def leave_chamber(self):
        """Handle leaving the chamber without taking anything."""
        leave_text = f"""
🚪 THE WISDOM OF RESTRAINT 🚪

{self.game.player_name}, you decide that some mysteries are best 
left undisturbed. With a respectful bow to the chamber, you turn 
to leave.

As you reach the entrance, the chamber's voice calls out:
"Your restraint shows wisdom beyond your years. Take this gift 
as a token of respect for your noble heart."

A small, glowing crystal appears in your hand - a compass that 
will always guide you toward your true destiny.

RECEIVED: Destiny Compass - "It points not to treasure, but to purpose."
        """
        
        self.game.print_with_delay(leave_text, 0.02)
        
        # Reward for wisdom and restraint
        self.game.player_inventory.append("Destiny Compass")
        self.game.game_state["showed_restraint"] = True
        self.game.game_state["has_destiny_compass"] = True
        
        time.sleep(2)
        return "wise_restraint"
