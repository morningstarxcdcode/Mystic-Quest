"""
Adventurer Crossroads Scene for Mystic Quest
===========================================
A unique scene where players encounter echoes of other adventurers and can
interact with their stories, learn from their experiences, and even compete
in challenges.
"""

import random
import time


class AdventurerCrossroadsScene:
    """The crossroads where adventurers' paths intersect across time and space."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        self.other_adventurers = [
            {
                "name": "Lyra the Spellweaver",
                "class": "Mage",
                "level": random.randint(3, 8),
                "specialty": "Elemental Magic",
                "story": "A master of fire and ice who seeks to balance opposing forces",
                "challenge": "magical_duel",
                "reward_type": "spell"
            },
            {
                "name": "Thorne Ironshield",
                "class": "Warrior",
                "level": random.randint(4, 9),
                "specialty": "Combat Mastery",
                "story": "A veteran warrior who has faced countless battles",
                "challenge": "combat_trial",
                "reward_type": "strength"
            },
            {
                "name": "Whisper Shadowstep",
                "class": "Rogue",
                "level": random.randint(2, 7),
                "specialty": "Stealth & Agility",
                "story": "A mysterious figure who moves like smoke through shadows",
                "challenge": "stealth_test",
                "reward_type": "agility"
            },
            {
                "name": "Sage Moonwhisper",
                "class": "Scholar",
                "level": random.randint(5, 10),
                "specialty": "Ancient Knowledge",
                "story": "A keeper of forgotten lore and ancient wisdom",
                "challenge": "wisdom_trial",
                "reward_type": "intelligence"
            },
            {
                "name": "Lucky Goldleaf",
                "class": "Treasure Hunter",
                "level": random.randint(3, 6),
                "specialty": "Fortune & Discovery",
                "story": "An adventurer blessed by fortune who finds treasure everywhere",
                "challenge": "treasure_hunt",
                "reward_type": "luck"
            }
        ]
        
    def play(self):
        """Play the adventurer crossroads scene."""
        self.game.clear_screen()
        
        # Display crossroads ASCII art
        self.display_crossroads_art()
        
        print()
        self.game.print_border('-', 60)
        
        # Story introduction
        story_text = f"""
{self.game.player_name}, you arrive at a mystical crossroads where the 
paths of many adventurers converge. Ethereal campfires flicker with 
spectral flames, and you can see the ghostly echoes of other heroes 
who have passed this way.

This is the Adventurer's Crossroads - a place between worlds where 
the stories of all heroes intersect. Here, you can learn from the 
experiences of others, test your skills, and forge connections that 
transcend time and space.

The air hums with the collective energy of countless adventures, and 
you feel the presence of kindred spirits who share your quest for 
glory and discovery.
        """
        
        self.game.print_with_delay(story_text, 0.02)
        
        print()
        self.game.print_border('-', 60)
        print()
        
        # Select random adventurers to encounter
        available_adventurers = random.sample(self.other_adventurers, 3)
        
        # Present choices
        print("┌─────────────────────────────────────────────────────────┐")
        print("│              ADVENTURER'S CROSSROADS                    │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print(f"│  1. 🗣️  Approach {available_adventurers[0]['name']:<25}      │")
        print(f"│     ({available_adventurers[0]['class']} - {available_adventurers[0]['specialty']})                    │")
        print("│                                                         │")
        print(f"│  2. 🤝 Approach {available_adventurers[1]['name']:<25}      │")
        print(f"│     ({available_adventurers[1]['class']} - {available_adventurers[1]['specialty']})                 │")
        print("│                                                         │")
        print(f"│  3. ⚔️  Challenge {available_adventurers[2]['name']:<23}      │")
        print(f"│     ({available_adventurers[2]['class']} - {available_adventurers[2]['specialty']})                │")
        print("│                                                         │")
        print("│  4. 🔮 Commune with the Crossroads Spirit               │")
        print("│     (Gain insight from all adventurers' experiences)    │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        # Get player choice
        while True:
            try:
                choice = input(f"{self.game.player_name}, who do you approach? (1-4): ").strip()
                
                if choice == '1':
                    return self.interact_with_adventurer(available_adventurers[0], "friendly")
                elif choice == '2':
                    return self.interact_with_adventurer(available_adventurers[1], "collaborative")
                elif choice == '3':
                    return self.interact_with_adventurer(available_adventurers[2], "challenge")
                elif choice == '4':
                    return self.commune_with_spirit()
                else:
                    print("Please enter 1, 2, 3, or 4 to make your choice.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, 3, or 4).")
                continue
                
    def display_crossroads_art(self):
        """Display ASCII art for the adventurer crossroads."""
        crossroads_art = """
    🗡️ ADVENTURER'S CROSSROADS ⚔️
    
        ╭─────────────────────────╮
        │    👥 Heroes Gather 👥   │
        │                         │
        │  🔥    🗡️    🏹    ✨   │
        │    ╲    │    │    ╱     │
        │     ╲   │    │   ╱      │
        │      ╲  │    │  ╱       │
        │       ╲ │    │ ╱        │
        │        ╲│    │╱         │
        │         ╲    ╱          │
        │          ╲  ╱           │
        │           ╲╱            │
        │        🌟 YOU 🌟        │
        ╰─────────────────────────╯
        
    Echoes of legendary heroes...
        """
        print(crossroads_art)
        
    def interact_with_adventurer(self, adventurer, interaction_type):
        """Interact with a specific adventurer."""
        self.game.clear_screen()
        
        print(f"👤 You approach {adventurer['name']}...")
        time.sleep(1)
        
        # Display adventurer info
        print(f"\n{adventurer['name']} - Level {adventurer['level']} {adventurer['class']}")
        print(f"Specialty: {adventurer['specialty']}")
        print(f"Story: {adventurer['story']}")
        print()
        
        if interaction_type == "friendly":
            return self.friendly_interaction(adventurer)
        elif interaction_type == "collaborative":
            return self.collaborative_interaction(adventurer)
        else:  # challenge
            return self.challenge_interaction(adventurer)
            
    def friendly_interaction(self, adventurer):
        """Have a friendly conversation with an adventurer."""
        print(f"🗣️ {adventurer['name']} greets you warmly:")
        
        # Generate dialogue based on adventurer type
        if adventurer['class'] == 'Mage':
            dialogue = f"""
