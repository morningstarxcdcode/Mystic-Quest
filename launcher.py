#!/usr/bin/env python3
"""
Mystic Quest Launcher
====================
Choose between the original classic experience or the new enhanced edition.
"""

import os
import sys
import subprocess


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_launcher():
    """Display the game launcher menu."""
    clear_screen()
    
    launcher_art = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║    ███╗   ███╗██╗   ██╗███████╗████████╗██╗ ██████╗     ║
    ║    ████╗ ████║╚██╗ ██╔╝██╔════╝╚══██╔══╝██║██╔════╝     ║
    ║    ██╔████╔██║ ╚████╔╝ ███████╗   ██║   ██║██║          ║
    ║    ██║╚██╔╝██║  ╚██╔╝  ╚════██║   ██║   ██║██║          ║
    ║    ██║ ╚═╝ ██║   ██║   ███████║   ██║   ██║╚██████╗     ║
    ║    ╚═╝     ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚═╝ ╚═════╝     ║
    ║                                                          ║
    ║         ██████╗ ██╗   ██╗███████╗███████╗████████╗       ║
    ║        ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝       ║
    ║        ██║   ██║██║   ██║█████╗  ███████╗   ██║          ║
    ║        ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║          ║
    ║        ╚██████╔╝╚██████╔╝███████╗███████║   ██║          ║
    ║         ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝          ║
    ║                                                          ║
    ║                    🎮 GAME LAUNCHER 🎮                   ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    
    print(launcher_art)
    print()
    print("=" * 60)
    print("           Welcome to Mystic Quest!")
    print("=" * 60)
    print()
    
    print("┌─────────────────────────────────────────────────────────┐")
    print("│                   CHOOSE YOUR EDITION                   │")
    print("├─────────────────────────────────────────────────────────┤")
    print("│                                                         │")
    print("│  1. 🌟 ENHANCED EDITION (Recommended)                  │")
    print("│     • Advanced RPG systems & character progression     │")
    print("│     • Dynamic weather and time mechanics               │")
    print("│     • Magic system with 10+ spells                     │")
    print("│     • Companion recruitment system                     │")
    print("│     • Inventory management & item crafting             │")
    print("│     • Achievement system & save/load                   │")
    print("│     • 3 unique new scenes with time travel             │")
    print("│     • 15+ different endings                            │")
    print("│                                                         │")
    print("│  2. 📖 CLASSIC EDITION                                 │")
    print("│     • Original simple adventure experience             │")
    print("│     • Choice-based storytelling                        │")
    print("│     • Beautiful ASCII art                              │")
    print("│     • Multiple story paths                             │")
    print("│     • Lightweight and fast                             │")
    print("│                                                         │")
    print("│  3. 📚 View Documentation                              │")
    print("│     • Read about new features                          │")
    print("│     • Game guides and tips                             │")
    print("│                                                         │")
    print("│  4. 🚪 Exit                                            │")
    print("│                                                         │")
    print("└─────────────────────────────────────────────────────────┘")
    print()


def launch_enhanced():
    """Launch the enhanced edition."""
    try:
        print("🌟 Starting Mystic Quest Enhanced Edition...")
        print("Loading advanced systems...")
        subprocess.run([sys.executable, "main_enhanced.py"])
    except FileNotFoundError:
        print("❌ Enhanced edition not found! Please ensure main_enhanced.py exists.")
        input("Press Enter to return to launcher...")
        main()
    except Exception as e:
        print(f"❌ Error launching enhanced edition: {e}")
        input("Press Enter to return to launcher...")
        main()


def launch_classic():
    """Launch the classic edition."""
    try:
        print("📖 Starting Mystic Quest Classic Edition...")
        print("Loading original adventure...")
        subprocess.run([sys.executable, "main.py"])
    except FileNotFoundError:
        print("❌ Classic edition not found! Please ensure main.py exists.")
        input("Press Enter to return to launcher...")
        main()
    except Exception as e:
        print(f"❌ Error launching classic edition: {e}")
        input("Press Enter to return to launcher...")
        main()


def view_documentation():
    """Display documentation options."""
    clear_screen()
    print("📚 MYSTIC QUEST DOCUMENTATION")
    print("=" * 50)
    print()
    print("Available documentation:")
    print()
    print("1. Enhanced Edition Features (README_ENHANCED.md)")
    print("2. Original Game Guide (README.md)")
    print("3. Return to Launcher")
    print()
    
    choice = input("Select documentation (1-3): ").strip()
    
    if choice == '1':
        try:
            with open("README_ENHANCED.md", 'r') as f:
                content = f.read()
            print("\n" + "=" * 60)
            print("ENHANCED EDITION DOCUMENTATION")
            print("=" * 60)
            print(content[:2000])  # Show first 2000 characters
            print("\n... (truncated for display)")
            print("\nFor full documentation, open README_ENHANCED.md in a text editor.")
        except FileNotFoundError:
            print("❌ Enhanced documentation not found!")
    elif choice == '2':
        try:
            with open("README.md", 'r') as f:
                content = f.read()
            print("\n" + "=" * 60)
            print("CLASSIC EDITION DOCUMENTATION")
            print("=" * 60)
            print(content[:2000])  # Show first 2000 characters
            print("\n... (truncated for display)")
            print("\nFor full documentation, open README.md in a text editor.")
        except FileNotFoundError:
            print("❌ Classic documentation not found!")
    
    input("\nPress Enter to return to launcher...")
    main()


def main():
    """Main launcher function."""
    while True:
        display_launcher()
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            launch_enhanced()
        elif choice == '2':
            launch_classic()
        elif choice == '3':
            view_documentation()
        elif choice == '4':
            clear_screen()
            print("🌟 Thank you for playing Mystic Quest!")
            print("Your adventure awaits your return...")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🌟 Thanks for playing Mystic Quest!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Launcher error: {e}")
        sys.exit(1)
