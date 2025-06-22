"""
Save/Load System for Mystic Quest
=================================
Allows players to save their progress and continue their adventure later.
"""

import json
import os
from datetime import datetime


class SaveSystem:
    """Handle saving and loading game progress."""
    
    def __init__(self, game_engine):
        self.game = game_engine
        self.save_directory = "saves"
        self.ensure_save_directory()
        
    def ensure_save_directory(self):
        """Create saves directory if it doesn't exist."""
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
            
    def save_game(self, slot_name="quicksave"):
        """Save the current game state."""
        try:
            save_data = {
                "timestamp": datetime.now().isoformat(),
                "player_name": self.game.player_name,
                "player_health": self.game.player_health,
                "player_inventory": self.game.player_inventory,
                "game_state": self.game.game_state,
                "version": "2.0"
            }
            
            # Add enhanced systems data if available
            if hasattr(self.game, 'systems'):
                systems = self.game.systems
                save_data.update({
                    "player_stats": systems.stats_system.player_stats,
                    "inventory_items": systems.inventory_system.items,
                    "known_spells": systems.magic_system.known_spells,
                    "companions": systems.companion_system.companions,
                    "achievements": list(systems.achievement_system.unlocked_achievements),
                    "game_time": systems.time_system.game_time,
                    "current_weather": systems.weather_system.current_weather
                })
            
            filename = f"{self.save_directory}/{slot_name}.json"
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=2)
                
            return True, f"Game saved successfully to {slot_name}!"
            
        except Exception as e:
            return False, f"Failed to save game: {str(e)}"
            
    def load_game(self, slot_name="quicksave"):
        """Load a saved game state."""
        try:
            filename = f"{self.save_directory}/{slot_name}.json"
            
            if not os.path.exists(filename):
                return False, f"Save file '{slot_name}' not found!"
                
            with open(filename, 'r') as f:
                save_data = json.load(f)
                
            # Load basic game data
            self.game.player_name = save_data.get("player_name", "Adventurer")
            self.game.player_health = save_data.get("player_health", 100)
            self.game.player_inventory = save_data.get("player_inventory", [])
            self.game.game_state = save_data.get("game_state", {})
            
            # Load enhanced systems data if available
            if hasattr(self.game, 'systems') and "player_stats" in save_data:
                systems = self.game.systems
                systems.stats_system.player_stats = save_data["player_stats"]
                systems.inventory_system.items = save_data.get("inventory_items", {})
                systems.magic_system.known_spells = save_data.get("known_spells", ["heal"])
                systems.companion_system.companions = save_data.get("companions", [])
                systems.achievement_system.unlocked_achievements = set(save_data.get("achievements", []))
                systems.time_system.game_time = save_data.get("game_time", 6)
                systems.weather_system.current_weather = save_data.get("current_weather", "clear")
            
            timestamp = save_data.get("timestamp", "Unknown")
            return True, f"Game loaded successfully from {slot_name}! (Saved: {timestamp[:19]})"
            
        except Exception as e:
            return False, f"Failed to load game: {str(e)}"
            
    def list_saves(self):
        """List all available save files."""
        try:
            save_files = []
            for filename in os.listdir(self.save_directory):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.save_directory, filename)
                    with open(filepath, 'r') as f:
                        save_data = json.load(f)
                    
                    save_info = {
                        "name": filename[:-5],  # Remove .json extension
                        "player_name": save_data.get("player_name", "Unknown"),
                        "timestamp": save_data.get("timestamp", "Unknown"),
                        "level": save_data.get("player_stats", {}).get("level", 1) if "player_stats" in save_data else 1
                    }
                    save_files.append(save_info)
                    
            return save_files
            
        except Exception as e:
            return []
            
    def delete_save(self, slot_name):
        """Delete a save file."""
        try:
            filename = f"{self.save_directory}/{slot_name}.json"
            if os.path.exists(filename):
                os.remove(filename)
                return True, f"Save file '{slot_name}' deleted successfully!"
            else:
                return False, f"Save file '{slot_name}' not found!"
                
        except Exception as e:
            return False, f"Failed to delete save: {str(e)}"
            
    def display_save_menu(self):
        """Display save/load menu."""
        saves = self.list_saves()
        
        menu_text = """
┌─────────────────────────────────────────────────────────┐
│                    SAVE/LOAD MENU                       │
├─────────────────────────────────────────────────────────┤
│  1. Save Game                                           │
│  2. Load Game                                           │
│  3. List Saved Games                                    │
│  4. Delete Save                                         │
│  5. Return to Game                                      │
└─────────────────────────────────────────────────────────┘
"""
        
        if saves:
            menu_text += "\n📁 AVAILABLE SAVES:\n"
            menu_text += "=" * 50 + "\n"
            for save in saves:
                timestamp = save["timestamp"][:19] if save["timestamp"] != "Unknown" else "Unknown"
                menu_text += f"• {save['name']} - {save['player_name']} (Level {save['level']}) - {timestamp}\n"
                
        return menu_text
