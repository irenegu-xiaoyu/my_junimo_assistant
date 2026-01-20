def handle_preferences_command():
    """Interactive preference setter"""
    print("\n✨ Let's set up your preferences!\n")
    
    # Playstyle
    print("What's your playstyle?")
    print("  1. Min-max (optimize everything)")
    print("  2. Casual (relaxed, enjoy the game)")
    print("  3. Roleplay (immersive, story-focused)")
    print("  4. Skip")
    choice = input("Choose (1-4): ").strip()
    if choice == "1":
        user_preferences["playstyle"] = "min-max optimizer"
    elif choice == "2":
        user_preferences["playstyle"] = "casual player"
    elif choice == "3":
        user_preferences["playstyle"] = "roleplayer"
    
    # Priorities
    print("\nWhat are your top priorities? (separate with commas)")
    print("  Examples: money, relationships, community center, fishing, mining, aesthetics")
    priorities = input("Priorities: ").strip()
    if priorities:
        user_preferences["priorities"] = [p.strip() for p in priorities.split(",")]
    
    # Focus NPCs
    print("\nAny specific NPCs you want to focus on? (separate with commas, or press Enter to skip)")
    npcs = input("NPCs: ").strip()
    if npcs:
        user_preferences["focus_npcs"] = [n.strip() for n in npcs.split(",")]
    
    # Things to avoid
    print("\nAnything you want to avoid? (separate with commas, or press Enter to skip)")
    print("  Examples: fishing, mining, animals, JojaMart")
    avoid = input("Avoid: ").strip()
    if avoid:
        user_preferences["avoid"] = [a.strip() for a in avoid.split(",")]
    
    # Custom notes
    print("\nAny other notes or preferences? (or press Enter to skip)")
    notes = input("Notes: ").strip()
    if notes:
        user_preferences["custom_notes"] = notes
    
    print("\n✅ Preferences saved! Your advice will now be tailored to your preferences.\n")
    show_preferences()

def show_preferences():
    """Display current preferences"""
    if not any([user_preferences["playstyle"], user_preferences["priorities"], 
                user_preferences["focus_npcs"], user_preferences["avoid"], 
                user_preferences["custom_notes"]]):
        print("📋 No preferences set yet. Use /preferences to set them.\n")
        return
    
    print("📋 CURRENT PREFERENCES:")
    if user_preferences["playstyle"]:
        print(f"  Playstyle: {user_preferences['playstyle']}")
    if user_preferences["priorities"]:
        print(f"  Priorities: {', '.join(user_preferences['priorities'])}")
    if user_preferences["focus_npcs"]:
        print(f"  Focus NPCs: {', '.join(user_preferences['focus_npcs'])}")
    if user_preferences["avoid"]:
        print(f"  Avoid: {', '.join(user_preferences['avoid'])}")
    if user_preferences["custom_notes"]:
        print(f"  Notes: {user_preferences['custom_notes']}")
    print()

def clear_preferences():
    """Clear all preferences"""
    user_preferences["playstyle"] = None
    user_preferences["priorities"] = []
    user_preferences["focus_npcs"] = []
    user_preferences["avoid"] = []
    user_preferences["custom_notes"] = ""
    print("🗑️  Preferences cleared!\n")

# -- User Preferences Store --
user_preferences = {
    "playstyle": None,  # e.g., "min-max", "casual", "roleplay"
    "priorities": [],   # e.g., ["money", "relationships", "completion"]
    "focus_npcs": [],   # Specific NPCs user wants to befriend
    "avoid": [],        # Things user wants to avoid
    "custom_notes": ""  # Any custom preferences
}

def get_preference_prompt() -> str:
    """Generate dynamic prompt section based on user preferences"""
    if not any([user_preferences["playstyle"], user_preferences["priorities"], 
                user_preferences["focus_npcs"], user_preferences["avoid"], 
                user_preferences["custom_notes"]]):
        return ""
    
    prompt_parts = ["\n--- USER PREFERENCES ---"]
    
    if user_preferences["playstyle"]:
        prompt_parts.append(f"Playstyle: {user_preferences['playstyle']}")
    
    if user_preferences["priorities"]:
        prompt_parts.append(f"Priorities (in order): {', '.join(user_preferences['priorities'])}")
    
    if user_preferences["focus_npcs"]:
        prompt_parts.append(f"Focus on befriending: {', '.join(user_preferences['focus_npcs'])}")
    
    if user_preferences["avoid"]:
        prompt_parts.append(f"Avoid: {', '.join(user_preferences['avoid'])}")
    
    if user_preferences["custom_notes"]:
        prompt_parts.append(f"Additional notes: {user_preferences['custom_notes']}")
    
    prompt_parts.append("--- TAILOR YOUR ADVICE TO THESE PREFERENCES ---\n")
    
    return "\n".join(prompt_parts)