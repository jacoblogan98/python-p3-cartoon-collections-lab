def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves):
        print(f"{i+1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [f"{call.capitalize()}!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    
    return False

def find_the_cheese(foods):
    for food in foods:
        if food == "cheddar" or food == "gouda" or food == "camembert":
            return food
    
    return None
