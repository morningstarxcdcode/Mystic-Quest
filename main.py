#!/usr/bin/env python3
"""
Mystic Quest - A Text-Based Adventure Game
==========================================
A modular, beautiful text adventure with ASCII art and multiple storylines.

Author: Adventure Game Creator
Version: 1.0
"""

import os
import sys
import time
from ascii_art import AsciiArt
from scenes.intro import IntroScene
from scenes.forest import ForestScene
from scenes.cave import CaveScene
from scenes.boss import BossScene
from scenes.ending import EndingScene


class GameEngine:
    """Main game engine that manages the flow and state of the adventure."""
    
    def __init__(self):
        self.player_name = ""
        self.player_health = 100
        self.player_inventory = []
        self.game_state = {}
        self.ascii_art = AsciiArt()
        
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
        print("Welcome to MYSTIC QUEST - A Text Adventure")
        self.print_border('=', 60)
        print()
        
    def display_menu(self):
        """Display the main menu and handle user choice."""
        self.display_title()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                    MAIN MENU                            │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Start New Adventure                                 │")
        print("│  2. Game Instructions                                   │")
        print("│  3. Credits                                             │")
        print("│  4. Exit Game                                           │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            choice = input("Enter your choice (1-4): ").strip()
            if choice == '1':
                self.start_game()
                break
            elif choice == '2':
                self.show_instructions()
            elif choice == '3':
                self.show_credits()
            elif choice == '4':
                self.exit_game()
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                
    def show_instructions(self):
        """Display game instructions."""
        self.clear_screen()
        self.print_border('*', 60)
        print("                    INSTRUCTIONS")
        self.print_border('*', 60)
        print()
        print("• Make choices by entering the number (1, 2, or 3)")
        print("• Your decisions affect the story outcome")
        print("• Collect items and manage your health wisely")
        print("• Multiple endings await based on your choices")
        print("• Type your responses carefully and press Enter")
        print()
        input("Press Enter to return to main menu...")
        self.display_menu()
        
    def show_credits(self):
        """Display game credits."""
        self.clear_screen()
        self.print_border('~', 60)
        print("                      CREDITS")
        self.print_border('~', 60)
        print()
        print("Game Design & Programming: Adventure Creator")
        print("ASCII Art: Custom Designs")
        print("Story: Original Fantasy Adventure")
        print("Engine: Pure Python 3")
        print()
        print("Thank you for playing Mystic Quest!")
        print()
        input("Press Enter to return to main menu...")
        self.display_menu()
        
    def exit_game(self):
        """Exit the game with a farewell message."""
        self.clear_screen()
        self.ascii_art.display_farewell()
        print("Thank you for playing Mystic Quest!")
        print("Adventure awaits your return...")
        sys.exit(0)
        
    def start_game(self):
        """Start the main game sequence."""
        self.clear_screen()
        
        # Get player name
        print("Before we begin your adventure...")
        self.player_name = input("What is your name, brave adventurer? ").strip()
        if not self.player_name:
            self.player_name = "Adventurer"
            
        # Initialize scenes
        intro_scene = IntroScene(self)
        forest_scene = ForestScene(self)
        cave_scene = CaveScene(self)
        boss_scene = BossScene(self)
        ending_scene = EndingScene(self)
        
        # Game flow
        intro_choice = intro_scene.play()
        
        if intro_choice == 1:  # Forest path
            forest_result = forest_scene.play()
            if forest_result == "boss":
                boss_result = boss_scene.play()
                ending_scene.play(boss_result)
            else:
                ending_scene.play(forest_result)
                
        elif intro_choice == 2:  # Cave path
            cave_result = cave_scene.play()
            if cave_result == "boss":
                boss_result = boss_scene.play()
                ending_scene.play(boss_result)
            else:
                ending_scene.play(cave_result)
                
        else:  # Rest choice
            ending_scene.play("rest")
            
        # Return to main menu
        input("\nPress Enter to return to main menu...")
        self.display_menu()


def main():
    """Main function to start the game."""
    try:
        game = GameEngine()
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
