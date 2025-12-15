from utils.cache_input import get_input

NUMBER_DAY = "4"

TEST_INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

TEST_OUTPUT_FIRST = 13
TEST_OUTPUT_SECOND = 43

def second_part(raw_data: str): 

    raw_base_map = raw_data

    coor_rolls = first_part(raw_base_map)

    raw_base_map = uptade_roll_map(coor_rolls, raw_base_map)

    moved_rolls = len(coor_rolls)

    while len(coor_rolls) > 0:
        raw_base_map = uptade_roll_map(coor_rolls, raw_base_map)
        coor_rolls.clear()
        coor_rolls = first_part(raw_base_map)
        moved_rolls += len(coor_rolls)

    return moved_rolls
    
def first_part(raw_entry: str):
    base_map = raw_entry.splitlines()
    roll_char = '@'
    moved_rolls = 0

    pos_rolls = []

    for row, line in enumerate(base_map):
        for column, char in enumerate(line):
            if char == roll_char:
                if check_for_rolls(column, row, base_map):
                    pos_rolls.append((row, column))
                    moved_rolls += 1

    return pos_rolls

"""
Para la segunda parte vamos a guardar la row, col de cada rollo movido, al finalizar el mapa
Pasamos esta lista de coordenadas para cambiar '@' por '.' y volviendo a pasar por el proceso
mientras que moved_rolls sea distinto de cero vamos a seguir haciendo esto y registrando cuantos
rollos se movieron cada vez que se hizo el proceso 
"""

def uptade_roll_map(moved_coor:list[tuple], base_map: str)-> str:
    splited_map = base_map.splitlines()
    new_map = ""
    
    for row, line in enumerate(splited_map):
        new_line = ""
        for col, char in enumerate(line):
            
            if (row, col) in moved_coor:
                new_line += "."
            else:
                new_line += char
        new_map += new_line + "\n"

    return new_map
                    

def check_for_rolls(posx: int, posy: int, base_map: list[list[str]]) -> bool:
    
    max_rolls = 4
    roll_char = "@"
    rolls = 0
    l_line = len(base_map[0])

    # print(f"Checking: {posx} | {posy}")

    def check_num_rolls(rolls) -> bool:
        return rolls < max_rolls
    
    # Podemos refactorizar ya que si entra aqui es por que es un '@'
    # add the checking of map edges
    # Corners
    if posx == 0 and posy == 0:
        return True if base_map[posy][posx] == roll_char else False

    if posx == len(base_map[posy]) - 1 and posy == 0:
        return True if base_map[posy][posx] == roll_char else False

    if posy == len(base_map) - 1 and posx == 0:
        return True if base_map[posy][posx] == roll_char else False
        
    if posy == len(base_map) - 1 and posx == len(base_map[posy]) - 1:
        return True if base_map[posy][posx] == roll_char else False

    # Upper Edge
    if posy == 0 and posx > 0 and posx < len(base_map[posy]):
        # Adelante
        if base_map[posy][posx + 1] == roll_char:
            rolls += 1
        # Atras
        if base_map[posy][posx - 1] == roll_char:
            rolls += 1
        # Adelante - Abajo
        if base_map[posy + 1][posx + 1] == roll_char:
            rolls += 1
        # Atras - Abajo
        if base_map[posy + 1][posx - 1] == roll_char:
            rolls += 1
        # Abajo
        if base_map[posy + 1][posx] == roll_char:
            rolls += 1

        return check_num_rolls(rolls)
    
    # Left Edge
    if posx == 0 and ( posy > 0 and posy < len(base_map)):
        #Up 
        if base_map[posy - 1][posx] == roll_char:
            rolls += 1
        # Up Front
        if base_map[posy - 1][posx + 1] == roll_char:
            rolls += 1
        # Front 
        if base_map[posy][posx + 1] == roll_char:
            rolls += 1
        # Down Front
        if base_map[posy + 1][posx + 1] == roll_char:
            rolls += 1
        # Down
        if base_map[posy + 1][posx] == roll_char:
            rolls += 1

        return check_num_rolls(rolls)

    # Right Edge
    if posx == l_line - 1 and (posy > 0 and posy < len(base_map)):
         #Up 
        if base_map[posy - 1][posx] == roll_char:
            rolls += 1
        # Up Back
        if base_map[posy - 1][posx - 1] == roll_char:
            rolls += 1
        # Back
        if base_map[posy][posx - 1] == roll_char:
            rolls += 1
        # Down Back
        if base_map[posy + 1][posx - 1] == roll_char:
            rolls += 1
        # Down
        if base_map[posy + 1][posx] == roll_char:
            rolls += 1

        return check_num_rolls(rolls)
    
    # Lower Edge
    if posy == len(base_map) - 1 and (posx > 0 and posx < len(base_map[posy])):
        # Front
        if base_map[posy][posx + 1] == roll_char:
            rolls += 1
        # Back
        if base_map[posy][posx - 1] == roll_char:
            rolls += 1
        # Up - Front
        if base_map[posy - 1][posx + 1] == roll_char:
            rolls += 1
        # Up - Back
        if base_map[posy - 1][posx - 1] == roll_char:
            rolls += 1
        # Up
        if base_map[posy - 1][posx] == roll_char:
            rolls += 1

        return check_num_rolls(rolls)

    # Center of Map
    # adelante - atras 
    if base_map[posy][posx - 1] == roll_char:
        rolls += 1
       
    if base_map[posy][posx + 1] == roll_char:
        rolls += 1

    # abajo - arriba
    if base_map[posy + 1][posx] == roll_char:
        rolls += 1
    
    if base_map[posy - 1][posx] == roll_char:
        rolls += 1

    # early return ? 
    if not check_num_rolls(rolls):
        return False
    
    # back front up 
    if base_map[posy + 1][posx - 1] == roll_char:
        rolls += 1

    if base_map[posy + 1][posx + 1] == roll_char:
        rolls += 1

    if not check_num_rolls(rolls):
        return False
    
    # back front - down

    if base_map[posy - 1][posx - 1] == roll_char:
        rolls += 1

    if base_map[posy - 1][posx + 1] == roll_char:
        rolls += 1

    if not check_num_rolls(rolls):
        return False
    
    return True
    
# TODO Change posx to column, posy to row
# TODO Check for map edges comparisions like posx = len(base_map) - 1, and so on...
# TODO Check consistencia de los returns de los rollos... 


if __name__ == "__main__":
    res_val = 0
    # try:
    #     res_val = first_part(TEST_INPUT)
    # except Exception as e:
    #     print("Error in process: ", e)

    personal_input = get_input(NUMBER_DAY)

    test = False

    # if test:
    #     res_val = first_part(TEST_INPUT)

    #     if res_val == TEST_OUTPUT:
    #         print("Passed: ", res_val)
    #     else: 
    #         print("Not Passed: ", res_val)
    # else:
    #     try:
    #         res_val = first_part(personal_input)
    #         print(res_val)
    #     except ValueError:
    #         print("Something went wrong :(")

    if test: 
        res_val = second_part(TEST_INPUT)
        if res_val == TEST_OUTPUT_SECOND:
            print("Passed: ", res_val)
        else: 
            print("Not Passed: ", res_val)
    else:
        try:
            res_val = second_part(personal_input)
            print(res_val)
        except ValueError:
            print("Something went wrong :(")
