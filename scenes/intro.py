"""
Intro Scene for Mystic Quest
============================
The opening scene where the adventure begins and the player makes their first choice.
"""

import time


class IntroScene:
    """The introductory scene of the game."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        
    def play(self):
        """Play the intro scene and return the player's choice."""
        self.game.clear_screen()
        
        # Display intro ASCII art
        self.game.ascii_art.display_intro_scene()
        
        print()
        self.game.print_border('-', 60)
        
        # Story introduction
        story_text = f"""
Greetings, {self.game.player_name}!

You find yourself standing at the edge of a mystical realm, where ancient 
magic still flows through the very air you breathe. Before you lie three 
paths, each leading to a different destiny.

The wind carries whispers of forgotten legends, and your heart pounds with 
the thrill of adventure. Your journey begins now...
        """
        
        self.game.print_with_delay(story_text, 0.02)
        
        print()
        self.game.print_border('-', 60)
        print()
        
        # Present choices
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                   CHOOSE YOUR PATH                      │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 🌲 Enter the Enchanted Forest                      │")
        print("│     (A path of nature's mysteries and hidden magic)     │")
        print("│                                                         │")
        print("│  2. 🕳️  Descend into the Crystal Cave                  │")
        print("│     (A journey into the depths of ancient secrets)     │")
        print("│                                                         │")
        print("│  3. 🏕️  Rest and meditate by the sacred spring        │")
        print("│     (Sometimes wisdom comes from stillness)            │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        # Get player choice
        while True:
            try:
                choice = input(f"{self.game.player_name}, what is your choice? (1-3): ").strip()
                
                if choice == '1':
                    print(f"\n🌲 {self.game.player_name} steps into the Enchanted Forest...")
                    time.sleep(1.5)
                    return 1
                elif choice == '2':
                    print(f"\n🕳️ {self.game.player_name} descends into the Crystal Cave...")
                    time.sleep(1.5)
                    return 2
                elif choice == '3':
                    print(f"\n🏕️ {self.game.player_name} chooses the path of contemplation...")
                    time.sleep(1.5)
                    return 3
                else:
                    print("Please enter 1, 2, or 3 to choose your path.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
