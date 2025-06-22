"""
ASCII Art Collection for Mystic Quest
=====================================
Beautiful ASCII art scenes and decorations for the text adventure game.
"""

import time


class AsciiArt:
    """Collection of ASCII art for various game scenes."""
    
    def __init__(self):
        pass
        
    def display_with_delay(self, art, delay=0.1):
        """Display ASCII art with a slight delay for dramatic effect."""
        for line in art.split('\n'):
            print(line)
            time.sleep(delay)
            
    def display_title(self):
        """Display the main title ASCII art."""
        title_art = """
    ███╗   ███╗██╗   ██╗███████╗████████╗██╗ ██████╗ 
    ████╗ ████║╚██╗ ██╔╝██╔════╝╚══██╔══╝██║██╔════╝ 
    ██╔████╔██║ ╚████╔╝ ███████╗   ██║   ██║██║      
    ██║╚██╔╝██║  ╚██╔╝  ╚════██║   ██║   ██║██║      
    ██║ ╚═╝ ██║   ██║   ███████║   ██║   ██║╚██████╗ 
    ╚═╝     ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝ ╚═════╝ 
                                                      
         ██████╗ ██╗   ██╗███████╗███████╗████████╗   
        ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝   
        ██║   ██║██║   ██║█████╗  ███████╗   ██║      
        ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║      
        ╚██████╔╝╚██████╔╝███████╗███████║   ██║      
         ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝      
        """
        print(title_art)
        
    def display_forest(self):
        """Display forest scene ASCII art."""
        forest_art = """
                    🌲 THE ENCHANTED FOREST 🌲
        
                         /\\    /\\    /\\
                        /  \\  /  \\  /  \\
                       /____\\/____\\/____\\
                         ||    ||    ||
                         ||    ||    ||
        
            🍄     The ancient trees whisper secrets...     🍄
        
                    ╔══════════════════════════╗
                    ║   Sunlight filters down  ║
                    ║   through emerald leaves ║
                    ╚══════════════════════════╝
        """
        self.display_with_delay(forest_art, 0.05)
        
    def display_cave(self):
        """Display cave scene ASCII art."""
        cave_art = """
                      🕳️  THE MYSTERIOUS CAVE  🕳️
        
                    ╔════════════════════════════╗
                    ║                            ║
                    ║    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    ║
                    ║   ▄                   ▄   ║
                    ║  ▄   Dark passages     ▄  ║
                    ║ ▄    lead deeper...     ▄ ║
                    ║▄                         ▄║
                    ║                            ║
                    ╚════════════════════════════╝
        
                💎 Crystals glimmer in the darkness... 💎
        """
        self.display_with_delay(cave_art, 0.05)
        
    def display_boss(self):
        """Display boss encounter ASCII art."""
        boss_art = """
                    ⚔️  THE SHADOW GUARDIAN  ⚔️
        
                           ╔═══════════╗
                           ║  👹      ║
                           ║    ╲   ╱  ║
                           ║     ╲ ╱   ║
                           ║      ╳    ║
                           ║     ╱ ╲   ║
                           ║    ╱   ╲  ║
                           ║           ║
                           ╚═══════════╝
        
                    "WHO DARES DISTURB MY SLUMBER?"
        
                    ⚡ Lightning crackles in the air... ⚡
        """
        self.display_with_delay(boss_art, 0.08)
        
    def display_treasure(self):
        """Display treasure discovery ASCII art."""
        self.display_hidden_treasure()
        
    def display_treasure_simple(self):
        """Display simple treasure discovery ASCII art."""
        treasure_art = """
                        💰 TREASURE DISCOVERED! 💰
        
                            ╔═══════════╗
                            ║  ✨ 💎 ✨  ║
                            ║ 💰 👑 💰 ║
                            ║  ✨ 💎 ✨  ║
                            ╚═══════════╝
        
                    Ancient riches beyond imagination!
        """
        self.display_with_delay(treasure_art, 0.05)
        
    def display_victory(self):
        """Display victory ASCII art."""
        victory_art = """
                        🏆 VICTORY ACHIEVED! 🏆
        
                    ╔═══════════════════════════════╗
                    ║                               ║
                    ║        ⭐ HERO ⭐           ║
                    ║                               ║
                    ║    You have proven yourself   ║
                    ║    worthy of legend!          ║
                    ║                               ║
                    ╚═══════════════════════════════╝
        
                        🎉 Congratulations! 🎉
        """
        self.display_with_delay(victory_art, 0.05)
        
    def display_defeat(self):
        """Display defeat ASCII art."""
        defeat_art = """
                        💀 DEFEAT... 💀
        
                    ╔═══════════════════════════════╗
                    ║                               ║
                    ║         ⚰️  R.I.P  ⚰️         ║
                    ║                               ║
                    ║    Your adventure ends here   ║
                    ║    But legends never die...   ║
                    ║                               ║
                    ╚═══════════════════════════════╝
        
                        Try again, brave soul!
        """
        self.display_with_delay(defeat_art, 0.05)
        
    def display_peaceful_ending(self):
        """Display peaceful ending ASCII art."""
        peaceful_art = """
                    🕊️ PEACEFUL RESOLUTION 🕊️
        
                    ╔═══════════════════════════════╗
                    ║                               ║
                    ║        🌅 WISDOM 🌅          ║
                    ║                               ║
                    ║   Sometimes the greatest      ║
                    ║   adventure is knowing        ║
                    ║   when to rest...             ║
                    ║                               ║
                    ╚═══════════════════════════════╝
        
                        🌸 Inner peace achieved 🌸
        """
        self.display_with_delay(peaceful_art, 0.05)
        
    def display_farewell(self):
        """Display farewell ASCII art."""
        farewell_art = """
                    ✨ FAREWELL, ADVENTURER! ✨
        
                    ╔═══════════════════════════════╗
                    ║                               ║
                    ║         Until we meet         ║
                    ║         again on the          ║
                    ║         paths of destiny...   ║
                    ║                               ║
                    ║            🌟 END 🌟          ║
                    ║                               ║
                    ╚═══════════════════════════════╝
        """
        self.display_with_delay(farewell_art, 0.05)
        
    def display_intro_scene(self):
        """Display intro scene ASCII art."""
        intro_art = """
                    🌄 YOUR ADVENTURE BEGINS 🌄
        
                    ╔═══════════════════════════════╗
                    ║                               ║
                    ║    You stand at a crossroads  ║
                    ║    in an ancient land...      ║
                    ║                               ║
                    ║         🛤️  ⚡  🛤️           ║
                    ║                               ║
                    ║    Which path calls to you?   ║
                    ║                               ║
                    ╚═══════════════════════════════╝
        """
        self.display_with_delay(intro_art, 0.05)
        
    def display_hidden_treasure(self):
        """Display hidden treasure room discovery ASCII art."""
        treasure_art = """
                    🗝️ HIDDEN TREASURE CHAMBER 🗝️
        
                ╔═══════════════════════════════════════╗
                ║  💎    ✨    👑    ✨    💎        ║
                ║    ╔═══════════════════════════╗      ║
                ║ 💰 ║  🔮  RIDDLE  TRIAL  🔮  ║ 💰   ║
                ║    ║                         ║      ║
                ║ 💎 ║   🔵    🟡    🔴      ║ 💎   ║
                ║    ║                         ║      ║
                ║ 👑 ║  Three Orbs of Wisdom   ║ 👑   ║
                ║    ╚═══════════════════════════╝      ║
                ║  ✨    💰    💎    💰    ✨        ║
                ╚═══════════════════════════════════════╝
        
                Ancient magic fills the air with possibility...
        """
        self.display_with_delay(treasure_art, 0.05)
        
    def display_riddle_master(self):
        """Display riddle master victory ASCII art."""
        riddle_art = """
                    🧩 MASTER OF RIDDLES 🧩
        
                    ╔═══════════════════════════════╗
                    ║                               ║
                    ║        🧠 WISDOM 🧠          ║
                    ║                               ║
                    ║   🔵 ✅  🟡 ✅  🔴 ✅      ║
                    ║                               ║
                    ║    All riddles conquered!     ║
                    ║    Intelligence triumphs!     ║
                    ║                               ║
                    ╚═══════════════════════════════╝
        
                        🏆 ULTIMATE TREASURE 🏆
        """
        self.display_with_delay(riddle_art, 0.05)
        
    def display_secret_garden(self):
        """Display secret underground garden ASCII art."""
        garden_art = """
                    🌸 SECRET UNDERGROUND GARDEN 🌸
        
                    ╔═══════════════════════════════╗
                    ║  🌺    🌸    🌼    🌻    🌷  ║
                    ║                               ║
                    ║    💧 Crystal Spring 💧      ║
                    ║         ╔═══════╗             ║
                    ║  🌿     ║ ✨💎✨ ║     🌿     ║
                    ║         ║  💧💧  ║             ║
                    ║  🍄     ╚═══════╝     🍄     ║
                    ║                               ║
                    ║  🌺    🌸    🌼    🌻    🌷  ║
                    ╚═══════════════════════════════╝
        
                    A sanctuary of eternal beauty and peace...
        """
        self.display_with_delay(garden_art, 0.05)
