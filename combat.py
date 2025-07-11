import random
from player import player
from enemies import enemy_types



def start_combat():
    
    heal_cost = 1
    fire_arrow_cost = 2
    necromancy_cost = 3
    heal_magic_cost = 2

    fire_arrow_damg = 15
    heal_magic_heal = 10 * player['Level']

    bleed = 0
    enemy_names = list(enemy_types.keys())
    chosen_enemy_name = random.choice(enemy_names)
    current_enemy = enemy_types[chosen_enemy_name]

    level_diff = player['Level'] - current_enemy['Level']
    enemy_level_up = 1.1 ** level_diff

    if current_enemy['Level'] < player['Level']:
        current_enemy['Level'] = player['Level']
        current_enemy['Max_HP'] *= enemy_level_up
        current_enemy['ATK'] *= enemy_level_up

    if "Heal" in current_enemy:
        can_heal = True
    else:
        can_heal = False

    if "Bleed_Attack" in current_enemy:
        can_bleed_attack = True
    else:
        can_bleed_attack = False

    enemy_hp = round(current_enemy['Max_HP'])
    exp_gained = current_enemy['EXP_Gain']

    while enemy_hp > 0 and player["HP"] > 0:

        is_restored_hp = False
        if bleed > 0:
            bleed -= 1
        D = 1
        enemy_atk = round(current_enemy['ATK'])
        edmg = random.randint(3, round(enemy_atk))
        bleed_attack = 0.4 * edmg
        bdmg = random.randint(1, 5)

        print("\n", player['Name'])
        print("HP:       ", round(player['HP']), "/", player['Max_HP'])
        print("Energy:   ", player['Energy'], "/", player['Max_Energy'])
        print("Level     ", player['Level'])
        print("EXP:      ", player['EXP'], "/", player['Need_EXP'])
        print("\n--- A New Enemy Appears! ---")
        print("\n", chosen_enemy_name)
        print("Enemy HP:  ", round(enemy_hp))
        print("Enemy ATK: ", enemy_atk)

        action = input("\n[Attack / Strong Attack / Heal / Parry / Defence / Magic / Rest / Run]: ").lower()
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
                return
            else:
                print("You didn't manage to escape!")
        elif action == "parry":
            parry_cost = 2
            if player['Energy'] >= parry_cost:
                enemy_hp -= 0.5 * enemy_atk
                edmg = 0
                player['Energy'] -= parry_cost
                print(f"You hane succsfully parry enemy attack! Enemy take {round(0.5 * enemy_atk)} damage!")
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
            rest = 1
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
            
            print("---Magick types---")
            print(f"Fire arrow, cost: {fire_arrow_cost} energy.")
            print(f"Necromancy, cost: {necromancy_cost} energy. (Coming soon)")
            print(f"Heal magic, cost: {heal_magic_cost} energy.")
            print()
            magic_action = input("").lower()

            if magic_action == "fire arrow":
                if player['Energy'] >= fire_arrow_cost:
                    enemy_hp -= fire_arrow_damg
                    player['Energy'] -= fire_arrow_cost
                    print("You have successfully caste fire arrow!")
                    print(f"Enemy took {fire_arrow_damg} damage!")
                else:
                    print(f"Not enough energy for a fire arrow! (Requires {fire_arrow_cost} energy)")
            elif magic_action == "necromancy":
                if player['Energy'] >= necromancy_cost:
                    player['Energy'] -= necromancy_cost
                    print("You have successfully caste necromancy!")
                else:
                    print(f"Not enough energy for a necromancy! (Requires {necromancy_cost} energy)")
            elif magic_action == "heal magic":
                if player['Energy'] >= heal_magic_cost:
                    player['Energy'] -= heal_magic_cost
                    player['HP'] += heal_magic_heal
                    print("You have successfully caste heal magic!")
                    print(f"You healed for {heal_magic_heal} HP.")
                else:
                    print(f"Not enough energy for a heal magic! (Requires {heal_magic_cost} energy)")
            else:
                print("Invalid magic type.")
        else:
            print("Invalid action.")

        if player['HP'] > player['Max_HP']:
            player['HP'] = player['Max_HP']

        if enemy_hp > 0:
            if can_heal == True:
                if enemy_hp < current_enemy['Max_HP'] - 2 * current_enemy['Heal'] and not is_restored_hp:
                    enemy_hp += current_enemy['Heal']
                    print(f"{chosen_enemy_name} heal {current_enemy['Heal']} HP!")
                    is_restored_hp = True
                else:
                    player["HP"] -= edmg
                    print(f"\nThe enemy hits you for {edmg} damage.")
                    is_restored_hp = False
            elif can_bleed_attack:
                if bleed == 0:
                    bleed = current_enemy['Bleed_Attack']
                    player['HP'] -= bleed_attack
                    print(f"The enemy hits you with a bloody attack for {round(bleed_attack)} damage.")
                else:
                    player['HP'] -= edmg
                    player['HP'] -= bdmg
                    print(f"\nThe enemy hits you for {edmg} damage.")
                    print(f"You lost {bdmg} HP due to bleeding.")
            else:
                player["HP"] -= edmg
                print(f"\nThe enemy hits you for {edmg} damage.")
        else:
            print(f"\nYou defeated the {chosen_enemy_name}!")
            player['EXP'] += exp_gained
            print(f"You gained {exp_gained} EXP!")
        
        input()