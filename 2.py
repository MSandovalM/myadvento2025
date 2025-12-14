from utils.cache_input import get_input

NUMBER_DAY = "2"
test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

small_test_input = "11-22,95-115,998-1012"

def count_entry(entry:str):
    
    count = 0
    total_sum  = 0
    entry_list = entry.split(",")

    for entry in entry_list:
        value = entry.split("-")
        start_value = value[0]
        end_value = value[1]

        for value in range(int(start_value),int(end_value) + 1):

            value_str = str(value)
            
            if len(value_str) % 2 == 0: 

                # split - dividir a la mitad el numero 

                left_val = value_str[0:len(value_str) // 2] 
                right_val = value_str[len(value_str) // 2::]

                if left_val == right_val:

                    total_sum += value
                    count += 1

    print("Total count", count)
    print("Sum of count", total_sum)

# def find_min_prefix(entry:str):

#     entry_list = entry.split(",")

#     for entry in entry_list: 
#         values = entry.split("-")
#         start = values[0]
#         end = values[1]

#         for value in range(int(start), int(end) + 1):
#             value_str = str(value)
#             limit = 1
#             seed = value_str[0:limit]
#             while seed <= len(value_str) // 2:
#                 limit += 1
#                 if seed != value_str[limit + 1: len(seed)]:
#                     break


def find_sum_invalid_numbers(entry:str):
    entry_list = entry.split(",")

    invalid_numbers = []

    for entry in entry_list: 
        values = entry.split("-")
        start = values[0]
        end = values[1]

        for value in range(int(start), int(end) + 1):
            value_str = str(value)
            digits = [int(d) for d in value_str]

            is_valid = True

            for i in range(len(digits) - 1):
                if digits[i] > digits[i + 1]:
                    is_valid = False
                    break

            if is_valid:
                has_double = False
                count_dict = {}

                for digit in digits:
                    if digit in count_dict:
                        count_dict[digit] += 1
                    else:
                        count_dict[digit] = 1

                for count in count_dict.values():
                    if count == 2:
                        has_double = True
                        break

                if not has_double:
                    is_valid = False

            if not is_valid:
                invalid_numbers.append(value)

    total_sum = sum(invalid_numbers)
    print("Sum of invalid numbers:", total_sum)

if __name__ == "__main__":

    entry = get_input(NUMBER_DAY)
    count_entry(entry=entry)

    # find_min_prefix(entry=small_test_input)
    find_sum_invalid_numbers(entry=test_input)
