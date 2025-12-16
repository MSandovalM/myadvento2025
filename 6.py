from utils.cache_input import get_input
from math import prod

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

if __name__ == "__main__":
    opts, nums = parse_input(TEST_INPUT)

    personal_input = get_input(NUMBER_DAY)

    p_opts, p_nums = parse_input(personal_input)

    # print(opts)
    # print(nums)

    print(len(opts))
    print(len(nums))

    # print(p_opts)
    # print(p_nums)

    print(len(p_opts))
    print(len(p_nums))

    print(process_opts(opts, nums))
    print(process_opts(p_opts, p_nums))

