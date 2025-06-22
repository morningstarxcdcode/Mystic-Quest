"""
Ending Scene for Mystic Quest
=============================
Multiple endings based on the player's choices and outcomes throughout the game.
"""

import time


class EndingScene:
    """The final scene with multiple possible endings."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        
    def play(self, outcome):
        """Play the appropriate ending based on the outcome."""
        self.game.clear_screen()
        
        # Route to appropriate ending
        if outcome == "peaceful_victory":
            self.peaceful_victory_ending()
        elif outcome == "power_victory":
            self.power_victory_ending()
        elif outcome == "nature_victory":
            self.nature_victory_ending()
        elif outcome == "strength_victory":
            self.strength_victory_ending()
        elif outcome == "wisdom_victory":
            self.wisdom_victory_ending()
        elif outcome == "combat_victory":
            self.combat_victory_ending()
        elif outcome == "hard_victory":
            self.hard_victory_ending()
        elif outcome == "honorable_defeat":
            self.honorable_defeat_ending()
        elif outcome == "peaceful":
            self.peaceful_path_ending()
        elif outcome == "rest":
            self.restful_ending()
        elif outcome == "treasure_master":
            self.treasure_master_ending()
        elif outcome == "secret_garden":
            self.secret_garden_ending()
        elif outcome == "ancient_knowledge":
            self.ancient_knowledge_ending()
        elif outcome == "wise_restraint":
            self.wise_restraint_ending()
        else:
            self.default_ending()
            
    def peaceful_victory_ending(self):
        """Ending for peaceful resolution of the boss fight."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
🕊️ THE PEACEMAKER'S TRIUMPH 🕊️

{self.game.player_name}, your journey has reached its most beautiful 
conclusion. Through compassion and understanding, you have not only 
defeated the Shadow Guardian - you have healed it.

The ancient realm is transformed by your act of mercy. Where once 
darkness reigned, now light and shadow dance together in perfect 
harmony. The Guardian, restored to its true noble form, becomes 
your eternal ally and friend.

Word of your deed spreads throughout the land. You are remembered 
not as a conqueror, but as a healer - one who chose understanding 
over violence, compassion over conquest.

The realm prospers under the Guardian's renewed protection, and you 
are forever welcome in this magical place. You have proven that the 
greatest victories are won not through strength of arm, but through 
strength of heart.

🌟 ACHIEVEMENT UNLOCKED: THE PEACEMAKER 🌟
"True heroes heal rather than harm."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("LEGENDARY PEACEMAKER")
        
    def power_victory_ending(self):
        """Ending for power-based victory."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
⚡ THE MASTER OF POWER ⚡

{self.game.player_name}, you have proven that with great power comes 
great responsibility. Your mastery of the mystical forces you 
encountered has allowed you to restore balance to the ancient realm.

The Shadow Guardian, purified by your balanced approach to power, 
now serves as a protector once more. The realm's magical energies 
flow in harmony, and you are recognized as a true master of the 
mystical arts.

Your name becomes legend among those who study the ancient ways. 
You have shown that power without wisdom is destruction, but power 
guided by wisdom can heal the world.

The crystals in the cave now sing with pure energy, the forest 
blooms with renewed life, and the realm enters a golden age of 
magical prosperity.

⚡ ACHIEVEMENT UNLOCKED: THE POWER MASTER ⚡
"True power lies in knowing how to use it wisely."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("MASTER OF MYSTICAL POWER")
        
    def nature_victory_ending(self):
        """Ending for nature-blessed victory."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
🌸 THE NATURE'S CHAMPION 🌸

{self.game.player_name}, blessed by the fairies and empowered by 
nature's own magic, you have brought life and growth to a realm 
that had known only shadow and stagnation.

Your victory transforms the entire landscape. The Enchanted Forest 
expands, bringing green life to barren places. Flowers bloom in 
the crystal caves, and even the darkest corners of the realm now 
know the touch of growing things.

