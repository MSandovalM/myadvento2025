from utils.cache_input import get_input
import re

NUMBER_DAY = "5"

TEST_INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def set_entry(raw_input: str):
    line_split = raw_input.split("\n\n")
    ranges, ids = line_split

    return (ranges, ids)


def check_id_in_ranges(raw_input: str):

    ranges, ids = set_entry(raw_input)

    fresh_food = 0
    found_id = False
    for idx in ids.splitlines():
        # print("Cheking for id: ", idx)
        found_id = False
        for rang in ranges.splitlines():
            start, end = rang.split("-")
            # print(f"Range: {start} to {end}")
            if int(idx) >= int(start) and int(idx) <= int(end) and not found_id:
                found_id = True
                fresh_food += 1

    return fresh_food

# Para la segunda parte hay que contar cuantos números hay en los rangos [start, end] incluyendo fronteras
# Funcion para el test pero no para el input personal, son demasiados números... 
def check_ranges(raw_data: str):
    ranges, ids = set_entry(raw_input=raw_data)
    
    num_set = {}

    for ran in ranges.splitlines(): 
        start, end = ran.split("-")

        print(f"Cheking range {start} to {end}")
        
        for num in range(int(start), int(end) + 1):
            num_set[num] = num

    return len(num_set)

def check_sum_ranges(raw_data: str):
    ranges, ids = set_entry(raw_input=raw_data)
    
    num_set = {}

    for ran in ranges.splitlines(): 
        start, end = ran.split("-")



    return len(num_set)    
    
def parse_ranges(ranges_text: str) -> list[tuple[int, int]]:
    intervals = []
    for line in ranges_text.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = line.split("-")
        start, end = int(a), int(b)
        if start > end: 
            start, end = end, start
        intervals.append((start, end))
        return intervals


def parse_ranges_any_format(text: str) -> list[tuple[int, int]]:
    # Accept separators: newline, spaces, commas
    # Extract tokens that look like "number-number"
    tokens = re.findall(r"(-?\d+)\s*-\s*(-?\d+)", text)

    intervals = []
    for a, b in tokens:
        start, end = int(a), int(b)
        if start > end:
            start, end = end, start
        intervals.append((start, end))
    return intervals

def count_unique_nums_in_ranges(ranges_text:str)-> int:
    intervals = parse_ranges_any_format(ranges_text)
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])

    total = 0

    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            total += (cur_end - cur_start +1 )
            cur_start, cur_end = start, end

    total += (cur_end - cur_start + 1)
    return total

def get_raw_ranges(raw_data:str):

    ranges, ids = set_entry(raw_input=raw_data)

    return ranges


if __name__ == "__main__":    

    personal_input = get_input(NUMBER_DAY)

    print(check_id_in_ranges(TEST_INPUT))

    print(check_id_in_ranges(personal_input))

    print(check_ranges(TEST_INPUT))

    print(count_unique_nums_in_ranges(get_raw_ranges(TEST_INPUT)))
    print(count_unique_nums_in_ranges(get_raw_ranges(personal_input)))