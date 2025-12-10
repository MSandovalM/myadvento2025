from utils.cache_input import get_input

NUMBER_DAY = "2"
test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

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

def find_the_min_prefix():
    ...

if __name__ == "__main__":

    entry = get_input(NUMBER_DAY)
    count_entry(entry=entry)
