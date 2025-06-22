"""
Cave Scene for Mystic Quest
===========================
The mysterious crystal cave path with underground adventures and discoveries.
"""

import time
import random


class CaveScene:
    """The crystal cave scene with underground mysteries and challenges."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        
    def play(self):
        """Play the cave scene and return the result."""
        self.game.clear_screen()
        
        # Display cave ASCII art
        self.game.ascii_art.display_cave()
        
        print()
        self.game.print_border('*', 60)
        
        # Cave story
        cave_story = f"""
{self.game.player_name}, you descend into the Crystal Cave, where the air 
grows cool and mysterious. Your footsteps echo in the vast chambers as 
crystalline formations catch and reflect the dim light filtering from above.

The walls are adorned with glowing crystals that pulse with an inner light, 
creating a mesmerizing display of colors that dance across the stone. 
Ancient symbols are carved into the rock, telling stories of civilizations 
long forgotten.

As you venture deeper, you discover three passages leading into the 
mountain's heart...
        """
        
        self.game.print_with_delay(cave_story, 0.02)
        
        print()
        self.game.print_border('*', 60)
        print()
        
        # Present cave choices
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                  THE CAVE PASSAGES                      │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 💎 Follow the glowing crystals to the Crystal Hall  │")
        print("│     (Brilliant gems light the way to hidden treasures)  │")
        print("│                                                         │")
        print("│  2. 📜 Investigate the ancient symbols on the walls     │")
        print("│     (Mysterious runes hint at forgotten knowledge)      │")
        print("│                                                         │")
        print("│  3. 🌊 Follow the sound of underground water            │")
        print("│     (A distant echo suggests a hidden underground lake) │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        # Get player choice
        while True:
            try:
                choice = input("Which passage through the cave calls to you? (1-3): ").strip()
                
                if choice == '1':
                    return self.crystal_hall_encounter()
                elif choice == '2':
                    return self.ancient_symbols_encounter()
                elif choice == '3':
                    return self.underground_lake_encounter()
                else:
                    print("Please enter 1, 2, or 3 to choose your cave passage.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def crystal_hall_encounter(self):
        """Handle the crystal hall encounter."""
        self.game.clear_screen()
        
        crystal_story = f"""
💎 THE CRYSTAL HALL 💎

{self.game.player_name}, you follow the glowing crystals deeper into the 
cave system. The passage opens into a magnificent hall where enormous 
crystals jut from floor and ceiling like frozen lightning.

In the center of the hall stands a pedestal holding a crystal orb that 
pulses with incredible power. As you approach, the orb begins to resonate 
with your presence, and you hear a voice that seems to come from the 
crystals themselves:

"Seeker of truth, you have found the Heart of the Mountain. This crystal 
contains the power to reshape destiny itself, but such power comes with 
great responsibility. Choose wisely."

Suddenly, you notice that one of the crystal formations has a peculiar 
hollow space behind it, almost like a hidden passage...
        """
        
        self.game.print_with_delay(crystal_story, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                 THE CRYSTAL'S CHOICE                    │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. ⚡ Touch the crystal orb (Gain immense power)       │")
        print("│  2. 🔍 Study the crystal's patterns first              │")
        print("│  3. 🕳️ Investigate the hollow space behind crystals    │")
        print("│  4. 🚫 Leave the crystal untouched                     │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What do you do with the crystal orb? (1-4): ").strip()
                
                if choice == '1':
                    # Random outcome - power can be dangerous
                    power_outcome = random.choice(["overwhelming", "controlled", "corrupted"])
                    
                    if power_outcome == "overwhelming":
                        self.game.player_inventory.append("Crystal Power")
                        self.game.game_state["crystal_power"] = "overwhelming"
                        print(f"\n⚡ {self.game.player_name} grasps the crystal orb!")
                        print("Incredible energy surges through you! You feel invincible,")
                        print("but the power is almost too much to control...")
                        time.sleep(2)
                        return "boss"  # Powerful but unstable for boss fight
                        
                    elif power_outcome == "controlled":
                        self.game.player_inventory.append("Balanced Crystal Power")
                        self.game.game_state["crystal_power"] = "balanced"
                        print(f"\n⚡ {self.game.player_name} carefully channels the crystal's energy!")
                        print("You feel the power flow through you in perfect harmony.")
                        print("Strength and wisdom unite within your spirit!")
                        time.sleep(2)
                        return "boss"  # Perfect balance for boss fight
                        
                    else:  # corrupted
                        self.game.player_health -= 30
                        self.game.game_state["crystal_power"] = "corrupted"
                        print(f"\n💀 The crystal's power overwhelms {self.game.player_name}!")
                        print("Dark energy courses through you. You feel powerful but changed...")
                        time.sleep(2)
                        return "boss"  # Corrupted power for boss fight
                        
                elif choice == '2':
                    self.game.game_state["studied_crystal"] = True
                    self.game.player_inventory.append("Crystal Knowledge")
                    print(f"\n🔍 {self.game.player_name} studies the crystal's intricate patterns...")
                    print("You learn the secret of controlling crystal energy without being")
                    print("consumed by it. Knowledge proves more valuable than raw power.")
                    time.sleep(3)
                    return "boss"  # Wisdom advantage in boss fight
                    
                elif choice == '3':
                    return self.discover_crystal_passage()
                    
                elif choice == '4':
                    self.game.game_state["resisted_temptation"] = True
                    print(f"\n🚫 {self.game.player_name} steps back from the crystal orb.")
                    print("'Some powers are too dangerous to wield,' you whisper.")
                    print("The crystals seem to approve of your restraint, glowing warmly.")
                    time.sleep(2)
                    return "peaceful"  # Wisdom leads to peaceful path
                    
                else:
                    print("Please enter 1, 2, 3, or 4 to choose your action with the crystal.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, 3, or 4).")
                continue
                
    def discover_crystal_passage(self):
        """Handle discovery of the crystal passage to treasure room."""
        from .treasure import TreasureScene
        
        passage_text = f"""
