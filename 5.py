from utils.cache_input import get_input

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


if __name__ == "__main__":    

    personal_input = get_input(NUMBER_DAY)

    print(check_id_in_ranges(TEST_INPUT))

    print(check_id_in_ranges(personal_input))