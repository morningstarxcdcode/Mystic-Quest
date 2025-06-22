"""
Enhanced Game Systems for Mystic Quest
=====================================
Advanced gameplay mechanics including inventory, stats, weather, and more.
"""

import random
import json
import os
from datetime import datetime


class GameSystems:
    """Advanced game systems for enhanced gameplay."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        self.weather_system = WeatherSystem()
        self.inventory_system = InventorySystem()
        self.stats_system = StatsSystem()
        self.achievement_system = AchievementSystem()
        self.random_events = RandomEventSystem()
        self.combat_system = CombatSystem()
        self.magic_system = MagicSystem()
        self.companion_system = CompanionSystem()
        self.time_system = TimeSystem()
        
    def initialize_player(self, name):
        """Initialize all player systems."""
        self.stats_system.initialize_player(name)
        self.inventory_system.initialize()
        self.magic_system.initialize()
        self.companion_system.initialize()
        self.time_system.initialize()


class WeatherSystem:
    """Dynamic weather system that affects gameplay."""
    
    def __init__(self):
        self.current_weather = "clear"
        self.weather_types = {
            "clear": {"description": "☀️ Clear skies", "effect": "normal"},
            "rainy": {"description": "🌧️ Light rain", "effect": "stealth_bonus"},
            "stormy": {"description": "⛈️ Thunderstorm", "effect": "magic_boost"},
            "foggy": {"description": "🌫️ Dense fog", "effect": "confusion"},
            "snowy": {"description": "❄️ Gentle snow", "effect": "cold_damage"},
            "mystical": {"description": "✨ Mystical aurora", "effect": "magic_regeneration"}
        }
        
    def change_weather(self):
        """Randomly change the weather."""
        self.current_weather = random.choice(list(self.weather_types.keys()))
        
    def get_weather_info(self):
        """Get current weather information."""
        weather = self.weather_types[self.current_weather]
        return f"{weather['description']} - {weather['effect'].replace('_', ' ').title()}"
        
    def get_weather_effect(self):
        """Get the current weather's gameplay effect."""
        return self.weather_types[self.current_weather]["effect"]


class InventorySystem:
    """Advanced inventory management system."""
    
    def __init__(self):
        self.items = {}
        self.max_capacity = 10
        self.item_database = {
            "healing_potion": {"name": "Healing Potion", "type": "consumable", "effect": "heal_50", "description": "Restores 50 health points"},
            "magic_crystal": {"name": "Magic Crystal", "type": "artifact", "effect": "mana_boost", "description": "Increases magical power"},
            "ancient_key": {"name": "Ancient Key", "type": "key", "effect": "unlock", "description": "Opens mysterious doors"},
            "elven_cloak": {"name": "Elven Cloak", "type": "equipment", "effect": "stealth_boost", "description": "Grants enhanced stealth abilities"},
            "dragon_scale": {"name": "Dragon Scale", "type": "material", "effect": "fire_resistance", "description": "Provides protection from fire"},
            "wisdom_scroll": {"name": "Wisdom Scroll", "type": "consumable", "effect": "experience_boost", "description": "Grants additional experience"},
            "fairy_dust": {"name": "Fairy Dust", "type": "material", "effect": "magic_enhancement", "description": "Enhances magical abilities"},
            "shadow_gem": {"name": "Shadow Gem", "type": "artifact", "effect": "dark_magic", "description": "Grants access to shadow magic"}
        }
        
    def initialize(self):
        """Initialize inventory with starting items."""
        self.add_item("healing_potion", 2)
        
    def add_item(self, item_id, quantity=1):
        """Add an item to inventory."""
        if len(self.items) >= self.max_capacity and item_id not in self.items:
            return False, "Inventory is full!"
            
        if item_id in self.items:
            self.items[item_id] += quantity
        else:
            self.items[item_id] = quantity
        return True, f"Added {quantity} {self.item_database[item_id]['name']}(s)"
        
    def remove_item(self, item_id, quantity=1):
        """Remove an item from inventory."""
        if item_id not in self.items or self.items[item_id] < quantity:
            return False, "Not enough items!"
            
        self.items[item_id] -= quantity
        if self.items[item_id] <= 0:
            del self.items[item_id]
        return True, f"Used {quantity} {self.item_database[item_id]['name']}(s)"
        
    def display_inventory(self):
        """Display current inventory."""
        if not self.items:
            return "Your inventory is empty."
            
        inventory_text = "📦 INVENTORY:\n"
        inventory_text += "=" * 40 + "\n"
        
        for item_id, quantity in self.items.items():
            item = self.item_database[item_id]
            inventory_text += f"• {item['name']} x{quantity}\n"
            inventory_text += f"  {item['description']}\n\n"
            
        return inventory_text