🕳️ THE CRYSTAL PASSAGE 🕳️

{self.game.player_name}, your keen observation reveals that the hollow 
space behind the crystals is actually a hidden passage! The crystals 
have grown around an ancient doorway, concealing it for centuries.

As you squeeze through the narrow opening, the crystals begin to sing 
with a beautiful, harmonic resonance. The passage leads deeper into 
the mountain, and you can see a warm, golden light ahead.

The crystal voice whispers: "You have found the path that few discover. 
The crystals have guided you to a place of great significance. Proceed 
with wisdom, for what lies ahead will test more than your courage."
        """
        
        self.game.print_with_delay(passage_text, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                THE CRYSTAL PASSAGE                      │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🚶 Follow the passage to its destination           │")
        print("│  2. 🎵 Listen to the crystal song for guidance         │")
        print("│  3. 🔙 Return to the Crystal Hall                      │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What do you do in the crystal passage? (1-3): ").strip()
                
                if choice == '1':
                    print(f"\n🚶 {self.game.player_name} follows the mysterious passage...")
                    print("The golden light grows brighter as you approach your destiny...")
                    time.sleep(2)
                    
                    # Enter treasure room with crystal guidance
                    self.game.game_state["found_via_crystals"] = True
                    treasure_scene = TreasureScene(self.game)
                    treasure_result = treasure_scene.play()
                    
                    # After treasure room, continue based on result
                    if treasure_result in ["treasure_master", "partial_treasure", "ancient_knowledge"]:
                        return "boss"  # Enhanced for boss fight
                    else:
                        return treasure_result
                        
                elif choice == '2':
                    self.game.game_state["heard_crystal_song"] = True
                    self.game.player_inventory.append("Crystal Harmony")
                    print(f"\n🎵 {self.game.player_name} listens carefully to the crystal song...")
                    print("The harmonious tones fill you with peace and understanding.")
                    print("You feel attuned to the mountain's ancient wisdom.")
                    time.sleep(2)
                    
                    # Still go to treasure room but with special advantage
                    treasure_scene = TreasureScene(self.game)
                    treasure_result = treasure_scene.play()
                    
                    if treasure_result in ["treasure_master", "partial_treasure", "ancient_knowledge"]:
                        return "boss"
                    else:
                        return treasure_result
                        
                elif choice == '3':
                    print(f"\n🔙 {self.game.player_name} returns to the Crystal Hall...")
                    print("Perhaps some mysteries are meant for another time.")
                    time.sleep(1)
                    # Return to original crystal hall choice
                    return self.crystal_hall_encounter()
                    
                else:
                    print("Please enter 1, 2, or 3 to choose your action in the passage.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def ancient_symbols_encounter(self):
        """Handle the ancient symbols encounter."""
        self.game.clear_screen()
        
        symbols_story = f"""
📜 THE ANCIENT SYMBOLS 📜

{self.game.player_name}, you approach the wall covered in mysterious runes 
and symbols. As your eyes adjust to the dim light, the carvings seem to 
shift and dance, telling an ancient story of heroes and shadows.

The symbols begin to glow as you trace them with your finger, and suddenly 
you can understand their meaning. They tell of a great guardian that once 
protected this land, but was corrupted by loneliness and despair.