"Ah, a fellow seeker of mysteries! I can sense the magical energy 
flowing through you. In my travels, I've learned that true power 
comes not from the strength of your spells, but from understanding 
the harmony between all magical forces.

Let me share some of my knowledge with you. Magic is like a river - 
it flows best when you don't try to force it, but guide it gently."
            """
        elif adventurer['class'] == 'Warrior':
            dialogue = f"""
"Well met, adventurer! I can see the determination in your eyes. 
In my years of battle, I've learned that true strength isn't just 
about swinging a sword harder - it's about knowing when to fight 
and when to show mercy.

Every scar tells a story, and every victory teaches humility. 
Let me share some hard-won wisdom with you."
            """
        elif adventurer['class'] == 'Rogue':
            dialogue = f"""
"*steps out of the shadows* Impressive... most people don't notice 
me until I want them to. You have good instincts. In my line of 
work, I've learned that the best treasure isn't always gold - 
sometimes it's information, sometimes it's knowing when to disappear.

The shadows have taught me patience. Let me show you what I've learned."
            """
        elif adventurer['class'] == 'Scholar':
            dialogue = f"""
"Greetings, seeker of truth! Your aura suggests a mind open to 
learning - how refreshing! In my studies of ancient texts and 
forgotten lore, I've discovered that knowledge is the only treasure 
that multiplies when shared.

Every question leads to ten more, and that's the beauty of wisdom. 
Allow me to share some insights from my research."
            """
        else:  # Treasure Hunter
            dialogue = f"""
"Hey there, fellow adventurer! *jingles a pouch of coins* You know 
what I've learned in all my treasure hunting? The real treasure 
isn't the gold you find - it's the adventures you have finding it!

