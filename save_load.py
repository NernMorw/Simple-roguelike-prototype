import json
from player import player

def save_game():
    print()
    SAVE_FILE_INPUT = input("Save navne: ")
    SAVE_FILE = f"{SAVE_FILE_INPUT}.json"
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump(player, f, indent=4)
        print(f"\nGame saved in {SAVE_FILE}")
    except IOError as e:
        print(f"\nGame saved error: {e}")

def load_game():
    global player
    SAVE_FILE_INPUT = input("Save navne: ")
    SAVE_FILE = f"{SAVE_FILE_INPUT}.json"
    try:
        with open(SAVE_FILE, 'r') as f:
            loaded_player_data = json.load(f)
            player.update(loaded_player_data)
        print(f"\nGame loaded from {SAVE_FILE}")
        return True
    except FileNotFoundError:
        print("\nSave file not found. Starting a new game.")
        return False
    except json.JSONDecodeError as e:
        print(f"\nError reading save file (maybe it's corrupted): {e}")
        return False
    except Exception as e:
        print(f"\nUnknown load error: {e}")
        return False