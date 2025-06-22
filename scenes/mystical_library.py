"""
Mystical Library Scene for Mystic Quest
=======================================
A magical library where knowledge and spells can be discovered.
"""

import random
import time


class MysticalLibraryScene:
    """The mystical library scene with spell learning and lore."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        
    def play(self):
        """Play the mystical library scene."""
        self.game.clear_screen()
        
        # Display library ASCII art
        self.display_library_art()
        
        print()
        self.game.print_border('-', 60)
        
        # Story introduction
        story_text = f"""
{self.game.player_name}, you discover a magnificent library hidden within 
the mystical realm. Ancient tomes float gently through the air, their pages 
glowing with ethereal light. The scent of old parchment and magical ink 
fills your nostrils.

A wise-looking owl perches on a crystal lectern, its eyes gleaming with 
ancient knowledge. Shelves stretch impossibly high, filled with books 
that seem to whisper secrets of forgotten magic.
        """
        
        self.game.print_with_delay(story_text, 0.02)
        
        print()
        self.game.print_border('-', 60)
        print()
        
        # Present choices
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                THE MYSTICAL LIBRARY                     │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 📚 Study Ancient Tomes                             │")
        print("│     (Learn new spells and magical knowledge)            │")
        print("│                                                         │")
        print("│  2. 🦉 Speak with the Wise Owl                         │")
        print("│     (Gain wisdom and possibly a companion)              │")
        print("│                                                         │")
        print("│  3. 🔍 Search for Hidden Secrets                       │")
        print("│     (Explore the library's mysteries)                   │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        # Get player choice
        while True:
            try:
                choice = input(f"{self.game.player_name}, what do you choose? (1-3): ").strip()
                
                if choice == '1':
                    return self.study_tomes()
                elif choice == '2':
                    return self.speak_with_owl()
                elif choice == '3':
                    return self.search_secrets()
                else:
                    print("Please enter 1, 2, or 3 to make your choice.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def display_library_art(self):
        """Display ASCII art for the mystical library."""
        library_art = """
    📚 THE MYSTICAL LIBRARY 📚
    
    ╔══════════════════════════════════════╗
    ║  📖    📜    📚    📖    📜    📚  ║
    ║                                      ║
    ║    ✨ Ancient Knowledge Awaits ✨    ║
    ║                                      ║
    ║  📚    📖    📜    📚    📖    📜  ║
    ╚══════════════════════════════════════╝
    
           🦉 Wise Guardian Owl 🦉
        """
        print(library_art)
        
    def study_tomes(self):
        """Study ancient tomes to learn spells."""
        self.game.clear_screen()
        
        print("📚 You approach the floating tomes...")
        time.sleep(1)
        
        # Random spell learning
        available_spells = ["fireball", "shield", "insight", "teleport"]
        learned_spells = []
        
        for spell_id in available_spells:
            if spell_id not in self.game.systems.magic_system.known_spells:
                if random.random() < 0.6:  # 60% chance to learn each spell
                    spell_msg = self.game.systems.magic_system.learn_spell(spell_id)
                    learned_spells.append(spell_msg)
                    
        if learned_spells:
            print("\n✨ The ancient knowledge flows into your mind!")
            for msg in learned_spells:
                print(f"  {msg}")
                time.sleep(1)
        else:
            print("\n📖 You study the tomes but find no new spells to learn.")
            print("However, you gain valuable magical knowledge!")
            
        # Gain experience and intelligence
        leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(75)
        print(f"\n⭐ {exp_msg}")
        
        # Boost intelligence
        self.game.systems.stats_system.player_stats["intelligence"] += 3
        print("🧠 Your intelligence increases by 3!")
        
        # Add magical item
        success, item_msg = self.game.systems.inventory_system.add_item("wisdom_scroll")
        if success:
            print(f"📜 {item_msg}")
            
        # Achievement check
        if len(learned_spells) >= 2:
            achievement_msg = self.game.systems.achievement_system.unlock_achievement("spell_caster")
            if achievement_msg:
                print(f"\n{achievement_msg}")
                
        input("\nPress Enter to continue...")
        return "library_studied"
        
    def speak_with_owl(self):
        """Speak with the wise owl guardian."""
        self.game.clear_screen()
        
        print("🦉 You approach the majestic owl...")
        time.sleep(1)
        
        owl_dialogue = f"""
The owl's eyes gleam with ancient wisdom as it speaks in a voice like 
rustling leaves:

"Greetings, {self.game.player_name}. I am Athenaeum, Guardian of Knowledge. 
I have watched over this library for centuries, waiting for a worthy 
seeker of wisdom."