The fairy queen herself appears to crown you as Nature's Champion, 
and all the creatures of the wild acknowledge you as their friend 
and protector. You have become a bridge between the mortal world 
and the realm of natural magic.

Wherever you walk, life flourishes. Your legacy is one of growth, 
renewal, and the eternal cycle of life that conquers all darkness.

🌺 ACHIEVEMENT UNLOCKED: NATURE'S CHAMPION 🌺
"Life finds a way, and you are its guide."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("CHAMPION OF NATURE")
        
    def strength_victory_ending(self):
        """Ending for strength-based victory."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
🐺 THE PROVEN WARRIOR 🐺

{self.game.player_name}, your courage and strength of character have 
earned you victory through the most honorable means. The Shadow 
Guardian, recognizing your true warrior's spirit, yields with respect.

Your triumph is celebrated throughout the realm as a victory of 
courage over fear, determination over despair. The spirit wolf 
appears to acknowledge you as a true warrior, one who fights not 
for glory but for justice.

You are granted the title of Guardian's Successor, and the ancient 
realm places itself under your protection. Your strength becomes 
a shield for the innocent and a beacon of hope for the lost.

Tales of your courage inspire others to face their own shadows 
with bravery. You have proven that true strength comes not from 
power, but from the courage to do what is right.

⚔️ ACHIEVEMENT UNLOCKED: THE PROVEN WARRIOR ⚔️
"Courage is not the absence of fear, but action in spite of it."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("PROVEN WARRIOR")
        
    def wisdom_victory_ending(self):
        """Ending for wisdom-based victory."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
📚 THE SAGE OF AGES 📚

{self.game.player_name}, your victory through wisdom and understanding 
marks you as one of the great sages of the age. You have proven that 
knowledge and insight can overcome even the mightiest foes.

The ancient symbols in the cave now glow with renewed purpose, 
recording your deeds for future generations to study. The Shadow 
Guardian, enlightened by your wisdom, becomes a teacher rather 
than a threat.

You establish a great library in the crystal caves, where seekers 
of knowledge from across the realm come to learn. Your wisdom 
becomes a light that guides others through their own dark times.

The realm enters an age of learning and enlightenment, with you 
as its greatest teacher. Your legacy is one of minds opened, 
mysteries solved, and wisdom shared freely with all.

🧠 ACHIEVEMENT UNLOCKED: THE SAGE OF AGES 🧠
"The pen is mightier than the sword, and wisdom mightier than both."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("SAGE OF AGES")
        
    def combat_victory_ending(self):
        """Ending for direct combat victory."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
⚔️ THE VALIANT HERO ⚔️

{self.game.player_name}, through sheer determination and unwavering 
courage, you have achieved victory against overwhelming odds. Your 
triumph is a testament to the power of the human spirit.

Though you lacked magical powers or ancient wisdom, your pure heart 
and indomitable will proved stronger than any enchantment. The 
Shadow Guardian, defeated by your relentless courage, acknowledges 
your heroism.

Your victory inspires songs and stories that will be told for 
generations. You have proven that ordinary people can achieve 
extraordinary things when they refuse to give up.

The realm celebrates you as a true hero - one who succeeded not 
through gifts or advantages, but through the simple refusal to 
surrender in the face of darkness.

🏆 ACHIEVEMENT UNLOCKED: THE VALIANT HERO 🏆
"Heroes are made, not born, in moments of greatest trial."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("VALIANT HERO")
        
    def hard_victory_ending(self):
        """Ending for costly victory."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
💪 THE SCARRED CHAMPION 💪

{self.game.player_name}, your victory has come at great personal cost, 
but your sacrifice has not been in vain. Though wounded in body, 
your spirit burns brighter than ever.

The Shadow Guardian, moved by your willingness to sacrifice for 
others, grants you a healing that goes beyond the physical. Your 
scars become marks of honor, proof of your dedication to justice.

Your hard-won victory teaches the realm that some things are worth 
fighting for, no matter the cost. You become a symbol of sacrifice 
and determination, inspiring others to persevere through their 
own struggles.

