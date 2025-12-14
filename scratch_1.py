test_value = "123123123"

def check_repeated_pattern(value:str) -> bool:
    length = len(value)

    for i in range(1, length // 2 + 1):
        pattern = value[0:i]
        repeated = pattern * (length // i)
        print(f"Checking pattern '{pattern}' gives '{repeated}'")
        if repeated == value:
            return True

    return False

if __name__ == "__main__":
    result = check_repeated_pattern(test_value)
    print(f"Does '{test_value}' have a repeated pattern? {result}")

