from pathlib import Path
from dotenv import load_dotenv
import os
import requests 

ENDPOINT = "https://adventofcode.com/2025/day"

CACHE_PATH = Path(__file__).with_suffix(".txt")

def env_exist(env_name: str) -> bool:
    if env_name in os.environ:
        return True
    return False

def save_input(number_day:str, load):
    day_cache = Path(number_day).with_suffix(".txt")
    if not day_cache.exists():
        with open(day_cache, 'w') as file:
            file.write(load)

def get_input(number_day: int):

    load_dotenv()

    cache_txt = Path(number_day).with_suffix(".txt")
    day_endpoint = f"{ENDPOINT}/{number_day}/input"

    env_key = "AOC_SESSION"

    if not env_exist(env_key):
        raise EnvironmentError(f"Key: {env_key}, no existe en variables de entorno")

    if cache_txt.exists():
        print(f"Loading {number_day}.txt from cache...")
        with open(cache_txt, 'r') as file:
            return file.read()

    session_cookie = os.getenv(env_key)
    print(f"Requesting... {day_endpoint}")
    result = requests.get(day_endpoint, cookies={"session": session_cookie})

    if result.status_code == 200: 
        save_input(number_day, result.text)
        return result.text
    else:
        print("Error: ", result.status_code)
        print(result.text)
        raise RuntimeError("Error al obtener input")
    

if __name__ == "__main__":
    ...