class StatsSystem:
    """Character progression and stats system."""
    
    def __init__(self):
        self.player_stats = {
            "name": "",
            "level": 1,
            "experience": 0,
            "health": 100,
            "max_health": 100,
            "mana": 50,
            "max_mana": 50,
            "strength": 10,
            "intelligence": 10,
            "agility": 10,
            "luck": 10
        }
        
    def initialize_player(self, name):
        """Initialize player stats."""
        self.player_stats["name"] = name
        
    def gain_experience(self, amount):
        """Gain experience and check for level up."""
        self.player_stats["experience"] += amount
        exp_needed = self.player_stats["level"] * 100
        
        if self.player_stats["experience"] >= exp_needed:
            return self.level_up()
        return False, f"Gained {amount} experience!"
        
    def level_up(self):
        """Level up the player."""
        self.player_stats["level"] += 1
        self.player_stats["max_health"] += 20
        self.player_stats["max_mana"] += 10
        self.player_stats["health"] = self.player_stats["max_health"]
        self.player_stats["mana"] = self.player_stats["max_mana"]
        
        # Random stat increase
        stat_to_increase = random.choice(["strength", "intelligence", "agility", "luck"])
        self.player_stats[stat_to_increase] += 2
        
        return True, f"🎉 LEVEL UP! You are now level {self.player_stats['level']}!\n{stat_to_increase.title()} increased by 2!"
        
    def display_stats(self):
        """Display player statistics."""
        stats = self.player_stats
        stats_text = f"""
🏆 CHARACTER STATS - {stats['name']}
{'=' * 40}
Level: {stats['level']} | Experience: {stats['experience']}/{stats['level'] * 100}
Health: {stats['health']}/{stats['max_health']} ❤️
Mana: {stats['mana']}/{stats['max_mana']} 💙

Strength: {stats['strength']} 💪 | Intelligence: {stats['intelligence']} 🧠
Agility: {stats['agility']} 🏃 | Luck: {stats['luck']} 🍀
"""
        return stats_text


class AchievementSystem:
    """Track and display player achievements."""
    
    def __init__(self):
        self.unlocked_achievements = set()
        self.achievements = {
            "first_steps": {"name": "First Steps", "description": "Begin your adventure", "icon": "👣"},
            "explorer": {"name": "Explorer", "description": "Visit 5 different locations", "icon": "🗺️"},
            "collector": {"name": "Collector", "description": "Collect 10 different items", "icon": "📦"},
            "level_master": {"name": "Level Master", "description": "Reach level 5", "icon": "⭐"},
            "spell_caster": {"name": "Spell Caster", "description": "Cast 10 spells", "icon": "🔮"},
            "beast_friend": {"name": "Beast Friend", "description": "Befriend a magical creature", "icon": "🐺"},
            "treasure_hunter": {"name": "Treasure Hunter", "description": "Find hidden treasure", "icon": "💎"},
            "wise_one": {"name": "Wise One", "description": "Make 5 wisdom-based choices", "icon": "🦉"},
            "warrior": {"name": "Warrior", "description": "Win 10 battles", "icon": "⚔️"},
            "peacemaker": {"name": "Peacemaker", "description": "Resolve conflicts peacefully", "icon": "🕊️"}
        }
        
    def unlock_achievement(self, achievement_id):
        """Unlock an achievement."""
        if achievement_id not in self.unlocked_achievements:
            self.unlocked_achievements.add(achievement_id)
            achievement = self.achievements[achievement_id]
            return f"🏆 ACHIEVEMENT UNLOCKED!\n{achievement['icon']} {achievement['name']}: {achievement['description']}"
        return None
        
    def display_achievements(self):
        """Display all achievements."""
        text = "🏆 ACHIEVEMENTS:\n" + "=" * 40 + "\n"
        
        for achievement_id, achievement in self.achievements.items():
            status = "✅" if achievement_id in self.unlocked_achievements else "❌"
            text += f"{status} {achievement['icon']} {achievement['name']}\n"
            text += f"   {achievement['description']}\n\n"
            
        return text


class RandomEventSystem:
    """System for random encounters and events."""
    
    def __init__(self):
        self.events = [
            {
                "name": "Mysterious Merchant",
                "description": "A hooded figure offers to trade rare items.",
                "type": "trade",
                "rarity": "uncommon"
            },
            {
                "name": "Shooting Star",
                "description": "A shooting star grants you a wish!",
                "type": "blessing",
                "rarity": "rare"
            },
            {
                "name": "Lost Traveler",
                "description": "A lost traveler asks for directions.",
                "type": "choice",
                "rarity": "common"
            },
            {
                "name": "Ancient Runes",
                "description": "You discover glowing runes on a stone.",
                "type": "magic",
                "rarity": "uncommon"
            },
            {
                "name": "Wild Magic Surge",
                "description": "The air crackles with unstable magic!",
                "type": "magic_chaos",
                "rarity": "rare"
            }
        ]
        
    def trigger_random_event(self):
        """Trigger a random event based on probability."""
        if random.random() < 0.3:  # 30% chance
            event = random.choice(self.events)
            return event
        return None