Though I'll admit, the gold doesn't hurt either. *winks* Let me 
share some of my luckiest discoveries with you!"
            """
            
        self.game.print_with_delay(dialogue, 0.03)
        print()
        
        # Offer benefits based on adventurer type
        print("┌─────────────────────────────────────────────────────────┐")
        print(f"│  {adventurer['name']} offers to share their wisdom:     │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Learn from their experiences (Gain experience)      │")
        print("│  2. Ask for practical advice (Gain items)              │")
        print("│  3. Request training (Improve abilities)               │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        choice = input("Your choice (1-3): ").strip()
        
        if choice == '1':
            # Experience gain
            exp_amount = adventurer['level'] * 25
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(exp_amount)
            print(f"\n⭐ {exp_msg}")
            
            print(f"📚 {adventurer['name']} shares tales of their adventures!")
            print("You gain valuable experience from their stories.")
            
        elif choice == '2':
            # Item rewards
            if adventurer['class'] == 'Mage':
                items = ["magic_crystal", "wisdom_scroll"]
            elif adventurer['class'] == 'Warrior':
                items = ["healing_potion", "dragon_scale"]
            elif adventurer['class'] == 'Rogue':
                items = ["elven_cloak", "ancient_key"]
            elif adventurer['class'] == 'Scholar':
                items = ["wisdom_scroll", "fairy_dust"]
            else:  # Treasure Hunter
                items = ["healing_potion", "magic_crystal"]
                
            for item in items:
                success, item_msg = self.game.systems.inventory_system.add_item(item)
                if success:
                    print(f"\n🎁 {item_msg}")
                    
        else:
            # Stat improvement
            stats = self.game.systems.stats_system.player_stats
            
            if adventurer['class'] == 'Mage':
                stats['intelligence'] += 5
                stats['max_mana'] += 15
                print(f"\n🧠 {adventurer['name']} teaches you magical theory!")
                print("Intelligence +5, Max Mana +15!")
            elif adventurer['class'] == 'Warrior':
                stats['strength'] += 5
                stats['max_health'] += 20
                print(f"\n💪 {adventurer['name']} trains you in combat techniques!")
                print("Strength +5, Max Health +20!")
            elif adventurer['class'] == 'Rogue':
                stats['agility'] += 5
                stats['luck'] += 3
                print(f"\n🏃 {adventurer['name']} teaches you stealth and precision!")
                print("Agility +5, Luck +3!")
            elif adventurer['class'] == 'Scholar':
                stats['intelligence'] += 7
                print(f"\n📖 {adventurer['name']} expands your knowledge!")
                print("Intelligence +7!")
            else:  # Treasure Hunter
                stats['luck'] += 8
                print(f"\n🍀 {adventurer['name']} shares their fortune secrets!")
                print("Luck +8!")
                
        input("\nPress Enter to continue...")
        return f"befriended_{adventurer['class'].lower()}"
        
    def collaborative_interaction(self, adventurer):
        """Work together with an adventurer on a joint task."""
        print(f"🤝 {adventurer['name']} suggests working together:")
        
        collaboration_text = f"""
"I have an idea! There's a challenge here at the crossroads that's 
too difficult for one person alone. If we combine our skills, we 
could accomplish something truly remarkable.

What do you say we team up? Together, we can achieve more than 
either of us could alone!"
        """
        
        self.game.print_with_delay(collaboration_text, 0.03)
        print()
        
        # Joint challenge based on adventurer type
        if adventurer['class'] == 'Mage':
            return self.magical_collaboration(adventurer)
        elif adventurer['class'] == 'Warrior':
            return self.combat_collaboration(adventurer)
        elif adventurer['class'] == 'Rogue':
            return self.stealth_collaboration(adventurer)
        elif adventurer['class'] == 'Scholar':
            return self.research_collaboration(adventurer)
        else:  # Treasure Hunter
            return self.treasure_collaboration(adventurer)
            
    def magical_collaboration(self, adventurer):
        """Collaborate on a magical ritual."""
        print("✨ Together, you attempt to perform an ancient magical ritual!")
        print("Your combined magical energies create something extraordinary...")
        time.sleep(2)
        
        # Success based on intelligence
        intelligence = self.game.systems.stats_system.player_stats['intelligence']
        success_chance = min(0.9, 0.5 + (intelligence * 0.02))
        
        if random.random() < success_chance:
            print("\n🌟 SUCCESS! The ritual creates a powerful magical enhancement!")
            
            # Major magical benefits
            stats = self.game.systems.stats_system.player_stats
            stats['max_mana'] += 30
            stats['mana'] = stats['max_mana']
            stats['intelligence'] += 8
            
            print("💙 Your magical capacity increases dramatically!")
            print("🧠 Your understanding of magic deepens!")
            
            # Learn collaborative spell
            self.game.systems.magic_system.spell_database["harmony_spell"] = {
                "name": "Harmony Spell", "cost": 20, "effect": "group_enhancement", 
                "description": "A spell born from collaboration and unity"
            }
            spell_msg = self.game.systems.magic_system.learn_spell("harmony_spell")
            print(f"✨ {spell_msg}")
            
        else:
            print("\n💥 The ritual goes awry, but you learn from the experience!")
            
            # Partial benefits
            stats = self.game.systems.stats_system.player_stats
            stats['intelligence'] += 3
            stats['max_mana'] += 10
            
            print("🧠 You gain insight from the failed attempt!")
            print("💙 Your magical understanding still improves!")
            
        input("\nPress Enter to continue...")
        return "magical_collaboration"
        
    def challenge_interaction(self, adventurer):
        """Challenge an adventurer to a contest."""
        print(f"⚔️ You challenge {adventurer['name']} to a contest of skills!")
        
        challenge_text = f"""
{adventurer['name']} grins and accepts your challenge:

"Excellent! I respect someone who isn't afraid to test themselves. 
Let's see what you're made of! This will be a friendly competition - 
may the best adventurer win!"
        """
        
        self.game.print_with_delay(challenge_text, 0.03)
        print()
        
        # Challenge based on adventurer type
        if adventurer['challenge'] == 'magical_duel':
            return self.magical_duel(adventurer)
        elif adventurer['challenge'] == 'combat_trial':
            return self.combat_trial(adventurer)
        elif adventurer['challenge'] == 'stealth_test':
            return self.stealth_test(adventurer)
        elif adventurer['challenge'] == 'wisdom_trial':
            return self.wisdom_trial(adventurer)
        else:  # treasure_hunt
            return self.treasure_hunt_challenge(adventurer)
            
    def magical_duel(self, adventurer):
        """Engage in a magical duel."""
        print("✨ The magical duel begins!")
        print("Spells fly through the air as you test your magical prowess!")
        time.sleep(2)
        
        # Duel based on intelligence and mana
        player_power = (self.game.systems.stats_system.player_stats['intelligence'] + 
                       self.game.systems.stats_system.player_stats['mana'] // 5)
        opponent_power = adventurer['level'] * 8 + random.randint(10, 30)
        
        if player_power > opponent_power:
            print(f"\n🏆 Victory! You defeat {adventurer['name']} in magical combat!")
            
            # Victory rewards
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(150)
            print(f"⭐ {exp_msg}")
            
            # Learn opponent's signature spell
            signature_spells = ["fireball", "shield", "insight"]
            for spell in signature_spells:
                if spell not in self.game.systems.magic_system.known_spells:
                    spell_msg = self.game.systems.magic_system.learn_spell(spell)
                    print(f"✨ {spell_msg}")
                    break
                    
            # Stat boost
            self.game.systems.stats_system.player_stats['intelligence'] += 6
            print("🧠 Your magical abilities improve significantly!")
            
        else:
            print(f"\n⚔️ {adventurer['name']} proves to be a formidable opponent!")
            print("Though you don't win, you learn valuable lessons!")
            
            # Consolation rewards
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(75)
            print(f"⭐ {exp_msg}")
            
            self.game.systems.stats_system.player_stats['intelligence'] += 3
            print("🧠 You gain insight from the challenge!")
            
        input("\nPress Enter to continue...")
        return "magical_duel_completed"
        
    def commune_with_spirit(self):
        """Commune with the crossroads spirit."""
        self.game.clear_screen()
        
        print("🔮 You approach the center of the crossroads...")
        print("A mystical spirit materializes before you...")
        time.sleep(2)
        
        spirit_dialogue = f"""
The Crossroads Spirit speaks in a voice like wind through ancient trees:

"Welcome, {self.game.player_name}. I am the guardian of this sacred 
place where all adventurers' paths converge. I have witnessed countless 
heroes pass through these crossroads, each carrying their own dreams 
and destinies.

You seek wisdom from the collective experiences of all who have come 
before. Very well. I shall grant you insight drawn from the echoes 
of every adventurer who has ever stood where you stand now."
        """
        
        self.game.print_with_delay(spirit_dialogue, 0.03)
        print()
        
        print("✨ The spirit channels the wisdom of all adventurers...")
        time.sleep(2)
        
        # Massive benefits from collective wisdom
        stats = self.game.systems.stats_system.player_stats
        
        # Boost all stats
        for stat in ["strength", "intelligence", "agility", "luck"]:
            stats[stat] += 4
            
        # Health and mana boost
        stats['max_health'] += 25
        stats['max_mana'] += 25
        stats['health'] = stats['max_health']
        stats['mana'] = stats['max_mana']
        
        print("🌟 The collective wisdom of countless heroes flows through you!")
        print("All your abilities are enhanced by the shared experiences!")
        
        # Learn multiple spells
        all_spells = list(self.game.systems.magic_system.spell_database.keys())
        spells_learned = 0
        
        for spell_id in all_spells:
            if spell_id not in self.game.systems.magic_system.known_spells and spells_learned < 3:
                spell_msg = self.game.systems.magic_system.learn_spell(spell_id)
                print(f"✨ {spell_msg}")
                spells_learned += 1
                
        # Massive experience boost
        leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(300)
        print(f"⭐ {exp_msg}")
        
        # Add rare items
        rare_items = ["shadow_gem", "dragon_scale", "fairy_dust"]
        for item in rare_items:
            success, item_msg = self.game.systems.inventory_system.add_item(item)
            if success:
                print(f"🎁 {item_msg}")
                
        # Unlock multiple achievements
        achievements_to_unlock = ["explorer", "wise_one", "collector"]
        for achievement in achievements_to_unlock:
            achievement_msg = self.game.systems.achievement_system.unlock_achievement(achievement)
            if achievement_msg:
                print(f"\n{achievement_msg}")
                
        print("\n🔮 The spirit fades, leaving you transformed by the encounter...")
        
        input("\nPress Enter to continue...")
        return "spirit_communion"
