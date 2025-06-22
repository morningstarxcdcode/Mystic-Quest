"""
Time Nexus Scene for Mystic Quest
=================================
A unique scene where players can experience different time periods and make
choices that affect the past, present, and future.
"""

import random
import time


class TimeNexusScene:
    """The time nexus scene with temporal mechanics."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        self.temporal_energy = 100
        
    def play(self):
        """Play the time nexus scene."""
        self.game.clear_screen()
        
        # Display time nexus ASCII art
        self.display_nexus_art()
        
        print()
        self.game.print_border('-', 60)
        
        # Story introduction
        story_text = f"""
{self.game.player_name}, you stumble upon a swirling vortex of temporal 
energy. The air shimmers with chronological distortions, and you can see 
glimpses of different time periods flickering in and out of existence.

Ancient runes circle the nexus, pulsing with power that seems to bend 
reality itself. You feel the weight of infinite possibilities pressing 
against your consciousness.

A ethereal voice whispers: "Mortal, you have found the Time Nexus. Here, 
past, present, and future converge. Choose wisely, for your actions will 
ripple through the streams of time itself."
        """
        
        self.game.print_with_delay(story_text, 0.02)
        
        print()
        self.game.print_border('-', 60)
        print()
        
        # Present temporal choices
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                  THE TIME NEXUS                         │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│                                                         │")
        print("│  1. ⏪ Journey to the Ancient Past                      │")
        print("│     (Visit the age of dragons and first magic)          │")
        print("│                                                         │")
        print("│  2. ⏩ Glimpse the Distant Future                       │")
        print("│     (See what your world might become)                  │")
        print("│                                                         │")
        print("│  3. 🔄 Alter a Moment in Recent History                │")
        print("│     (Change something from your own past)               │")
        print("│                                                         │")
        print("│  4. ⚡ Absorb Temporal Energy                           │")
        print("│     (Gain power but risk temporal instability)          │")
        print("│                                                         │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        # Get player choice
        while True:
            try:
                choice = input(f"{self.game.player_name}, what temporal path do you choose? (1-4): ").strip()
                
                if choice == '1':
                    return self.journey_to_past()
                elif choice == '2':
                    return self.glimpse_future()
                elif choice == '3':
                    return self.alter_history()
                elif choice == '4':
                    return self.absorb_temporal_energy()
                else:
                    print("Please enter 1, 2, 3, or 4 to make your temporal choice.")
                    
            except (ValueError, KeyboardInterrupt):
                print("Please enter a valid choice (1, 2, 3, or 4).")
                continue
                
    def display_nexus_art(self):
        """Display ASCII art for the time nexus."""
        nexus_art = """
    ⏰ THE TIME NEXUS ⏰
    
        ╭─────────────────────╮
        │  ⏪ PAST    FUTURE ⏩ │
        │        ╱   ╲        │
        │       ╱  ⚡  ╲       │
        │      ╱   🌀   ╲      │
        │     ╱  NEXUS   ╲     │
        │    ╱_____🔄_____╲    │
        │                     │
        │   ✨ Time Flows ✨   │
        ╰─────────────────────╯
        
    Reality bends around you...
        """
        print(nexus_art)
        
    def journey_to_past(self):
        """Journey to the ancient past."""
        self.game.clear_screen()
        
        print("⏪ The nexus swirls, pulling you backward through time...")
        time.sleep(2)
        
        print("\n🐉 You emerge in the Age of Dragons!")
        print("The world is young, magic flows freely, and mighty dragons")
        print("soar through crystal-clear skies. Ancient civilizations")
        print("are just beginning to harness the primal forces of creation.")
        
        time.sleep(2)
        
        # Ancient encounter
        encounter = random.choice([
            "dragon_meeting",
            "first_mage",
            "primordial_magic",
            "ancient_artifact"
        ])
        
        if encounter == "dragon_meeting":
            return self.meet_ancient_dragon()
        elif encounter == "first_mage":
            return self.meet_first_mage()
        elif encounter == "primordial_magic":
            return self.experience_primordial_magic()
        else:
            return self.discover_ancient_artifact()
            
    def meet_ancient_dragon(self):
        """Meet an ancient dragon in the past."""
        print("\n🐉 A magnificent ancient dragon descends from the sky!")
        print("Its scales shimmer with all the colors of creation.")
        
        dragon_dialogue = f"""
The dragon's voice resonates like thunder and music combined:

"Young one from the future time, I sense the temporal winds upon you. 
You carry the scent of ages yet to come. I am Chronowyrm, first of 
the Time Dragons.