class CombatSystem:
    """Turn-based combat system."""
    
    def __init__(self):
        self.in_combat = False
        
    def start_combat(self, enemy):
        """Start a combat encounter."""
        self.in_combat = True
        return f"⚔️ Combat begins with {enemy['name']}!"
        
    def player_attack(self, player_stats, enemy):
        """Player attacks enemy."""
        damage = random.randint(5, player_stats["strength"])
        enemy["health"] -= damage
        return f"You deal {damage} damage to {enemy['name']}!"
        
    def enemy_attack(self, enemy, player_stats):
        """Enemy attacks player."""
        damage = random.randint(3, enemy["attack"])
        player_stats["health"] -= damage
        return f"{enemy['name']} deals {damage} damage to you!"


class MagicSystem:
    """Magic spell system."""
    
    def __init__(self):
        self.known_spells = []
        self.spell_database = {
            "heal": {"name": "Heal", "cost": 10, "effect": "restore_health", "description": "Restore health"},
            "fireball": {"name": "Fireball", "cost": 15, "effect": "fire_damage", "description": "Deal fire damage"},
            "shield": {"name": "Magic Shield", "cost": 12, "effect": "protection", "description": "Temporary protection"},
            "insight": {"name": "Insight", "cost": 8, "effect": "reveal_secrets", "description": "Reveal hidden information"},
            "teleport": {"name": "Teleport", "cost": 20, "effect": "instant_travel", "description": "Travel instantly"}
        }
        
    def initialize(self):
        """Initialize with basic spell."""
        self.known_spells.append("heal")
        
    def learn_spell(self, spell_id):
        """Learn a new spell."""
        if spell_id not in self.known_spells:
            self.known_spells.append(spell_id)
            spell = self.spell_database[spell_id]
            return f"✨ Learned new spell: {spell['name']}!"
        return "You already know this spell."
        
    def cast_spell(self, spell_id, player_stats):
        """Cast a spell."""
        if spell_id not in self.known_spells:
            return False, "You don't know this spell!"
            
        spell = self.spell_database[spell_id]
        if player_stats["mana"] < spell["cost"]:
            return False, "Not enough mana!"
            
        player_stats["mana"] -= spell["cost"]
        return True, f"✨ Cast {spell['name']}! {spell['description']}"


class CompanionSystem:
    """System for recruiting and managing companions."""
    
    def __init__(self):
        self.companions = []
        self.companion_database = {
            "spirit_wolf": {"name": "Spirit Wolf", "type": "guardian", "ability": "tracking", "loyalty": 50},
            "fairy_guide": {"name": "Fairy Guide", "type": "magical", "ability": "healing", "loyalty": 30},
            "ancient_owl": {"name": "Ancient Owl", "type": "wise", "ability": "knowledge", "loyalty": 40},
            "shadow_cat": {"name": "Shadow Cat", "type": "stealth", "ability": "stealth", "loyalty": 35}
        }
        
    def initialize(self):
        """Initialize companion system."""
        pass
        
    def recruit_companion(self, companion_id):
        """Recruit a new companion."""
        if len(self.companions) < 2:  # Max 2 companions
            companion = self.companion_database[companion_id].copy()
            self.companions.append(companion)
            return f"🐾 {companion['name']} joins your party!"
        return "You can only have 2 companions at a time."
        
    def display_companions(self):
        """Display current companions."""
        if not self.companions:
            return "You travel alone."
            
        text = "🐾 COMPANIONS:\n" + "=" * 30 + "\n"
        for companion in self.companions:
            text += f"• {companion['name']} ({companion['type']})\n"
            text += f"  Ability: {companion['ability']} | Loyalty: {companion['loyalty']}\n\n"
        return text


class TimeSystem:
    """Game time and time-based events."""
    
    def __init__(self):
        self.game_time = 0  # Game hours
        self.day_cycle = ["Dawn", "Morning", "Noon", "Afternoon", "Evening", "Night"]
        
    def initialize(self):
        """Initialize time system."""
        self.game_time = 6  # Start at dawn
        
    def advance_time(self, hours=1):
        """Advance game time."""
        self.game_time += hours
        
    def get_time_of_day(self):
        """Get current time of day."""
        cycle_index = (self.game_time // 4) % len(self.day_cycle)
        return self.day_cycle[cycle_index]
        
    def get_time_effects(self):
        """Get effects based on time of day."""
        time_of_day = self.get_time_of_day()
        effects = {
            "Dawn": "Peaceful energy, magic regeneration",
            "Morning": "Clear thinking, bonus to wisdom",
            "Noon": "Full strength, combat bonus",
            "Afternoon": "Steady progress, normal effects",
            "Evening": "Mystical hour, enhanced magic",
            "Night": "Stealth bonus, but reduced visibility"
        }
        return effects.get(time_of_day, "Normal effects")
