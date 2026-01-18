import xml.etree.ElementTree as ET
import os
from pathlib import Path

def find_latest_stardew_save():
    # 1. Detect the home directory (~/)
    home = Path.home()
    
    # 2. Define the standard Stardew save paths for Mac and Windows
    # Mac: ~/.config/StardewValley/Saves
    # Windows: %AppData%/StardewValley/Saves
    if os.name == 'posix':  # Mac or Linux
        save_path = home / ".config" / "StardewValley" / "Saves"
    else:  # Windows
        save_path = Path(os.environ['APPDATA']) / "StardewValley" / "Saves"

    if not save_path.exists():
        return "Save folder not found! Make sure the game is installed."

    # 3. Get all folders in the Saves directory
    all_saves = [d for d in save_path.iterdir() if d.is_dir()]
    
    if not all_saves:
        return "No save files found in the folder."

    # 4. Sort by 'last modified' to find your most recent play session
    latest_save_folder = max(all_saves, key=lambda d: d.stat().st_mtime)
    
    # 5. The actual save file has the same name as the folder
    save_file_name = latest_save_folder.name
    full_path = latest_save_folder / save_file_name
    
    return full_path


def get_farm_stats(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Define namespaces (Stardew XML usually doesn't need them for simple find)
    stats = {
        "farmer": root.find("player/name").text,
        "money": int(root.find("player/money").text),
        "day": root.find("dayOfMonth").text,
        "season": root.find("currentSeason").text,
        "year": root.find("year").text,
        "dailyLuck": float(root.find("dailyLuck").text)
    }
    
    return stats

# to use
game_data_file_path = find_latest_stardew_save()
print(f"Targeting save file: {game_data_file_path}")
game_state = get_farm_stats(game_data_file_path)
print(f"Game state: {game_state}")