"Your spirit burns bright with curiosity and courage. I sense great 
potential within you. Would you accept my guidance on your journey?"
        """
        
        self.game.print_with_delay(owl_dialogue, 0.03)
        print()
        
        # Offer companion
        print("┌─────────────────────────────────────────────────────────┐")
        print("│  The Wise Owl offers to join your adventure!           │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Accept Athenaeum as your companion                  │")
        print("│  2. Politely decline but ask for wisdom                │")
        print("│  3. Ask about the library's history                    │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        choice = input("Your response (1-3): ").strip()
        
        if choice == '1':
            # Recruit owl companion
            companion_msg = self.game.systems.companion_system.recruit_companion("ancient_owl")
            print(f"\n🦉 {companion_msg}")
            
            # Unlock achievement
            achievement_msg = self.game.systems.achievement_system.unlock_achievement("beast_friend")
            if achievement_msg:
                print(f"\n{achievement_msg}")
                
            # Grant wisdom bonus
            self.game.systems.stats_system.player_stats["intelligence"] += 5
            print("🧠 Athenaeum's wisdom grants you +5 Intelligence!")
            
        elif choice == '2':
            print("\n🦉 'Wisdom is not in knowing everything, but in understanding")
            print("    what truly matters. Remember: courage without wisdom is")
            print("    recklessness, but wisdom without courage is cowardice.'")
            
            # Grant experience and luck
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(100)
            print(f"\n⭐ {exp_msg}")
            self.game.systems.stats_system.player_stats["luck"] += 3
            print("🍀 Your luck increases by 3!")
            
        else:
            print("\n🦉 'This library exists between worlds, a sanctuary for")
            print("    knowledge that must not be lost. Many heroes have")
            print("    visited these halls, each leaving their mark in the")
            print("    great tapestry of adventure.'")
            
            # Learn about game lore
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(50)
            print(f"\n⭐ {exp_msg}")
            
        input("\nPress Enter to continue...")
        return "owl_encountered"
        
    def search_secrets(self):
        """Search for hidden secrets in the library."""
        self.game.clear_screen()
        
        print("🔍 You begin searching the library for hidden secrets...")
        time.sleep(1)
        
        # Random discoveries
        discoveries = []
        
        # Check player's luck for better discoveries
        luck = self.game.systems.stats_system.player_stats["luck"]
        discovery_chance = min(0.8, 0.4 + (luck * 0.02))  # Higher luck = better chance
        
        if random.random() < discovery_chance:
            discoveries.append("secret_passage")
            
        if random.random() < 0.6:
            discoveries.append("hidden_tome")
            
        if random.random() < 0.4:
            discoveries.append("magical_artifact")
            
        if not discoveries:
            print("\n🔍 Despite your thorough search, you find nothing unusual.")
            print("However, your exploration skills improve!")
            self.game.systems.stats_system.player_stats["agility"] += 2
            print("🏃 Your agility increases by 2!")
            
        else:
            print("\n✨ Your search reveals amazing discoveries!")
            
            for discovery in discoveries:
                if discovery == "secret_passage":
                    print("\n🚪 You discover a hidden passage behind a bookshelf!")
                    print("   It leads to a secret chamber filled with ancient treasures.")
                    
                    # Add rare items
                    success, item_msg = self.game.systems.inventory_system.add_item("ancient_key")
                    if success:
                        print(f"   🗝️ {item_msg}")
                        
                    success, item_msg = self.game.systems.inventory_system.add_item("shadow_gem")
                    if success:
                        print(f"   💎 {item_msg}")
                        
                elif discovery == "hidden_tome":
                    print("\n📖 You find a hidden tome of powerful magic!")
                    
                    # Learn a rare spell
                    rare_spells = ["teleport", "insight"]
                    for spell in rare_spells:
                        if spell not in self.game.systems.magic_system.known_spells:
                            spell_msg = self.game.systems.magic_system.learn_spell(spell)
                            print(f"   ✨ {spell_msg}")
                            break
                            
                elif discovery == "magical_artifact":
                    print("\n🔮 You discover a powerful magical artifact!")
                    
                    # Add magical items
                    success, item_msg = self.game.systems.inventory_system.add_item("magic_crystal")
                    if success:
                        print(f"   💎 {item_msg}")
                        
                    success, item_msg = self.game.systems.inventory_system.add_item("fairy_dust")
                    if success:
                        print(f"   ✨ {item_msg}")
                        
        # Gain experience
        exp_amount = 60 + (len(discoveries) * 20)
        leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(exp_amount)
        print(f"\n⭐ {exp_msg}")
        
        # Check for treasure hunter achievement
        if "secret_passage" in discoveries:
            achievement_msg = self.game.systems.achievement_system.unlock_achievement("treasure_hunter")
            if achievement_msg:
                print(f"\n{achievement_msg}")
                
        input("\nPress Enter to continue...")
        return "secrets_discovered"