Your presence here creates ripples. I offer you a choice that will 
echo through the centuries."
        """
        
        self.game.print_with_delay(dragon_dialogue, 0.03)
        print()
        
        print("┌─────────────────────────────────────────────────────────┐")
        print("│  The Ancient Dragon offers you a temporal gift:         │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Dragon's Blessing - Permanent stat increases        │")
        print("│  2. Temporal Knowledge - Learn all time-based spells    │")
        print("│  3. Future Warning - Knowledge of coming dangers        │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        choice = input("Your choice (1-3): ").strip()
        
        if choice == '1':
            # Massive stat boost
            stats = self.game.systems.stats_system.player_stats
            stats["strength"] += 10
            stats["intelligence"] += 10
            stats["agility"] += 10
            stats["luck"] += 10
            stats["max_health"] += 50
            stats["max_mana"] += 30
            stats["health"] = stats["max_health"]
            stats["mana"] = stats["max_mana"]
            
            print("\n🐉 The dragon breathes ancient power into your soul!")
            print("💪 All your abilities are permanently enhanced!")
            print("❤️ Your vitality increases dramatically!")
            
        elif choice == '2':
            # Learn time spells
            time_spells = ["teleport", "insight"]
            for spell in time_spells:
                spell_msg = self.game.systems.magic_system.learn_spell(spell)
                print(f"\n✨ {spell_msg}")
                
            # Add unique temporal spell
            self.game.systems.magic_system.spell_database["time_stop"] = {
                "name": "Time Stop", "cost": 25, "effect": "temporal_freeze", 
                "description": "Briefly stop time around you"
            }
            spell_msg = self.game.systems.magic_system.learn_spell("time_stop")
            print(f"⏰ {spell_msg}")
            
        else:
            # Future knowledge
            print("\n🔮 The dragon shares visions of potential futures...")
            print("You gain insight into the challenges ahead!")
            
            # Massive experience boost
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(500)
            print(f"⭐ {exp_msg}")
            
            # Boost luck significantly
            self.game.systems.stats_system.player_stats["luck"] += 15
            print("🍀 Your luck increases dramatically from future knowledge!")
            
        # Dragon scale gift
        success, item_msg = self.game.systems.inventory_system.add_item("dragon_scale")
        if success:
            print(f"\n🐉 {item_msg}")
            print("This scale will protect you from the greatest dangers!")
            
        input("\nPress Enter to return to your time...")
        return "dragon_blessed"
        
    def meet_first_mage(self):
        """Meet the first mage in history."""
        print("\n🧙‍♂️ You encounter the First Mage, discoverer of magic itself!")
        print("They are experimenting with raw magical forces.")
        
        mage_dialogue = """
The First Mage looks up from their primitive spell components:

"Fascinating! You radiate magical energy I've never seen before. 
Your techniques... they're so refined! You must be from a time 
when magic has evolved far beyond my simple discoveries.

