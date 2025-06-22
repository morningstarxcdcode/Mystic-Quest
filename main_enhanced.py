#!/usr/bin/env python3
"""
Mystic Quest - Enhanced Text-Based Adventure Game
================================================
A modular, beautiful text adventure with advanced RPG systems, ASCII art, 
multiple storylines, and unique gameplay mechanics.

Author: Adventure Game Creator
Version: 2.0 - Enhanced Edition
"""

import os
import sys
import time
import random
from ascii_art import AsciiArt
from game_systems import GameSystems
from save_system import SaveSystem
from scenes.intro import IntroScene
from scenes.forest import ForestScene
from scenes.cave import CaveScene
from scenes.boss import BossScene
from scenes.ending import EndingScene


class EnhancedGameEngine:
    """Enhanced game engine with advanced RPG systems."""
    
    def __init__(self):
        # Basic game state
        self.player_name = ""
        self.player_health = 100
        self.player_inventory = []
        self.game_state = {}
        
        # Enhanced systems
        self.ascii_art = AsciiArt()
        self.systems = GameSystems(self)
        self.save_system = SaveSystem(self)
        
        # Game tracking
        self.locations_visited = set()
        self.choices_made = []
        self.battles_won = 0
        self.spells_cast = 0
        
    def clear_screen(self):
        """Clear the terminal screen for better presentation."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_with_delay(self, text, delay=0.03):
        """Print text with a typewriter effect."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def print_border(self, char='=', length=60):
        """Print a decorative border."""
        print(char * length)
        
    def display_title(self):
        """Display the main title screen."""
        self.clear_screen()
        self.ascii_art.display_title()
        self.print_border('=', 60)
        print("Welcome to MYSTIC QUEST - Enhanced Edition")
        self.print_border('=', 60)
        
        # Display current weather and time
        weather_info = self.systems.weather_system.get_weather_info()
        time_of_day = self.systems.time_system.get_time_of_day()
        print(f"🌤️ Weather: {weather_info}")
        print(f"🕐 Time: {time_of_day}")
        print()
        
    def display_menu(self):
        """Display the enhanced main menu."""
        self.display_title()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                    MAIN MENU                            │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Start New Adventure                                 │")
        print("│  2. Load Saved Game                                     │")
        print("│  3. Game Instructions                                   │")
        print("│  4. View Achievements                                   │")
        print("│  5. Credits                                             │")
        print("│  6. Exit Game                                           │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            choice = input("Enter your choice (1-6): ").strip()
            if choice == '1':
                self.start_new_game()
                break
            elif choice == '2':
                self.load_game_menu()
            elif choice == '3':
                self.show_instructions()
            elif choice == '4':
                self.show_achievements()
            elif choice == '5':
                self.show_credits()
            elif choice == '6':
                self.exit_game()
                break
            else:
                print("Invalid choice. Please enter 1-6.")
                
    def show_instructions(self):
        """Display enhanced game instructions."""
        self.clear_screen()
        self.print_border('*', 60)
        print("                    INSTRUCTIONS")
        self.print_border('*', 60)
        print()
        print("🎮 BASIC GAMEPLAY:")
        print("• Make choices by entering numbers (1, 2, or 3)")
        print("• Your decisions affect the story outcome")
        print("• Multiple endings await based on your choices")
        print()
        print("🆕 NEW FEATURES:")
        print("• 📊 Character Stats: Level up and improve abilities")
        print("• 🎒 Inventory System: Collect and use items strategically")
        print("• ✨ Magic System: Learn and cast powerful spells")
        print("• 🐾 Companions: Recruit allies to aid your journey")
        print("• 🌤️ Dynamic Weather: Weather affects gameplay")
        print("• 🎲 Random Events: Unexpected encounters await")
        print("• 🏆 Achievements: Track your accomplishments")
        print("• 💾 Save/Load: Continue your adventure anytime")
        print("• ⚔️ Combat System: Strategic turn-based battles")
        print("• 🕐 Time System: Actions change based on time of day")
        print()
        print("💡 TIPS:")
        print("• Check your stats and inventory regularly")
        print("• Weather and time affect your abilities")
        print("• Save your game before important decisions")
        print("• Explore thoroughly to find hidden secrets")
        print()
        input("Press Enter to return to main menu...")
        self.display_menu()
        
    def show_achievements(self):
        """Display achievement system."""
        self.clear_screen()
        print(self.systems.achievement_system.display_achievements())
        input("Press Enter to return to main menu...")
        self.display_menu()
        
    def show_credits(self):
        """Display enhanced game credits."""
        self.clear_screen()
        self.print_border('~', 60)
        print("                      CREDITS")
        self.print_border('~', 60)
        print()
        print("🎮 Game Design & Programming: Adventure Creator")
        print("🎨 ASCII Art: Custom Designs")
        print("📖 Story: Original Fantasy Adventure")
        print("⚙️ Engine: Pure Python 3 with Enhanced Systems")
        print("🆕 New Features: RPG Systems, Weather, Magic & More")
        print()
        print("🌟 Enhanced Edition Features:")
        print("• Advanced character progression")
        print("• Dynamic weather and time systems")
        print("• Comprehensive inventory management")
        print("• Magic spell system with multiple schools")
        print("• Companion recruitment and management")
        print("• Achievement tracking system")
        print("• Save/load functionality")
        print("• Random event system")
        print("• Strategic combat mechanics")
        print()
        print("Thank you for playing Mystic Quest Enhanced Edition!")
        print()
        input("Press Enter to return to main menu...")
        self.display_menu()
        
    def load_game_menu(self):
        """Display load game menu."""
        self.clear_screen()
        saves = self.save_system.list_saves()
        
        if not saves:
            print("No saved games found!")
            input("Press Enter to return to main menu...")
            self.display_menu()
            return
            
        print("📁 LOAD GAME")
        self.print_border('-', 40)
        
        for i, save in enumerate(saves, 1):
            timestamp = save["timestamp"][:19] if save["timestamp"] != "Unknown" else "Unknown"
            print(f"{i}. {save['name']} - {save['player_name']} (Level {save['level']})")
            print(f"   Saved: {timestamp}")
            print()
            
        print(f"{len(saves) + 1}. Return to Main Menu")
        print()
        
        while True:
            try:
                choice = int(input("Select save file: "))
                if 1 <= choice <= len(saves):
                    save_name = saves[choice - 1]["name"]
                    success, message = self.save_system.load_game(save_name)
                    print(message)
                    if success:
                        input("Press Enter to continue your adventure...")
                        self.game_loop()
                        return
                    else:
                        input("Press Enter to continue...")
                        break
                elif choice == len(saves) + 1:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a valid number!")
                
        self.display_menu()
        
    def start_new_game(self):
        """Start a new enhanced adventure."""
        self.clear_screen()
        
        # Get player name
        print("🌟 Welcome to your enhanced adventure!")
        self.player_name = input("What is your name, brave adventurer? ").strip()
        if not self.player_name:
            self.player_name = "Adventurer"
            
        # Initialize enhanced systems
        self.systems.initialize_player(self.player_name)
        
        # Unlock first achievement
        achievement_msg = self.systems.achievement_system.unlock_achievement("first_steps")
        if achievement_msg:
            print(f"\n{achievement_msg}")
            time.sleep(2)
            
        # Start the adventure
        self.game_loop()
        
    def game_loop(self):
        """Main enhanced game loop."""
        while True:
            self.display_game_status()
            
            # Check for random events
            random_event = self.systems.random_events.trigger_random_event()
            if random_event:
                self.handle_random_event(random_event)
                
            # Main game menu during adventure
            choice = self.display_adventure_menu()
            
            if choice == 1:  # Continue Adventure
                self.continue_story()
            elif choice == 2:  # View Character
                self.display_character_info()
            elif choice == 3:  # Manage Inventory
                self.manage_inventory()
            elif choice == 4:  # Cast Spell
                self.cast_spell_menu()
            elif choice == 5:  # Save Game
                self.save_game_menu()
            elif choice == 6:  # Return to Main Menu
                break
                
    def display_game_status(self):
        """Display current game status."""
        self.clear_screen()
        
        # Weather and time
        weather_info = self.systems.weather_system.get_weather_info()
        time_of_day = self.systems.time_system.get_time_of_day()
        time_effects = self.systems.time_system.get_time_effects()
        
        print("🌟 MYSTIC QUEST - ADVENTURE STATUS")
        self.print_border('=', 50)
        print(f"🌤️ Weather: {weather_info}")
        print(f"🕐 Time: {time_of_day} - {time_effects}")
        print()
        
        # Quick stats
        stats = self.systems.stats_system.player_stats
        print(f"👤 {stats['name']} | Level {stats['level']}")
        print(f"❤️ Health: {stats['health']}/{stats['max_health']} | 💙 Mana: {stats['mana']}/{stats['max_mana']}")
        
        # Companions
        if self.systems.companion_system.companions:
            companions_text = ", ".join([c['name'] for c in self.systems.companion_system.companions])
            print(f"🐾 Companions: {companions_text}")
        print()
        
    def display_adventure_menu(self):
        """Display adventure menu options."""
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                  ADVENTURE MENU                         │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Continue Adventure                                  │")
        print("│  2. View Character Stats                                │")
        print("│  3. Manage Inventory                                    │")
        print("│  4. Cast Spell                                          │")
        print("│  5. Save Game                                           │")
        print("│  6. Return to Main Menu                                 │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = int(input("Choose your action (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Please enter a valid number.")
                
    def continue_story(self):
        """Continue the main story."""
        # This would integrate with your existing scenes
        # For now, let's create a simple story continuation
        self.clear_screen()
        
        print("🌟 Continuing your adventure...")
        print()
        
        # Advance time
        self.systems.time_system.advance_time(1)
        
        # Possibly change weather
        if random.random() < 0.3:
            self.systems.weather_system.change_weather()
            weather_info = self.systems.weather_system.get_weather_info()
            print(f"🌤️ The weather changes: {weather_info}")
            print()
            
        # Gain some experience
        leveled_up, exp_msg = self.systems.stats_system.gain_experience(random.randint(10, 30))
        print(exp_msg)
        if leveled_up:
            print(exp_msg)
            
        input("\nPress Enter to continue...")
        
    def display_character_info(self):
        """Display detailed character information."""
        self.clear_screen()
        print(self.systems.stats_system.display_stats())
        print(self.systems.companion_system.display_companions())
        
        # Display known spells
        if self.systems.magic_system.known_spells:
            print("✨ KNOWN SPELLS:")
            print("=" * 30)
            for spell_id in self.systems.magic_system.known_spells:
                spell = self.systems.magic_system.spell_database[spell_id]
                print(f"• {spell['name']} (Cost: {spell['cost']} mana)")
                print(f"  {spell['description']}")
            print()
            
        input("Press Enter to continue...")
        
    def manage_inventory(self):
        """Manage player inventory."""
        self.clear_screen()
        print(self.systems.inventory_system.display_inventory())
        
        if self.systems.inventory_system.items:
            print("1. Use Item")
            print("2. Return")
            
            choice = input("Choose action (1-2): ").strip()
            if choice == '1':
                self.use_item_menu()
                
        input("Press Enter to continue...")
        
    def use_item_menu(self):
        """Menu for using items."""
        items = list(self.systems.inventory_system.items.keys())
        if not items:
            return
            
        print("\nSelect item to use:")
        for i, item_id in enumerate(items, 1):
            item = self.systems.inventory_system.item_database[item_id]
            quantity = self.systems.inventory_system.items[item_id]
            print(f"{i}. {item['name']} x{quantity}")
            
        try:
            choice = int(input("Item number: ")) - 1
            if 0 <= choice < len(items):
                item_id = items[choice]
                self.use_item(item_id)
        except ValueError:
            print("Invalid choice!")
            
    def use_item(self, item_id):
        """Use an item from inventory."""
        item = self.systems.inventory_system.item_database[item_id]
        success, message = self.systems.inventory_system.remove_item(item_id)
        
        if success:
            print(f"\n✨ Used {item['name']}!")
            
            # Apply item effects
            if item['effect'] == 'heal_50':
                stats = self.systems.stats_system.player_stats
                old_health = stats['health']
                stats['health'] = min(stats['max_health'], stats['health'] + 50)
                healed = stats['health'] - old_health
                print(f"❤️ Restored {healed} health!")
                
            elif item['effect'] == 'mana_boost':
                stats = self.systems.stats_system.player_stats
                stats['max_mana'] += 10
                stats['mana'] = stats['max_mana']
                print("💙 Maximum mana increased by 10!")
                
            elif item['effect'] == 'experience_boost':
                leveled_up, exp_msg = self.systems.stats_system.gain_experience(100)
                print(f"⭐ {exp_msg}")
                
        else:
            print(message)
            
    def cast_spell_menu(self):
        """Menu for casting spells."""
        self.clear_screen()
        
        if not self.systems.magic_system.known_spells:
            print("You don't know any spells yet!")
            input("Press Enter to continue...")
            return
            
        print("✨ CAST SPELL")
        self.print_border('-', 30)
        
        for i, spell_id in enumerate(self.systems.magic_system.known_spells, 1):
            spell = self.systems.magic_system.spell_database[spell_id]
            print(f"{i}. {spell['name']} (Cost: {spell['cost']} mana)")
            print(f"   {spell['description']}")
            print()
            
        print(f"{len(self.systems.magic_system.known_spells) + 1}. Cancel")
        
        try:
            choice = int(input("Select spell: "))
            if 1 <= choice <= len(self.systems.magic_system.known_spells):
                spell_id = self.systems.magic_system.known_spells[choice - 1]
                self.cast_spell(spell_id)
        except ValueError:
            print("Invalid choice!")
            
        input("Press Enter to continue...")
        
    def cast_spell(self, spell_id):
        """Cast a specific spell."""
        stats = self.systems.stats_system.player_stats
        success, message = self.systems.magic_system.cast_spell(spell_id, stats)
        
        print(f"\n{message}")
        
        if success:
            self.spells_cast += 1
            
            # Apply spell effects
            spell = self.systems.magic_system.spell_database[spell_id]
            if spell['effect'] == 'restore_health':
                old_health = stats['health']
                stats['health'] = min(stats['max_health'], stats['health'] + 40)
                healed = stats['health'] - old_health
                print(f"❤️ Restored {healed} health!")
                
            # Check for spell caster achievement
            if self.spells_cast >= 10:
                achievement_msg = self.systems.achievement_system.unlock_achievement("spell_caster")
                if achievement_msg:
                    print(f"\n{achievement_msg}")
                    
    def save_game_menu(self):
        """Menu for saving the game."""
        self.clear_screen()
        print("💾 SAVE GAME")
        self.print_border('-', 30)
        
        save_name = input("Enter save name (or press Enter for quicksave): ").strip()
        if not save_name:
            save_name = "quicksave"
            
        success, message = self.save_system.save_game(save_name)
        print(f"\n{message}")
        input("Press Enter to continue...")
        
    def handle_random_event(self, event):
        """Handle a random event."""
        self.clear_screen()
        print("🎲 RANDOM EVENT!")
        self.print_border('*', 40)
        print(f"✨ {event['name']}")
        print(f"{event['description']}")
        print()
        
        if event['type'] == 'blessing':
            # Grant random benefit
            benefit = random.choice(['health', 'mana', 'experience'])
            stats = self.systems.stats_system.player_stats
            
            if benefit == 'health':
                stats['health'] = stats['max_health']
                print("❤️ Your health is fully restored!")
            elif benefit == 'mana':
                stats['mana'] = stats['max_mana']
                print("💙 Your mana is fully restored!")
            else:
                leveled_up, exp_msg = self.systems.stats_system.gain_experience(50)
                print(f"⭐ {exp_msg}")
                
        elif event['type'] == 'trade':
            print("The merchant offers you a rare item!")
            success, message = self.systems.inventory_system.add_item("magic_crystal")
            print(message)
            
        input("\nPress Enter to continue...")
        
    def exit_game(self):
        """Exit the enhanced game."""
        self.clear_screen()
        self.ascii_art.display_farewell()
        print("Thank you for playing Mystic Quest Enhanced Edition!")
        print("Your adventure awaits your return...")
        print()
        print("🌟 New features you experienced:")
        print("• Advanced character progression")
        print("• Dynamic weather and time systems")
        print("• Magic spells and inventory management")
        print("• Achievement tracking")
        print("• Save/load functionality")
        print("• And much more!")
        sys.exit(0)


def main():
    """Main function to start the enhanced game."""
    try:
        game = EnhancedGameEngine()
        game.display_menu()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please restart the game.")
        sys.exit(1)


if __name__ == "__main__":
    main()
