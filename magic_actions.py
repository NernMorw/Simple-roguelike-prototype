from player import player

def magic_actions(enemy_hp, edmg, bleed, enemy_atk, can_necromancy, current_enemy):
    def attack_magic(enemy_hp, current_magic_damg, current_magic_cost, current_magic_name):
        if player['Energy'] >= current_magic_cost:
            enemy_hp -= current_magic_damg
            player['Energy'] -= current_magic_cost
            print(f"You have successfully cast {current_magic_name}!")
            print(f"Enemy took {current_magic_damg} damage!")
        else:
            print(f"Not enough energy for a {current_magic_name}! (Requires {current_magic_cost} energy)")
        return enemy_hp



    spawn_necro = False

    fire_arrow_cost = 2
    frost_bolt_cost = 2
    necromancy_cost = 4
    heal_magic_cost = 2

    fdmg = 1
    idmg = 1

    if "HResistance" in current_enemy:
        fdmg /= current_enemy['HResistance']
        idmg *= 2
    if "CResistance" in current_enemy:
        idmg /= current_enemy['CResistance']
        fdmg *= 2

    fire_arrow_damg = round(15 * (player['IMagic'] * player['IFArrow'] * fdmg))
    frost_bolt_damg = round(15 * (player['IMagic'] * player['IFBolt'] * idmg))
    heal_magic_heal = round(10 * (player['IMagic'] * player['IMHeal']))

    print("\033c", end="")
    print("--- Magic types ---")
    print(f"Fire arrow, cost: {fire_arrow_cost} energy.")
    print(f"Frost bolt, cost: {frost_bolt_cost} energy.")
    print(f"Necromancy, cost: {necromancy_cost} energy.")
    print(f"Heal magic, cost: {heal_magic_cost} energy.")
    print()

    valid_magic_actions = ["fire arrow", "farrow", "fbolt", "frost bolt", "necromancy", "necro", "heal magic", "mheal", "return"]
    magic_action = ""
    while magic_action not in valid_magic_actions:
        magic_action = input("\n[Return / Fire arrow / Necromancy / Heal magic]: ").lower()
        if magic_action not in valid_magic_actions:
            print("Invalid magic action. Please choose from the list.")
        elif magic_action == "return":
            return enemy_hp, edmg, bleed, enemy_atk, can_necromancy, current_enemy
    print("\033c", end="")

    if magic_action == "fire arrow" or magic_action == "farrow":
        if player['IFArrow'] > 0:
            enemy_hp = attack_magic(enemy_hp, fire_arrow_damg, fire_arrow_cost, "fire arrow")
        else:
            print("You can not cast fire arrow due to low skill")
    elif magic_action == "frost bolt" or magic_action == "fbolt":
        if player['IFBolt'] > 0:
            enemy_hp = attack_magic(enemy_hp, frost_bolt_damg, frost_bolt_cost, "frost bolt")
        else:
            print("You can not cast frost bolt due to low skill")

    elif magic_action == "necromancy" or magic_action == "necro":
        if player['INecro'] > 0:
            if player['Energy'] >= necromancy_cost and can_necromancy:
                player['Energy'] -= necromancy_cost
                print("You have successfully cast necromancy!")
                spawn_necro = True
            elif not can_necromancy:
                print("You can't cast necromancy!")
            else:
                print(f"Not enough energy for a necromancy! (Requires {necromancy_cost} energy)")
        else:
            print("You can not cast necromancy due to low skill")
    elif magic_action == "heal magic" or magic_action == "mheal":
        if player['IMHeal'] > 0:
            if player['Energy'] >= heal_magic_cost:
                player['Energy'] -= heal_magic_cost
                player['HP'] += heal_magic_heal
                print("You have successfully cast heal magic!")
                print(f"You healed for {heal_magic_heal} HP.")
            else:
                print(f"Not enough energy for a heal magic! (Requires {heal_magic_cost} energy)")
        else:
            print("You can not cast heal magic due to low skill")
    else:
        print("Invalid magic type.")
    return enemy_hp, edmg, bleed, False, spawn_necro, current_enemy