A ghostly figure materializes before you - the spirit of an ancient scholar:

"Young one, you seek to understand the old ways. These symbols hold the key 
to either awakening great power or finding peace through understanding. 
The choice of how to use this knowledge is yours alone."
        """
        
        self.game.print_with_delay(symbols_story, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                THE SCHOLAR'S WISDOM                     │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 📖 Learn the spell of binding (Control magic)       │")
        print("│  2. 💭 Learn the history of the Shadow Guardian        │")
        print("│  3. 🕊️ Learn the ritual of peaceful resolution         │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What knowledge do you seek from the ancient symbols? (1-3): ").strip()
                
                if choice == '1':
                    self.game.player_inventory.append("Binding Spell")
                    self.game.game_state["knows_binding_spell"] = True
                    print(f"\n📖 {self.game.player_name} learns the ancient spell of binding!")
                    print("The words of power burn themselves into your memory.")
                    print("You now possess the ability to control magical forces!")
                    time.sleep(2)
                    return "boss"  # Magical advantage in boss fight
                    
                elif choice == '2':
                    self.game.game_state["knows_guardian_history"] = True
                    self.game.player_inventory.append("Guardian's History")
                    print(f"\n💭 {self.game.player_name} learns the tragic tale of the Shadow Guardian...")
                    print("You discover that the guardian was once a protector who became")
                    print("corrupted by centuries of isolation. Understanding brings compassion.")
                    time.sleep(3)
                    return "boss"  # Empathy advantage in boss fight
                    
                elif choice == '3':
                    self.game.game_state["knows_peace_ritual"] = True
                    self.game.player_inventory.append("Peace Ritual")
                    print(f"\n🕊️ {self.game.player_name} learns the sacred ritual of peaceful resolution...")
                    print("The ancient words teach you that some conflicts can be ended")
                    print("not through victory, but through understanding and compassion.")
                    time.sleep(3)
                    return "peaceful"  # Direct path to peaceful ending
                    
                else:
                    print("Please enter 1, 2, or 3 to choose what knowledge to seek.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def underground_lake_encounter(self):
        """Handle the underground lake encounter."""
        self.game.clear_screen()
        
        lake_story = f"""
🌊 THE UNDERGROUND LAKE 🌊

{self.game.player_name}, you follow the sound of flowing water through 
winding passages until you emerge into a vast cavern. Before you stretches 
an underground lake of crystal-clear water that reflects the glowing 
crystals above like stars in a night sky.

In the center of the lake, a small island holds an ancient shrine. As you 
wonder how to reach it, a boat made of luminescent stone appears at the 
water's edge, as if summoned by your presence.

The water itself seems to whisper:

"This is the Lake of Reflection, where truth is revealed and souls are 
cleansed. Those who cross these waters are forever changed by what they 
discover about themselves."
        """
        
        self.game.print_with_delay(lake_story, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                 THE LAKE'S INVITATION                   │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🚤 Cross the lake to reach the shrine              │")
        print("│  2. 💧 Drink from the lake's sacred waters             │")
        print("│  3. 🪞 Gaze into the lake's reflective surface         │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("How do you interact with the underground lake? (1-3): ").strip()
                
                if choice == '1':
                    self.game.game_state["visited_shrine"] = True
                    self.game.player_inventory.append("Shrine Blessing")
                    print(f"\n🚤 {self.game.player_name} crosses the mystical lake...")
                    print("At the shrine, you find an ancient blessing that fills you")
                    print("with courage and determination. You are ready for any challenge!")
                    time.sleep(2)
                    return "boss"  # Blessed for boss fight
                    
                elif choice == '2':
                    self.game.player_health = 100  # Full healing
                    self.game.game_state["drank_sacred_water"] = True
                    self.game.player_inventory.append("Sacred Water")
                    print(f"\n💧 {self.game.player_name} drinks from the sacred waters...")
                    print("The water tastes like liquid starlight! All your wounds heal,")
                    print("and you feel purified in body and spirit.")
                    time.sleep(2)
                    return "boss"  # Fully healed for boss fight
                    
                elif choice == '3':
                    self.game.game_state["saw_true_self"] = True
                    print(f"\n🪞 {self.game.player_name} gazes into the lake's perfect reflection...")
                    print("In the water, you see not just your face, but your true self -")
                    print("your hopes, fears, and the strength that lies within.")
                    print("You realize that the greatest battles are won with wisdom, not force.")
                    time.sleep(3)
                    return "peaceful"  # Self-knowledge leads to peace
                    
                else:
                    print("Please enter 1, 2, or 3 to choose your interaction with the lake.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
