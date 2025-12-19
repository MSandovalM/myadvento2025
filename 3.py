from utils.cache_input import get_input

NUMBER_DAY = "3"
test_input = "234234234234278,987654321111111,811111111111119,818181911112111"

small_test_1 = "987654321111111"

def get_max_value(entry:str) -> int:

    curr_pos = entry[0]
    curr_value = curr_pos + "0"
    max_value = 0
    for index, value in enumerate(entry):

        if value > curr_pos:
            curr_pos = value

        if index < len(entry) - 1:
            curr_value = curr_pos + entry[index + 1]

        max_value = max(max_value, int(curr_value))
        # print("Current Value: ", curr_value)

    # print("Max Value: ", max_value)

    return max_value

def first_part(entry_raw:str):
    entry_list = entry_raw.splitlines()

    if entry_list:

        sum_values = 0
        for entry in entry_list:
            sum_values += get_max_value(entry)

        return sum_values
    
    return None

def second_part(entry_raw:str, test:bool=False) -> int:
    entry_list = []
    sum_entries = 0
    
    if test:
        entry_list = entry_raw.split(",")
    else:
        entry_list = entry_raw.splitlines()

    if entry_list:

        for entry in entry_list:
            result = get_twelve_value(entry)
            sum_entries += int(result)

        return sum_entries
    
    return 0
        
def get_twelve_value(raw_value:str) -> str:
    fixed_len = 12
    n_remaining = len(raw_value)
    d = n_remaining - fixed_len # num of digits to delete
    l_remaining = n_remaining - d
    result_val = ""
    work_str = raw_value
    nums_del = 0
    while l_remaining > 0:
        curr_max = 0
        idx_max = 0
        w_size = n_remaining - l_remaining + 1
        for i in range(0, w_size):
            if int(work_str[i]) > int(curr_max):
                curr_max = work_str[i]
                idx_max = i

        # add value to string
        result_val += curr_max
        # delete everything before max id
        work_str = work_str[idx_max + 1:]
        # how many numbers we deleted?
        nums_del += idx_max

        if nums_del >= d:
            break

        n_remaining -= idx_max + 1
        l_remaining -= 1

    if len(result_val) < fixed_len:
        result_val += work_str

    if len(result_val) == fixed_len:
        return result_val
    else:
        raise ValueError(f"Return error value from {get_twelve_value.__name__}")
    

def get_answer(entry: str):
    """
    Docstring for get_answer: Primer intento...
    
    :param entry: Description
    :type entry: str
    """

    entry_list = entry.split(",")

    for value in entry_list:

        first_pointer = len(value) - 1
        second_pointer = len(value) - 2

        ans_val = 0
        f_digit = value[first_pointer]
        s_digit = value[second_pointer]

        current = s_digit + f_digit

        while second_pointer > 0:
            second_pointer -= 1

            s_digit = value[second_pointer]

            current = s_digit + f_digit

            if value[second_pointer] > value[first_pointer]:
                first_pointer = second_pointer
                second_pointer -= 1
                f_digit = value[first_pointer]
                s_digit = value[second_pointer]

            ans_val = max(ans_val, int(current))

        print(ans_val)


def check_repeated_pattern(value:str) -> bool:
    length = len(value)

    for i in range(1, length // 2 + 1):
        pattern = value[0:i]
        repeated = pattern * (length // i)
        print(f"Checking pattern '{pattern}' gives '{repeated}'")
        if repeated == value:
            return True


if __name__ == "__main__":

    personal_input = get_input(NUMBER_DAY)

    # print(first_part(test_input))

    # print(first_part(personal_input))

    print(second_part(personal_input, test=False))