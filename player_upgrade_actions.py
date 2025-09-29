from player import player

def player_upgrade_actions(enemy_hp, edmg, bleed, enemy_atk, can_necromancy):
    exit = False
    while not exit:
        print("\033c", end="")
        increase_hp = 10
        increase_eng = 1
        increase_atk = 1
        increase_heal = 1
        increase_necro = 1
        increase_fire_arrow = 1
        increase_frost_bolt = 1
        increase_heal_magic = 1
        increase_magic = 0.5
        heal_point_cost = 10
        increase_heat_resist = 1
        increase_cold_resist = 1

        def calc_increase_percent(old_value, new_value):
            if old_value == 0:
                return float('inf') if new_value > 0 else 0
            return round((new_value / old_value - 1) * 100)

        def format_percent(value):
            if value == float('inf'):
                return 'INFINITY%'
            return f"{value}%"

        old_magic = player['IMagic']
        old_necro = player['INecro']
        old_farrow = player['IFArrow']
        old_fbolt = player['IFBolt']
        old_mheal = player['IMHeal']

        new_magic = old_magic + increase_magic
        new_necro = old_necro + increase_necro
        new_farrow = old_farrow + increase_fire_arrow
        new_fbolt = old_fbolt + increase_frost_bolt
        new_mheal = old_mheal + increase_heal_magic

        old_necro_power = old_magic * old_necro / 10
        new_necro_power = old_magic * new_necro / 10
        new_necrom_power = new_magic * old_necro / 10

        old_farrow_power = 15 * (old_magic * old_farrow)
        new_farrow_power = 15 * (old_magic * new_farrow)
        new_farrowm_power = 15 * (new_magic * old_farrow)

        old_fbolt_power = 15 * (old_magic * old_fbolt)
        new_fbolt_power = 15 * (old_magic * new_fbolt)
        new_fboltm_power = 15 * (new_magic * old_fbolt)

        old_mheal_power = 10 * (old_magic * old_mheal)
        new_mheal_power = 10 * (old_magic * new_mheal)
        new_mhealm_power = 10 * (new_magic * old_mheal)

        increasing_magic = calc_increase_percent(old_magic, new_magic)
        increasing_necro = calc_increase_percent(old_necro_power, new_necro_power)
        increasing_farrow = calc_increase_percent(old_farrow_power, new_farrow_power)
        increasing_fbolt = calc_increase_percent(old_fbolt_power, new_fbolt_power)
        increasing_mheal = calc_increase_percent(old_mheal_power, new_mheal_power)

        increasing_farrowm = calc_increase_percent(old_farrow_power, new_farrowm_power)
        increasing_fboltm = calc_increase_percent(old_fbolt_power, new_fboltm_power)
        increasing_necrom = calc_increase_percent(old_necro_power, new_necrom_power)
        increasing_mhealm = calc_increase_percent(old_mheal_power, new_mhealm_power)


        print(f"You have: {player['SPoint']}")
        print()
        print(f"Increase cost = {player['SCost']}.")
        print(f"Type 'hp' for increase your max HP by {increase_hp}.")
        print(f"Type 'en' to increase your max energy by {increase_eng}.")
        print(f"Type 'atk' to increase your attack power by {increase_atk}.")
        print(f"Type 'heal' to increase your heal power by {increase_heal}.")
        print()
        print(f"Type 'magic' to increase the effectiveness of magic by {format_percent(increasing_magic)} (farrow {format_percent(increasing_farrowm)}, fbolt {format_percent(increasing_fboltm)}, necro {format_percent(increasing_necrom)}, mheal {format_percent(increasing_mhealm)}).")
        print(f"Type 'farrow' to increase the effectiveness of fire arrow by {format_percent(increasing_farrow)}.")
        print(f"Type 'fbolt' to increase the effectiveness of frost bolt by {format_percent(increasing_fbolt)}.")
        print(f"Type 'necro' to increase the effectiveness of necromancy by {format_percent(increasing_necro)}.")
        print(f"Type 'mheal' to increase the effectiveness of heal magic by {format_percent(increasing_mheal)}.")
        print()
        print(f"Type 'hres' to increase your heat resistance by {increase_heat_resist}.")
        print(f"Type 'cres' to increase your cold resistance by {increase_cold_resist}.")
        print()
        print(f"Type 'restore' to restore your hp and energy for {heal_point_cost} skill points.")
        print()
        print("Type 'return' to return.")

        valid_actions = ["return", "hp", "en", "energy", "atk", "attack", "heal", "restore", "magic", "farrow", "fire arrow", "fbolt", "frost bolt", "necromancy", "necro", "mheal", "magic heal", "hres", "cres"]
        action = 0
        while action not in valid_actions:
            increase_input = input("\n[Return / HP / EN / ATK / Heal / Magic / FArrow / Necro / MHeal / Restore]: ").lower()
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
            elif increase_input == "fbolt" or increase_input == "frost bolt":
                player['IFBolt'] += increase_frost_bolt
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your frost bolt power.")
            elif increase_input == "mheal" or increase_input == "magic heal":
                player['IMHeal'] += increase_heal_magic
                player['SPoint'] -= player['SCost']
                print("You have successfully increase your heal magic power.")
            
            elif increase_input == "hres":
                player['HResistance'] += increase_heat_resist
                player['SPoint'] -= player['SCost']
                print("Your heat resistance has been increased.")
            elif increase_input == "cres":
                player['CResistance'] += increase_cold_resist
                player['SPoint'] -= player['SCost']
                print("Your cold resistance has been increased.")
            else:
                print("Invalid action.")
        elif increase_input == "return":
            exit = True
        else:
            print("Not enough SPoints")
    print("\033c", end="")
    return enemy_hp, edmg, bleed, enemy_atk, can_necromancy
