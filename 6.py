from utils.cache_input import get_input
from math import prod
from typing import List, Tuple

NUMBER_DAY = "6"

TEST_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def transpose_lists(original_array:list[list[int]]):
    return [list(line) for line in zip(*original_array)]


def parse_input(raw_input:str) -> tuple[list[str], list[int]]:
    array_2d = raw_input.splitlines()
    opts = array_2d.pop()
    number_lists = []

    opts_list =  " ".join(opts.split()).split(" ")

    for values in array_2d:
        clean_line = " ".join(values.split())
        line_list = []
        for number in clean_line.split(" "):
            line_list.append(int(number))

        number_lists.append(line_list)

    # transpose
    t_array = transpose_lists(number_lists)

    return (opts_list, t_array)

def process_opts(opts_list: list[str], nums_list:list[list[int]]):

    sum_opt = "+"
    prod_opt = "*"

    total = 0

    for i, nums in enumerate(nums_list):
        if opts_list[i] == sum_opt:
            total += sum(nums)

        if opts_list[i] == prod_opt:
            total += prod(nums)

    return total

"""
Idea para dia dos: Desde que los datos son str aumentar todos a 3 digitos 
si tienen menos de 3 le ponemos zeros al final -> [640, 230, 314] para que despues de hacer 
la transpuesta [004, 431, 623] con opt + [004 + 431 + 623] = 1058
[123, 450, 600 ] -> transpose: []
"""

"""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
"""

"""
123 328  x51 64x
x45 64x  387 23x 
xx6 98x  215 314
"""
# Funciona para el input test pero no para el personal...
def normalize_line(line: str) -> str:
    result = ""
    i = 0

    while i < len(line):
        block = line[i:i+3]
        digits = block.strip()
        if digits:
            missing = 3 - len(digits)

            if block.startswith(" "):
                block = "x" * missing + digits
            elif block.endswith(" "):
                block = digits + "x" * missing
            else:
                block = digits

        result += block

        i += 4

    return result


def split_chunks(string, size_chunks):
    return [string[char:char + size_chunks] for char in range(0, len(string), size_chunks)]
 

def parse_input_second(raw_input:str) -> tuple[list[str], list[str]]:
    array_2d = raw_input.splitlines()
    opts = array_2d.pop()
    number_lists_str = []

    opts_list =  " ".join(opts.split()).split(" ")

    for values in array_2d:
        new_line = normalize_line(values)
        new_line_list = split_chunks(new_line, 3)
        number_lists_str.append(new_line_list)

    t_num_list = transpose_lists(number_lists_str)

    t_matrix = [transpose_lists(element) for element in t_num_list]

    real_proces_nums = []

    for matrix in t_matrix:
        real_num_list = []
        for value in matrix:
            raw_val = "".join(value).replace("x", "")
            real_num = int(raw_val)
            real_num_list.append(real_num)

        real_proces_nums.append(real_num_list)

    return (opts_list, real_proces_nums)


def parse_input_lines(raw_input: str): 

    array_2d = raw_input.splitlines()
    opts = array_2d.pop()
    
    opts_list = " ".join(opts.split()).split(" ")

    return (opts_list, array_2d)


def split_into_grid_columns(block: str) -> List[List[str]]:
    lines = block
    if not lines:
        return []

    # 1) Pad to same length (so indexing lines[i] is safe)
    width = max(len(l) for l in lines)
    padded = [l.ljust(width) for l in lines]

    # 2) Positions that are spaces in ALL lines => separators
    all_space = [all(p[i] == " " for p in padded) for i in range(width)]

    # Find runs of separator positions (usually 1-char runs)
    runs: List[Tuple[int, int]] = []
    i = 0
    while i < width:
        if all_space[i]:
            j = i
            while j < width and all_space[j]:
                j += 1
            runs.append((i, j))
            i = j
        else:
            i += 1

    # 3) Build cut points around separator runs
    cuts = {0, width}
    for a, b in runs:
        cuts.add(a)  # cut before separator run
        cuts.add(b)  # cut after separator run
    cuts = sorted(cuts)

    # 4) Create segments between cuts, skipping pure-separator segments
    segments = []
    for s, e in zip(cuts, cuts[1:]):
        if s < e and all(all_space[k] for k in range(s, e)):
            continue
        segments.append((s, e))

    # 5) Extract column-groups (one group = same slice from each line)
    groups = []
    for s, e in segments:
        groups.append([p[s:e] for p in padded])

    return groups


def test_second_day(raw_data: str):

    # operations, numbers = parse_input_second(raw_data)

    operations, numbers_lines = parse_input_lines(raw_data)

    nums_groups = split_into_grid_columns(numbers_lines)

    # str_nums = []

    # for group in nums_groups:
    #     zero_group = [num.replace(" ", "0") for num in group]
    #     str_nums.append(zero_group)
        
    t_nums_groups = [transpose_lists(group) for group in nums_groups]

    int_nums = []
    for group in t_nums_groups:
        int_number = []
        for n_group in group:
            new_number = "".join(n_group)
            int_number.append(int(new_number))
        int_nums.append(int_number)

    return process_opts(operations, int_nums)
            



# ['58  ', '6724', '1311', '6245']

if __name__ == "__main__":

    personal_input = get_input(NUMBER_DAY)

    print(test_second_day(personal_input))

    print(test_second_day(TEST_INPUT))