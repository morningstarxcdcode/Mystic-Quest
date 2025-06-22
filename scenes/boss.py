"""
Boss Scene for Mystic Quest
===========================
The climactic encounter with the Shadow Guardian - the final challenge.
"""

import time
import random


class BossScene:
    """The final boss encounter with multiple resolution paths."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        
    def play(self):
        """Play the boss scene and return the result."""
        self.game.clear_screen()
        
        # Display boss ASCII art
        self.game.ascii_art.display_boss()
        
        print()
        self.game.print_border('!', 60)
        
        # Boss encounter story
        boss_story = f"""
{self.game.player_name}, your journey has led you to the heart of the ancient 
realm, where shadows gather like living things. Before you stands the Shadow 
Guardian - a towering figure wreathed in darkness, its eyes burning with 
the pain of centuries of solitude.

The air crackles with dark energy as the Guardian's voice echoes through 
the chamber like thunder:

"SO... ANOTHER MORTAL COMES TO DISTURB MY ETERNAL VIGIL. I HAVE GUARDED 
THESE SECRETS FOR A THOUSAND YEARS, AND I WILL NOT BE MOVED BY ONE SUCH 
AS YOU!"

The Guardian raises its massive form, ready for battle. But you sense 
something beneath the rage - a deep, aching loneliness that has festered 
for centuries...
        """
        
        self.game.print_with_delay(boss_story, 0.02)
        
        print()
        self.game.print_border('!', 60)
        print()
        
        # Check for special advantages from previous choices
        return self.determine_boss_encounter()
        
    def determine_boss_encounter(self):
        """Determine the type of boss encounter based on player's journey."""
        
        # Check for peaceful resolution options first
        if (self.game.game_state.get("knows_peace_ritual") or 
            self.game.game_state.get("saw_true_self") or
            self.game.game_state.get("knows_guardian_history")):
            return self.peaceful_resolution()
            
        # Check for special powers or advantages
        elif (self.game.game_state.get("has_fairy_blessing") or 
              self.game.game_state.get("crystal_power") or
              self.game.game_state.get("passed_wolf_trial")):
            return self.power_confrontation()
            
        # Check for wisdom-based approaches
        elif (self.game.game_state.get("has_fairy_wisdom") or
              self.game.game_state.get("studied_crystal") or
              self.game.game_state.get("knows_binding_spell")):
            return self.wisdom_confrontation()
            
        # Default combat encounter
        else:
            return self.combat_encounter()
            
    def peaceful_resolution(self):
        """Handle peaceful resolution of the boss encounter."""
        self.game.clear_screen()
        
        peace_story = f"""
🕊️ THE PATH OF UNDERSTANDING 🕊️

{self.game.player_name}, drawing upon the wisdom you've gained on your 
journey, you step forward with open hands instead of raised fists.

"Shadow Guardian," you call out, your voice steady and compassionate, 
"I have not come to fight you. I have come to understand."

The Guardian pauses, surprised by your words. For the first time in 
centuries, someone has spoken to it without fear or aggression.
        """
        
        self.game.print_with_delay(peace_story, 0.02)
        
        print()
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                 WORDS OF COMPASSION                     │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. 💭 'You have been alone for so long...'            │")
        print("│  2. 🤝 'I offer you friendship, not battle.'           │")
        print("│  3. 🌅 'Your vigil can end. You can find peace.'       │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        while True:
            try:
                choice = input("What do you say to the Shadow Guardian? (1-3): ").strip()
                
                if choice in ['1', '2', '3']:
                    return self.resolve_peacefully(choice)
                else:
                    print("Please enter 1, 2, or 3 to choose your words.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, or 3).")
                continue
                
    def resolve_peacefully(self, choice):
        """Resolve the encounter peacefully based on the player's words."""
        self.game.clear_screen()
        
        if choice == '1':
            resolution_text = f"""
💭 THE POWER OF EMPATHY 💭

{self.game.player_name} speaks with deep understanding:
"You have been alone for so long, carrying this burden without anyone 
to share it with. That pain has turned to anger, but underneath, 
I see the noble guardian you once were."

The Shadow Guardian's form begins to shimmer, the darkness slowly 
lifting like morning mist. For the first time in centuries, it 
remembers what it was like to be understood.

"Yes..." the Guardian whispers, its voice no longer thunderous but 
filled with ancient sadness. "So very long... alone..."
            """
            
        elif choice == '2':
            resolution_text = f"""
🤝 THE OFFER OF FRIENDSHIP 🤝

{self.game.player_name} extends a hand in friendship:
"I offer you friendship, not battle. You don't have to guard these 
secrets alone anymore. Let me share your burden."

The Shadow Guardian stares at the offered hand - the first gesture 
of kindness it has received in a millennium. Slowly, the darkness 
begins to recede, revealing the noble spirit beneath.

"Friendship..." the Guardian repeats wonderingly. "I had forgotten 
such a thing existed..."
            """
            
        else:  # choice == '3'
            resolution_text = f"""
🌅 THE PROMISE OF PEACE 🌅

{self.game.player_name} speaks with gentle authority:
"Your vigil can end. You have guarded these secrets faithfully, 
but now you can find peace. Your duty is complete."

The Shadow Guardian's burning eyes dim to a soft glow as centuries 
of tension finally begin to release. The weight of eternal duty 
starts to lift from its shoulders.

"Peace..." the Guardian breathes. "Can it truly be possible?"
            """
            
        self.game.print_with_delay(resolution_text, 0.02)
        
        print()
        final_resolution = f"""
The Shadow Guardian's form continues to change, darkness giving way to 
light. Where once stood a creature of shadow and rage, now stands a 
majestic being of silver and starlight - the true Guardian, freed from 
centuries of corruption.

"Thank you, {self.game.player_name}," the Guardian says, its voice now 
warm and grateful. "You have given me the greatest gift - the reminder 
that I am not alone. Take this blessing as a token of my gratitude."

The Guardian touches your forehead, and you feel a warm light fill your 
entire being. You have not only survived the encounter - you have healed 
an ancient wound and made the world a brighter place.
        """
        
        self.game.print_with_delay(final_resolution, 0.02)
        time.sleep(2)
        return "peaceful_victory"
        
    def power_confrontation(self):
        """Handle power-based confrontation with the boss."""
        self.game.clear_screen()
        
        power_story = f"""
⚡ THE CLASH OF POWERS ⚡

{self.game.player_name}, you feel the power you've gained on your journey 
surging through you. Whether it's the fairy's blessing, the crystal's 
energy, or the wolf's strength, you are ready to face the Shadow Guardian 
with force.

"If battle is what you seek, Guardian, then battle you shall have!" 
you declare, power crackling around you like lightning.

The Guardian roars in response, dark energy swirling around its massive 
form. The very air trembles with the clash of opposing forces!
        """
        
        self.game.print_with_delay(power_story, 0.02)
        
        # Determine outcome based on specific powers
        if self.game.game_state.get("crystal_power") == "balanced":
            return self.balanced_power_victory()
        elif self.game.game_state.get("has_fairy_blessing"):
            return self.fairy_blessed_victory()
        elif self.game.game_state.get("passed_wolf_trial"):
            return self.strength_victory()
        else:
            return self.power_struggle()
            
    def balanced_power_victory(self):
        """Victory through balanced crystal power."""
        victory_text = f"""
💎 PERFECT BALANCE 💎

{self.game.player_name}, the balanced crystal power flows through you 
with perfect harmony. You don't seek to destroy the Guardian, but to 
restore the balance that was lost.

Your crystal energy meets the Guardian's darkness, and instead of 
clashing, they begin to harmonize. The corruption that has plagued 
the Guardian for centuries is slowly purified by your balanced power.

"Impossible..." the Guardian gasps as its form begins to change. 
"The balance... it returns..."

You have achieved victory not through destruction, but through restoration!
        """
        
        self.game.print_with_delay(victory_text, 0.02)
        time.sleep(2)
        return "power_victory"
        
    def fairy_blessed_victory(self):
        """Victory through fairy blessing."""
        victory_text = f"""
✨ NATURE'S TRIUMPH ✨

{self.game.player_name}, the fairy blessing fills you with the pure 
power of nature itself. Flowers bloom at your feet even in this dark 
place, and the Guardian's shadows recoil from your radiant light.

"The old magic..." the Guardian whispers in awe. "The magic of life 
and growth... I had forgotten its beauty..."

Your nature magic doesn't destroy the Guardian's darkness - it 
transforms it, turning shadow into fertile soil from which new 
life can grow. Victory through transformation!
        """
        
        self.game.print_with_delay(victory_text, 0.02)
        time.sleep(2)
        return "nature_victory"
        
    def strength_victory(self):
        """Victory through proven strength."""
        victory_text = f"""
🐺 THE TRIAL'S REWARD 🐺

{self.game.player_name}, the strength you proved in the wolf's trial 
now serves you well. But this is not mere physical strength - it's 
the strength of character, the courage to face any challenge.

The Guardian recognizes this true strength and nods with respect.

"You have proven yourself worthy," the Guardian acknowledges. "Few 
mortals possess such genuine courage. I yield to your strength of spirit."

Victory through proven worth and courage!
        """
        
        self.game.print_with_delay(victory_text, 0.02)
        time.sleep(2)
        return "strength_victory"
        
    def wisdom_confrontation(self):
        """Handle wisdom-based confrontation."""
        self.game.clear_screen()
        
        wisdom_story = f"""
🧠 THE BATTLE OF MINDS 🧠

{self.game.player_name}, you realize that this battle cannot be won 
through force alone. Drawing upon the wisdom you've gained, you 
prepare to face the Guardian with knowledge and understanding.

"Guardian," you call out, "I challenge not your strength, but your 
reasoning. Let us settle this through wisdom, not warfare."

The Guardian pauses, intrigued despite itself. It has been so long 
since anyone has offered intellectual challenge rather than brute force.
        """
        
        self.game.print_with_delay(wisdom_story, 0.02)
        
        # Wisdom-based victory
        wisdom_resolution = f"""
Through careful reasoning and the knowledge you've gained, you help 
the Guardian understand that its long vigil has become a prison of 
its own making. True guardianship means knowing when to let go.

The Guardian's eyes clear as understanding dawns. "You speak truth, 
young one. Wisdom indeed conquers where force fails."

Victory through enlightenment!
        """
        
        self.game.print_with_delay(wisdom_resolution, 0.02)
        time.sleep(2)
        return "wisdom_victory"
        
    def combat_encounter(self):
        """Handle direct combat encounter."""
        self.game.clear_screen()
        
        combat_story = f"""
⚔️ THE FINAL BATTLE ⚔️

{self.game.player_name}, with no special powers or wisdom to guide you, 
you must face the Shadow Guardian in direct combat. Your courage and 
determination are your only weapons.

The battle is fierce and challenging, testing every ounce of your 
resolve. But sometimes, pure courage and a noble heart are enough 
to overcome even the greatest darkness.
        """
        
        self.game.print_with_delay(combat_story, 0.02)
        
        # Random combat outcome based on health and choices
        if self.game.player_health >= 80:
            combat_result = "victory"
        elif self.game.player_health >= 50:
            combat_result = random.choice(["victory", "hard_victory"])
        else:
            combat_result = random.choice(["hard_victory", "defeat"])
            
        if combat_result == "victory":
            print(f"\n⚔️ {self.game.player_name} fights with incredible determination!")
            print("Through sheer courage and will, you overcome the Shadow Guardian!")
            time.sleep(2)
            return "combat_victory"
        elif combat_result == "hard_victory":
            print(f"\n💪 {self.game.player_name} achieves victory, but at great cost...")
            print("You are wounded but victorious. Sometimes winning requires sacrifice.")
            time.sleep(2)
            return "hard_victory"
        else:
            print(f"\n💀 Despite {self.game.player_name}'s best efforts, the Guardian proves too powerful...")
            print("But your courage has not gone unnoticed. Even in defeat, you have honor.")
            time.sleep(2)
            return "honorable_defeat"