Though the path was difficult, you have emerged stronger and wiser. 
Your victory is all the sweeter for the challenges you overcame 
to achieve it.

🩹 ACHIEVEMENT UNLOCKED: THE SCARRED CHAMPION 🩹
"Victory is sweetest when it costs us something precious."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("SCARRED CHAMPION")
        
    def honorable_defeat_ending(self):
        """Ending for honorable defeat."""
        self.game.ascii_art.display_defeat()
        
        ending_text = f"""
🎖️ THE HONORABLE FALLEN 🎖️

{self.game.player_name}, though you did not achieve victory in battle, 
your courage in the face of overwhelming odds has earned you something 
far more valuable - honor.

The Shadow Guardian, impressed by your bravery and refusal to yield, 
spares your life and grants you safe passage. "You fought with honor," 
it declares. "That is rarer than victory."

Your courageous stand becomes legend. Though you did not win the day, 
you won something greater - the respect of your foe and the knowledge 
that you faced your fears without flinching.

Sometimes the greatest victory is simply refusing to surrender your 
principles, even in defeat. You have proven that true heroes are 
defined not by their victories, but by their character.

🎖️ ACHIEVEMENT UNLOCKED: THE HONORABLE FALLEN 🎖️
"It is better to fail with honor than to succeed without it."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("HONORABLE WARRIOR")
        
    def peaceful_path_ending(self):
        """Ending for choosing peaceful paths throughout."""
        self.game.ascii_art.display_peaceful_ending()
        
        ending_text = f"""
🌅 THE PATH OF INNER PEACE 🌅

{self.game.player_name}, your journey has taught you the greatest 
lesson of all - that true strength comes from inner peace and 
understanding. By choosing harmony over conflict, you have found 
a different kind of victory.

Your peaceful approach transforms not just yourself, but the entire 
realm. Conflicts that have raged for centuries are resolved through 
your example of compassion and understanding.

You become known as the Peacekeeper, one who can calm storms with 
a word and heal wounds with a touch. Your presence brings tranquility 
wherever you go.

The realm enters an age of unprecedented peace and prosperity. Your 
legacy is one of harmony, showing that the greatest adventures 
sometimes lead not to battle, but to understanding.

☮️ ACHIEVEMENT UNLOCKED: THE PEACEKEEPER ☮️
"The greatest victory is the battle not fought."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("KEEPER OF PEACE")
        
    def restful_ending(self):
        """Ending for choosing rest and meditation."""
        self.game.ascii_art.display_peaceful_ending()
        
        ending_text = f"""
🧘 THE CONTEMPLATIVE SAGE 🧘

{self.game.player_name}, your choice to rest and meditate by the sacred 
spring has led to the most profound adventure of all - the journey 
within. Through quiet contemplation, you have discovered truths that 
no amount of action could reveal.

Your meditation attracts other seekers of wisdom, and the sacred 
spring becomes a place of pilgrimage. You become a teacher of the 
inner path, showing others how to find peace within themselves.

The realm benefits from your wisdom as conflicts are resolved through 
understanding rather than force. Your example shows that sometimes 
the greatest action is stillness, the greatest journey is inward.

You have achieved something rarer than victory - you have found 
contentment. Your peaceful presence becomes a blessing to all 
who encounter it.

🧘 ACHIEVEMENT UNLOCKED: THE CONTEMPLATIVE SAGE 🧘
"In stillness, all answers are found."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("CONTEMPLATIVE SAGE")
        
    def default_ending(self):
        """Default ending for unexpected outcomes."""
        self.game.ascii_art.display_victory()
        
        ending_text = f"""
🌟 THE UNIQUE PATH 🌟

{self.game.player_name}, your journey has taken an unexpected path, 
and your unique choices have led to an outcome unlike any other. 
You have carved your own destiny in the ancient realm.

Your individual approach to the challenges you faced has created 
new possibilities that no one had imagined before. You have shown 
that there are as many paths to success as there are travelers 
willing to walk them.

