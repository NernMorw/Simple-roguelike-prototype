from player import player

def player_upgrade_actions(enemy_hp, edmg, bleed, enemy_atk, can_necromancy):
    exit = False
    while exit == False:
        
        increase_hp = 10
        increase_eng = 1
        increase_atk = 1
        increase_heal = 1
        increase_necro = 1
        increase_fire_arrow = 1
        increase_heal_magic = 1
        increase_magic = 0.5
        heal_point_cost = 10
        increase_cost = 10

        old_magic = player['IMagic']
        old_necro = player['INecro'] * player['IMagic']
        old_farrow = player['IFArrow'] * player['IMagic']
        old_mheal = player['IMHeal'] * player['IMagic']

        new_magic = old_magic + increase_magic
        new_necro = old_necro + increase_necro
        new_farrow = old_farrow + increase_fire_arrow
        new_mheal = old_mheal + increase_heal_magic

        increasing_magic = increase_magic / new_magic * 100
        increasing_necro = ((1 + new_necro * old_magic) /  (1 + old_necro * old_magic)) * 100
        increasing_farrow = ((15 + new_farrow * old_magic) /  (15 + old_farrow * old_magic)) * 100
        increasing_mheal = ((10 + new_mheal * old_magic) / (10 + old_mheal * old_magic)) * 100

        print(f"You have: {player['SPoint']}")
        print()
        print(f"Increase cost = {player['SCost']}.")
        print(f"Type 'hp' for increase your max HP by {increase_hp}.")
        print(f"Type 'en' to increase your max energy by {increase_eng}.")
        print(f"Type 'atk' to increase your attack power by {increase_atk}.")
        print(f"Type 'heal' to increase your heal power by {increase_heal}.")
        print(f"Type 'magic' to increase the effectiveness of magic by {round(increasing_magic)}%.")
        print(f"Type 'farrow' to increase the effectiveness of fire arrow by {round(increasing_farrow)}%.")
        print(f"Type 'necro' to increase the effectiveness of necromancy by {round(increasing_necro)}%.")
        print(f"Type 'mheal' to increase the effectiveness of heal magic by {round(increasing_mheal)}%.")
        print(f"Type 'restore' to restore your hp and energy for {heal_point_cost} skill points.")
        print()
        print(f"Type 'return' to return.")

        valid_actions = ["return", "hp", "en", "energy", "atk", "attack", "heal", "restore", "magic", "farrow", "fire arrow", "necromancy", "necro", "mheal", "magic heal"]
        action = 0
        while action not in valid_actions:
            increase_input = input("\n[Return / HP / EN / ATK / Heal / Magic / FArrow / Necro / MHeal]: ").lower()
            action = increase_input
            if action not in valid_actions:
                print("Invalid action. Please choose from the list.")
            elif action == "return":
                exit = True
        print("")
        if increase_input == "restore" and player['SPoint'] >= heal_point_cost:
            player['HP'] = player['Max_HP']
            player['Energy'] = player['Max_Energy']
            player['SPoint'] -= heal_point_cost
            print("You have successfully restore your HP and energy")
        elif player['SPoint'] >= player['SCost']:
            if increase_input == "hp":
                player['Max_HP'] += increase_hp
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your max HP.")
            elif increase_input == "en" or increase_input == "energy":
                player['Max_Energy'] += increase_eng
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your max energy.")
            elif increase_input == "atk" or increase_input == "attack":
                player['ATK'] += increase_atk
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your attack power.")
            elif increase_input == "heal":
                player['Heal'] += increase_heal
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your heal power.")

            elif increase_input == "magic":
                player['IMagic'] += increase_magic
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your magic power.")
            elif increase_input == "necro" or increase_input == "necromancy":
                player['INecro'] += increase_necro
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your necromancy power.")
            elif increase_input == "farrow" or increase_input == "fire arrow":
                player['IFArrow'] += increase_fire_arrow
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your fire arrow power.")
            elif increase_input == "mheal" or increase_input == "magic heal":
                player['IMHeal'] += increase_heal_magic
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your heal magic power.")
            else:
                print("Invalid action.")
        elif increase_input == "return":
            exit = True
        else:
            print("Not enough SPoints")
    return