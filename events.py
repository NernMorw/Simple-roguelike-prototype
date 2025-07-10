import random
from combat import start_combat
from player import player

def random_event():
    events = ["combat", "trap", "camp"]
    weights = [4, 2, 1]
    event_type = random.choices(events, weights=weights, k=1)[0]

    if event_type == "combat":
        print("\nYou encounter a wild enemy!")
        start_combat()
    elif event_type == "trap":
        dmg = random.randint(1, 15)
        player["HP"] -= dmg
        print(f"\nA hidden trap! You lose {dmg} HP.")
        print("Current HP: ", player['HP'])
    elif event_type == "camp":
        print("\nYou visited the camp")
        if player['HP'] < player['Max_HP']:
            heal = random.randint(5, player['Heal'])
            player['HP'] += heal
            print("You restored: ", heal, "HP")
        else:
            print("You aleredy have max HP")