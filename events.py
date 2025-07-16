import random
from combat import start_combat
from player import player
from player_actions import add_item_to_inventory
from items import item

def random_event():
    events = ["combat", "trap", "camp", "loot"] 
    weights = [4, 2, 1, 1] 
    event_type = random.choices(events, weights=weights, k=1)[0]

    if event_type == "combat":
        print("\nYou encounter a wild enemy!")
        start_combat()
    elif event_type == "trap":
        dmg = random.randint(1, 15)
        endmg = 1
        player['HP'] -= dmg
        player['Energy'] -= endmg
        print(f"\nA hidden trap! You lose {dmg} HP.")
        print(f"You lose {endmg} energy.")
        print(" Current HP: ", round(player['HP']))
    elif event_type == "camp":
        print("\nYou visited the camp")
        if player['HP'] < player['Max_HP']:
            heal = random.randint(5, player['Heal'])
            player['HP'] += heal
            player['Energy'] = player['Max_Energy']
            print("You restored: ", heal, "HP")
            print("Your energy has been restored!")
        else:
            print("You already have max HP")
            player['Energy'] = player['Max_Energy']
            print("Your energy has been restored!")
    elif event_type == "loot":
        print("\nYou found a mysterious chest!")
        possible_items = list(item.keys())
        found_item_key = random.choice(possible_items)
        add_item_to_inventory(player, found_item_key, item)