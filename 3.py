from utils.cache_input import get_input

NUMBER_DAY = "3"
test_input = "987654321111111,811111111111119,234234234234278,818181911112111"

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
    # entry_list = []
    # try:
    #     entry_list = entry_raw.split(",")
    # except SyntaxError:
    #     print("Incorrect entry")

    # try:
    #     entry_list = entry_raw.splitlines()
    # except SyntaxError:
    #     print("Incorrect entry")

    entry_list = entry_raw.splitlines()

    if entry_list:

        sum_values = 0
        for entry in entry_list:
            sum_values += get_max_value(entry)

        return sum_values
    
    return None

def get_answer(entry: str):

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


if __name__ == "__main__":

    personal_input = get_input(NUMBER_DAY)

    # print(first_part(test_input))

    print(first_part(personal_input))