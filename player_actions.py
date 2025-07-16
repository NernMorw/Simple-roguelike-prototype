import random
from player import player
from items import item

def add_item_to_inventory(player_data, item_key, items_data):
    if item_key in items_data:
        if item_key in player_data["Inventory"]:
            player_data["Inventory"][item_key]["Count"] += 1
            print(f"Count of {items_data[item_key]['Name']} increased to {player_data['Inventory'][item_key]['Count']}.")
        else:
            new_item = items_data[item_key].copy()
            new_item["Count"] = 1
            player_data["Inventory"][item_key] = new_item
            print(f"{items_data[item_key]['Name']} added to inventory. Count: 1.")
    else:
        print(f"Item '{item_key}' does not exist.")

def actions(enemy_hp, edmg, bleed, enemy_atk, can_necromancy):
        heal_cost = 1
        fire_arrow_cost = 2
        necromancy_cost = 3
        heal_magic_cost = 2
        D = 1
        rest = 1

        spawn_skeleton = False
        fire_arrow_damg = random.randint(15, 15 * player['Level'])
        heal_magic_heal = random.randint(10, 10 * player['Level'])

        valid_actions = ["attack", "strong attack", "heal", "parry", "defence", "magic", "rest", "run", "inventory"]
        action = ""
        while action not in valid_actions:
            action = input("\n[Attack / Strong Attack / Heal / Parry / Defence / Magic / Rest / Run / Inventory]: ").lower()
            if action not in valid_actions:
                print("Invalid action. Please choose from the list.")
        print('\n')

        if action == "attack":
            dmg = random.randint(1, player["ATK"])
            enemy_hp -= dmg
            print(f"\n\nYou deal {dmg} damage.")
        elif action == "heal":
            healed_amount = random.randint(2, player['Heal'])
            if player['Energy'] >= heal_cost:
                if bleed > 0:
                    bleed -= 1
                    player['Energy'] -= heal_cost
                    print(f"You successfully healed 1 bleed!")
                else:
                    player['HP'] += healed_amount
                    player['Energy'] -= heal_cost
                    print(f"You successfully healed for {healed_amount} HP!")
            else:
                print(f"Not enough energy to heal! (Requires {heal_cost} energy)")
        elif action == "run":
            is_succesfull = random.randint(1, 3)
            if is_succesfull != 1 and player['Energy'] >= 2:
                print("You fled the battle!")
                player['Energy'] -= 2
                return enemy_hp, edmg, bleed, True, spawn_skeleton
            else:
                print("You didn't manage to escape!")
        elif action == "parry":
            parry_cost = 2
            if player['Energy'] >= parry_cost:
                enemy_hp -= round(0.5 * edmg)
                edmg = 0
                player['Energy'] -= parry_cost
                print(f"You have successfully parry enemy attack! Enemy take {round(0.5 * enemy_atk)} damage!")
            else:
                print(f"Not enough energy to parry! (Requires {parry_cost} energy)")
        elif action == "defence":
            defence_cost = 1
            if player['Energy'] >= defence_cost:
                D = 2
                edmg /= D
                player['Energy'] -= defence_cost
                print(f"Enemy damage reduced by {D} times")
            else:
                print(f"Not enough energy to defence! (Requires {defence_cost} energy)")
        elif action == "rest":
            player['Energy'] += rest
            print(f"You have recovered {rest} energy!")
        elif action == "strong" or action == "strong attack":
            strong_attack_cost = 2
            if player['Energy'] >= strong_attack_cost:
                dmg = 2 * (random.randint(1, player["ATK"]))
                enemy_hp -= dmg
                player['Energy'] -= strong_attack_cost
                print(f"\n\nYou deal {dmg} damage.")
            else:
                print(f"Not enough energy for a strong attack! (Requires {strong_attack_cost} energy)")
        elif action == "magic":
            
            print("--- Magick types ---")
            print(f"Fire arrow, cost: {fire_arrow_cost} energy.")
            print(f"Necromancy, cost: {necromancy_cost} energy.")
            print(f"Heal magic, cost: {heal_magic_cost} energy.")
            print()
                
            valid_magic_actions = ["fire arrow", "necromancy", "heal magic"]
            magic_action = 1
            while magic_action not in valid_magic_actions:
                magic_action = input("").lower()
                if magic_action not in valid_magic_actions:
                    print("Invalid magic action. Please choose from the list.")
            print('\n')

            if magic_action == "fire arrow":
                if player['Energy'] >= fire_arrow_cost:
                    enemy_hp -= fire_arrow_damg
                    player['Energy'] -= fire_arrow_cost
                    print("You have successfully cast fire arrow!")
                    print(f"Enemy took {fire_arrow_damg} damage!")
                else:
                    print(f"Not enough energy for a fire arrow! (Requires {fire_arrow_cost} energy)")
            elif magic_action == "necromancy":
                if player['Energy'] >= necromancy_cost and can_necromancy:
                    player['Energy'] -= necromancy_cost
                    print("You have successfully cast necromancy!")
                    spawn_skeleton = True
                elif not can_necromancy:
                    print("You can't cast necromancy!")
                else:
                    print(f"Not enough energy for a necromancy! (Requires {necromancy_cost} energy)")
            elif magic_action == "heal magic":
                if player['Energy'] >= heal_magic_cost:
                    player['Energy'] -= heal_magic_cost
                    player['HP'] += heal_magic_heal
                    print("You have successfully cast heal magic!")
                    print(f"You healed for {heal_magic_heal} HP.")
                else:
                    print(f"Not enough energy for a heal magic! (Requires {heal_magic_cost} energy)")
            else:
                print("Invalid magic type.")
        elif action == "inventory":
            if not player["Inventory"]:
                print("Your inventory is empty.")
            else:
                print("\n--- Inventory ---")
                for item_key, item_details in player["Inventory"].items():
                    print(f"- {item_details['Name']} (Count: {item_details['Count']})")
                print("---------------------")
                
                if player["Inventory"]:
                    use_item_choice = input("Would you like to use the item? (name/no): ").lower()
                    print()
                    if use_item_choice != "no":
                        item_found = False
                        for item_key, item_details in player["Inventory"].items():
                            if use_item_choice == item_details['Name'].lower():
                                item_found = True
                                if item_details['Count'] > 0:
                                    if "Heal" in item_details:
                                        player['HP'] += item_details['Heal']
                                        print(f"You used {item_details['Name']} and heal {item_details['Heal']} HP.")
                                    elif "EHeal" in item_details:
                                        player['Energy'] += item_details['EHeal']
                                        print(f"You used {item_details['Name']} and restore {item_details['EHeal']} energy.")
                                    elif "Damage" in item_details:
                                        enemy_hp -= item_details['Damage']
                                        print(f"You used {item_details['Name']} and deal {item_details['Damage']} damage.")
                                    
                                    item_details['Count'] -= 1
                                    if item_details['Count'] == 0:
                                        del player["Inventory"][item_key]
                                        print(f"\n{item_details['Name']} has expired and has been removed from inventory.")
                                else:
                                    print(f"You don't have {item_details['Name']}.")
                                break
                        if not item_found:
                            print("Invalid item name.")
                    else:
                        print("You have decided not to use the item.")
        else:
            print("Invalid action.")

        return enemy_hp, edmg, bleed, False, spawn_skeleton