The realm is enriched by your unique perspective and unconventional 
solutions. You have proven that sometimes the best answer is the 
one no one else has thought of.

Your legacy is one of innovation and individual courage - a reminder 
that every person's journey is unique and valuable.

🌟 ACHIEVEMENT UNLOCKED: THE PATHFINDER 🌟
"The best path is often the one you make yourself."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("UNIQUE PATHFINDER")
        
    def display_final_stats(self, title):
        """Display final game statistics and player achievements."""
        print()
        self.game.print_border('=', 60)
        print(f"                    FINAL STATISTICS")
        self.game.print_border('=', 60)
        print()
        print(f"Hero Name: {self.game.player_name}")
        print(f"Final Title: {title}")
        print(f"Health: {self.game.player_health}/100")
        print(f"Items Collected: {len(self.game.player_inventory)}")
        
        if self.game.player_inventory:
            print("\nInventory:")
            for item in self.game.player_inventory:
                print(f"  • {item}")
                
        print(f"\nSpecial Achievements:")
        achievement_count = 0
        
        # Check for various achievements
        if self.game.game_state.get("has_fairy_blessing"):
            print("  ✨ Blessed by the Fairies")
            achievement_count += 1
        if self.game.game_state.get("passed_wolf_trial"):
            print("  🐺 Passed the Wolf's Trial")
            achievement_count += 1
        if self.game.game_state.get("crystal_power"):
            print("  💎 Mastered Crystal Power")
            achievement_count += 1
        if self.game.game_state.get("knows_guardian_history"):
            print("  📚 Learned Ancient History")
            achievement_count += 1
        if self.game.game_state.get("inner_peace"):
            print("  🧘 Achieved Inner Peace")
            achievement_count += 1
        if self.game.game_state.get("treasure_master"):
            print("  🧩 Master of Ancient Riddles")
            achievement_count += 1
        if self.game.game_state.get("found_secret_garden"):
            print("  🌸 Discovered the Secret Garden")
            achievement_count += 1
        if self.game.game_state.get("infinite_wisdom"):
            print("  🔮 Gained Infinite Wisdom")
            achievement_count += 1
        if self.game.game_state.get("has_destiny_compass"):
            print("  🧭 Bearer of the Destiny Compass")
            achievement_count += 1
        if self.game.game_state.get("knows_complete_history"):
            print("  📖 Scholar of Ancient Lore")
            achievement_count += 1
            
        if achievement_count == 0:
            print("  🌟 Forged Your Own Path")
            
        print(f"\nTotal Achievements: {achievement_count + 1}")
        print()
        self.game.print_border('=', 60)
        print("Thank you for playing MYSTIC QUEST!")
        print("Your adventure will be remembered...")
        self.game.print_border('=', 60)
        
    def treasure_master_ending(self):
        """Ending for mastering the treasure room riddles."""
        self.game.ascii_art.display_riddle_master()
        
        ending_text = f"""
🧩 THE RIDDLE MASTER'S TRIUMPH 🧩

{self.game.player_name}, your intellectual prowess has earned you the 
greatest treasure of all - the mastery of ancient wisdom! By solving 
all three riddles in the Hidden Treasure Chamber, you have proven 
yourself worthy of the realm's most guarded secrets.

The Orb of Infinite Wisdom now pulses with your heartbeat, granting 
you understanding beyond mortal comprehension. The Master Key opens 
not just physical doors, but pathways to knowledge that have been 
sealed for millennia.

Your victory in the treasure chamber has transformed you into a living 
legend. Scholars and adventurers from across the realm seek you out, 
hoping to learn from your wisdom. You have become the keeper of the 
ancient mysteries, a bridge between the past and the future.

The realm prospers under your guidance, as you use your vast knowledge 
to solve problems that have plagued the land for generations. Your 
legacy is one of enlightenment, showing that the greatest treasures 
are not gold or gems, but wisdom and understanding.

🏆 ACHIEVEMENT UNLOCKED: THE RIDDLE MASTER 🏆
"True wealth lies in the treasures of the mind."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("MASTER OF ANCIENT RIDDLES")
        
    def secret_garden_ending(self):
        """Ending for discovering the secret garden."""
        self.game.ascii_art.display_secret_garden()
        
        ending_text = f"""
