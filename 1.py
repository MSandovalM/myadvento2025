"""
Docstring for 1
"""
from pathlib import Path
from dotenv import load_dotenv
import os
import requests 

load_dotenv()
ENDPOINT = "https://adventofcode.com/2025/day/1/input"
CACHE_PATH = Path(__file__).with_suffix(".txt")
DIAL_SIZE = 100
START_POSITION = 50
example_input = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]

def save_input(load):
    if not CACHE_PATH.exists():
        with open(CACHE_PATH, 'w') as file:
            file.write(load)

def get_input():

    if CACHE_PATH.exists():
        with open(CACHE_PATH, 'r') as file:
            return file.read()

    session_cookie = os.getenv("AOC_SESSION")
    result = requests.get(ENDPOINT, cookies={"session": session_cookie})

    if result.status_code == 200: 
        save_input(result.text)
        return result.text
    else:
        print("Error: ", result.status_code)
        print(result.text)
        raise RuntimeError("Error al obtener input")
    

def check_pass_zero()->bool:
    ...


def apply_rotation(position:int, rotation: str) -> int:
    direction = rotation[0]
    steps = int(rotation[1:])
    
    if direction == "L":
        return (position - steps) % DIAL_SIZE
           
    if direction == "R": 
        return (position + steps) % DIAL_SIZE


def count_zero_hits(entry_list:list[str]) -> int:
    
    position = START_POSITION
    zero_hits = 0 

    for rotation in entry_list:
        position = apply_rotation(position, rotation)

        if position == 0: 
            zero_hits += 1

    return zero_hits


def count_zero_pass(entry_list: list[str]) -> tuple:
    pos = START_POSITION
    zero_passes = 0

    for entry in entry_list:
        direction = entry[0]
        value = int(entry[1:])

        full_turns, rem = divmod(value, DIAL_SIZE)
        zero_passes += full_turns

        if rem > 0: 
            if direction == "R":
                if pos > 0 and rem >= DIAL_SIZE - pos:
                    zero_passes += 1
                
                pos = (pos + rem) % DIAL_SIZE

            elif direction == "L":
                if pos > 0 and rem >= pos:
                    zero_passes += 1

                pos = (pos - rem ) % DIAL_SIZE

    return zero_passes, pos 

if __name__ == "__main__":

    aoc_input = get_input()
    in_list = aoc_input.splitlines()
    print(count_zero_hits(in_list))
    print(count_zero_pass(in_list))

    print(count_zero_hits(example_input))
    print(count_zero_pass(example_input))