Would you help me perfect this spell? Your knowledge could 
accelerate magical development by centuries!"
        """
        
        self.game.print_with_delay(mage_dialogue, 0.03)
        print()
        
        print("┌─────────────────────────────────────────────────────────┐")
        print("│  Help shape the development of magic itself:            │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Share advanced magical knowledge                    │")
        print("│  2. Teach them about magical ethics and responsibility  │")
        print("│  3. Learn their primitive but pure magical techniques   │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        choice = input("Your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n🧙‍♂️ You share advanced magical techniques!")
            print("The First Mage's eyes light up with understanding.")
            print("Magic itself evolves before your eyes!")
            
            # Learn all spells
            for spell_id in self.game.systems.magic_system.spell_database:
                if spell_id not in self.game.systems.magic_system.known_spells:
                    self.game.systems.magic_system.learn_spell(spell_id)
                    
            print("✨ You now know all forms of magic!")
            
            # Boost intelligence massively
            self.game.systems.stats_system.player_stats["intelligence"] += 20
            print("🧠 Your intelligence increases by 20!")
            
        elif choice == '2':
            print("\n🧙‍♂️ You teach the importance of using magic responsibly.")
            print("The First Mage nods gravely, understanding the weight of power.")
            print("You've helped ensure magic will be used for good!")
            
            # Unlock peacemaker achievement
            achievement_msg = self.game.systems.achievement_system.unlock_achievement("peacemaker")
            if achievement_msg:
                print(f"\n{achievement_msg}")
                
            # Boost wisdom and experience
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(300)
            print(f"\n⭐ {exp_msg}")
            
            achievement_msg = self.game.systems.achievement_system.unlock_achievement("wise_one")
            if achievement_msg:
                print(f"\n{achievement_msg}")
                
        else:
            print("\n🧙‍♂️ You learn the pure, unrefined techniques of early magic.")
            print("Sometimes the simplest approaches are the most powerful!")
            
            # Increase mana efficiency
            stats = self.game.systems.stats_system.player_stats
            stats["max_mana"] += 50
            stats["mana"] = stats["max_mana"]
            print("💙 Your mana capacity increases by 50!")
            
            # Add primitive but powerful spell
            self.game.systems.magic_system.spell_database["primal_force"] = {
                "name": "Primal Force", "cost": 5, "effect": "raw_magic", 
                "description": "Channel raw magical energy"
            }
            spell_msg = self.game.systems.magic_system.learn_spell("primal_force")
            print(f"⚡ {spell_msg}")
            
        input("\nPress Enter to return to your time...")
        return "first_mage_met"
        
    def glimpse_future(self):
        """Glimpse the distant future."""
        self.game.clear_screen()
        
        print("⏩ The nexus propels you forward through time...")
        time.sleep(2)
        
        print("\n🌟 You witness a possible future!")
        
        # Random future scenarios
        future_scenario = random.choice([
            "utopian_future",
            "magical_renaissance", 
            "cosmic_adventure",
            "transcendent_beings"
        ])
        
        if future_scenario == "utopian_future":
            print("\n🏙️ You see a world where magic and technology exist in harmony.")
            print("Cities float in the sky, powered by crystallized magic.")
            print("All beings live in peace, their needs met by abundant energy.")
            
            print("\nA future version of yourself approaches:")
            print("'You made the right choices. Your actions led to this golden age.'")
            
            # Boost all stats moderately
            stats = self.game.systems.stats_system.player_stats
            for stat in ["strength", "intelligence", "agility", "luck"]:
                stats[stat] += 5
            print("\n🌟 Seeing your positive future impact empowers you!")
            print("All abilities increase by 5!")
            
        elif future_scenario == "magical_renaissance":
            print("\n🎨 You witness a magical renaissance!")
            print("Art, music, and magic have merged into incredible new forms.")
            print("Spell-painters create living masterpieces that dance through the air.")
            
            print("\nA master spell-artist shows you their techniques:")
            
            # Learn artistic magic
            self.game.systems.magic_system.spell_database["artistic_magic"] = {
                "name": "Artistic Magic", "cost": 15, "effect": "creative_power", 
                "description": "Channel magic through artistic expression"
            }
            spell_msg = self.game.systems.magic_system.learn_spell("artistic_magic")
            print(f"🎨 {spell_msg}")
            
            # Boost intelligence and luck
            stats = self.game.systems.stats_system.player_stats
            stats["intelligence"] += 8
            stats["luck"] += 7
            print("🧠 Your creativity and intuition are enhanced!")
            
        elif future_scenario == "cosmic_adventure":
            print("\n🚀 You see yourself traveling between worlds!")
            print("Magic has evolved to allow interdimensional travel.")
            print("You witness yourself as a legendary cosmic adventurer!")
            
            print("\nYour future self gives you a cosmic artifact:")
            
            # Add cosmic items
            success, item_msg = self.game.systems.inventory_system.add_item("shadow_gem")
            if success:
                print(f"🌌 {item_msg}")
                
            # Learn teleportation
            spell_msg = self.game.systems.magic_system.learn_spell("teleport")
            print(f"🌟 {spell_msg}")
            
            # Massive experience boost
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(400)
            print(f"⭐ {exp_msg}")
            
        else:  # transcendent_beings
            print("\n✨ You witness the ultimate evolution of consciousness!")
            print("Beings of pure energy and thought exist in perfect harmony.")
            print("Physical limitations have been transcended through magic and wisdom.")
            
            print("\nA transcendent being shares ultimate knowledge with you:")
            
            # Massive intelligence boost
            stats = self.game.systems.stats_system.player_stats
            stats["intelligence"] += 25
            stats["max_mana"] += 100
            stats["mana"] = stats["max_mana"]
            print("🧠 Your mind expands beyond mortal limitations!")
            print("💙 Your magical capacity becomes extraordinary!")
            
            # Learn all spells
            for spell_id in self.game.systems.magic_system.spell_database:
                if spell_id not in self.game.systems.magic_system.known_spells:
                    self.game.systems.magic_system.learn_spell(spell_id)
            print("✨ You understand all forms of magic!")
            
        input("\nPress Enter to return to your time...")
        return "future_glimpsed"
        
    def alter_history(self):
        """Alter a moment in recent history."""
        self.game.clear_screen()
        
        print("🔄 You focus on a moment from your own past...")
        time.sleep(2)
        
        print("\nYou can change one decision from your adventure so far.")
        print("This will create a temporal paradox, but the nexus will stabilize it.")
        
        # Offer to undo a negative outcome or enhance a positive one
        print("\n┌─────────────────────────────────────────────────────────┐")
        print("│  What would you like to alter?                          │")
        print("├─────────────────────────────────────────────────────────┤")
        print("│  1. Prevent a past injury (Restore health)              │")
        print("│  2. Make a better first impression (Boost charisma)     │")
        print("│  3. Study harder in the past (Gain extra experience)    │")
        print("│  4. Be more careful with resources (Restore items)      │")
        print("└─────────────────────────────────────────────────────────┘")
        print()
        
        choice = input("Your alteration (1-4): ").strip()
        
        if choice == '1':
            # Full heal
            stats = self.game.systems.stats_system.player_stats
            stats["health"] = stats["max_health"]
            stats["max_health"] += 25  # Bonus for temporal manipulation
            print("\n⏰ You prevent past injuries from ever happening!")
            print("❤️ Your health is fully restored and permanently increased!")
            
        elif choice == '2':
            # Social benefits
            stats = self.game.systems.stats_system.player_stats
            stats["luck"] += 10
            print("\n⏰ You make better first impressions in the past!")
            print("🍀 Your luck increases by 10!")
            
            # Chance to recruit a companion retroactively
            if len(self.game.systems.companion_system.companions) < 2:
                companion_msg = self.game.systems.companion_system.recruit_companion("fairy_guide")
                print(f"🧚‍♀️ {companion_msg}")
                print("A fairy you befriended in the altered past joins you!")
                
        elif choice == '3':
            # Experience boost
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(200)
            print("\n⏰ You study more diligently in the past!")
            print(f"⭐ {exp_msg}")
            
            # Learn an extra spell
            available_spells = ["shield", "insight", "fireball"]
            for spell in available_spells:
                if spell not in self.game.systems.magic_system.known_spells:
                    spell_msg = self.game.systems.magic_system.learn_spell(spell)
                    print(f"✨ {spell_msg}")
                    break
                    
        else:
            # Restore items
            print("\n⏰ You're more careful with your resources in the past!")
            
            # Add useful items
            items_to_add = ["healing_potion", "magic_crystal", "fairy_dust"]
            for item in items_to_add:
                success, item_msg = self.game.systems.inventory_system.add_item(item)
                if success:
                    print(f"📦 {item_msg}")
                    
        # Temporal energy cost
        print("\n⚡ The temporal alteration drains some of your life force...")
        stats = self.game.systems.stats_system.player_stats
        stats["health"] -= 10
        print("❤️ You lose 10 health from temporal strain.")
        
        # But gain temporal resistance
        stats["max_mana"] += 20
        stats["mana"] = min(stats["max_mana"], stats["mana"] + 20)
        print("💙 But you gain temporal resistance! +20 max mana!")
        
        input("\nPress Enter to stabilize the timeline...")
        return "history_altered"
        
    def absorb_temporal_energy(self):
        """Absorb raw temporal energy."""
        self.game.clear_screen()
        
        print("⚡ You reach out to absorb the raw temporal energy...")
        print("The power is intoxicating but dangerous!")
        time.sleep(2)
        
        # Risk/reward scenario
        luck = self.game.systems.stats_system.player_stats["luck"]
        success_chance = min(0.8, 0.3 + (luck * 0.02))
        
        if random.random() < success_chance:
            print("\n✨ You successfully channel the temporal energy!")
            print("Power beyond imagination flows through you!")
            
            # Massive benefits
            stats = self.game.systems.stats_system.player_stats
            stats["max_health"] += 50
            stats["max_mana"] += 75
            stats["health"] = stats["max_health"]
            stats["mana"] = stats["max_mana"]
            
            for stat in ["strength", "intelligence", "agility", "luck"]:
                stats[stat] += 8
                
            print("🌟 All your abilities are dramatically enhanced!")
            
            # Learn temporal magic
            self.game.systems.magic_system.spell_database["temporal_mastery"] = {
                "name": "Temporal Mastery", "cost": 30, "effect": "time_control", 
                "description": "Master the flow of time itself"
            }
            spell_msg = self.game.systems.magic_system.learn_spell("temporal_mastery")
            print(f"⏰ {spell_msg}")
            
            # Massive experience
            leveled_up, exp_msg = self.game.systems.stats_system.gain_experience(1000)
            print(f"⭐ {exp_msg}")
            
        else:
            print("\n💥 The temporal energy overwhelms you!")
            print("Reality fractures around you as time becomes unstable!")
            
            # Negative effects but some compensation
            stats = self.game.systems.stats_system.player_stats
            stats["health"] -= 30
            print("❤️ You lose 30 health from temporal backlash!")
            
            # But gain some benefits
            stats["max_mana"] += 25
            stats["intelligence"] += 5
            print("💙 But your magical capacity increases from exposure!")
            print("🧠 Your understanding of time grants +5 Intelligence!")
            
            # Learn a basic temporal spell
            spell_msg = self.game.systems.magic_system.learn_spell("insight")
            print(f"✨ {spell_msg}")
            
        input("\nPress Enter to leave the unstable nexus...")
        return "temporal_energy_absorbed"