🌸 THE GARDEN KEEPER'S PEACE 🌸

{self.game.player_name}, your discovery of the Secret Underground Garden 
has led you to a destiny of tranquility and natural harmony. The crystal 
spring's waters have not only healed your body but transformed your very 
essence into something more connected to the natural world.

You become the Garden's eternal keeper, tending to the luminescent flowers 
and ensuring that this sanctuary of peace remains protected for future 
generations. The garden responds to your care by blooming even more 
magnificently, creating new species of magical plants.

Travelers who are pure of heart occasionally stumble upon the garden, 
and you welcome them with the same crystal spring water that transformed 
you. Each visitor leaves renewed and enlightened, carrying a piece of 
the garden's peace into the wider world.

Your legacy is one of quiet beauty and profound peace. While others 
seek glory in battle or treasure in gold, you have found the greatest 
treasure of all - a life lived in perfect harmony with nature.

🌺 ACHIEVEMENT UNLOCKED: THE GARDEN KEEPER 🌺
"In tending to beauty, we become beautiful ourselves."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("KEEPER OF THE SECRET GARDEN")
        
    def ancient_knowledge_ending(self):
        """Ending for gaining ancient knowledge from murals."""
        ending_text = f"""
📚 THE SCHOLAR'S ENLIGHTENMENT 📚

{self.game.player_name}, your dedication to understanding the ancient 
murals has granted you knowledge that transforms not just yourself, 
but the entire realm. The complete history you've uncovered reveals 
truths that rewrite the understanding of this mystical land.

Armed with the knowledge of secret paths and ancient prophecies, you 
become the realm's greatest explorer and historian. You discover lost 
cities, forgotten temples, and hidden civilizations that have been 
waiting centuries for someone with your insight to find them.

The protection spells you learned from the murals allow you to safeguard 
these discoveries, ensuring that the knowledge is preserved for future 
generations. You establish the Great Library of Mysteries, where all 
the realm's secrets are catalogued and protected.

Your understanding of the prophecy reveals that you were indeed the 
chosen hero foretold in ancient times - not a hero of sword and battle, 
but a hero of mind and wisdom. Your legacy is the preservation and 
sharing of knowledge that enriches all who seek understanding.

📖 ACHIEVEMENT UNLOCKED: THE ANCIENT SCHOLAR 📖
"Knowledge preserved is wisdom shared across the ages."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("KEEPER OF ANCIENT KNOWLEDGE")
        
    def wise_restraint_ending(self):
        """Ending for showing restraint with the treasure chamber."""
        ending_text = f"""
🧭 THE COMPASS OF DESTINY 🧭

{self.game.player_name}, your wisdom in showing restraint when faced 
with the treasure chamber's temptations has earned you something far 
more valuable than gold or gems - the Destiny Compass that guides you 
toward your true purpose in life.

The compass leads you on a journey of service and discovery, always 
pointing toward where you're needed most. You become a wandering helper, 
appearing at just the right moment to aid those in need, solve disputes, 
and bring hope to the hopeless.

Your reputation as the "Compass Bearer" spreads throughout the realm. 
People speak in whispers of the mysterious figure who appears when all 
seems lost, offers exactly the help that's needed, and then disappears 
to help others elsewhere.

The compass never leads you astray, for it points not to what you want, 
but to what the world needs from you. Your legacy is one of selfless 
service, showing that true heroism lies not in seeking glory, but in 
following the path of greatest good.

🧭 ACHIEVEMENT UNLOCKED: THE DESTINY WALKER 🧭
"The greatest treasure is knowing your true purpose."
        """
        
        self.game.print_with_delay(ending_text, 0.02)
        self.display_final_stats("BEARER OF THE DESTINY COMPASS")
